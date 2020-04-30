import dotenv
import uvicorn
import os, joblib
from fastapi import FastAPI, Form, Request, Response, HTTPException
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator

dotenv.load_dotenv('.env')

acccount_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_client = Client(acccount_sid, auth_token)

# Vectorizer
gender_vectorizer = open('genclf/genclf/models/gender_vectorizer.pkl', 'rb')
gender_cv = joblib.load(gender_vectorizer)

# Models
gender_nb_model = open('genclf/genclf/models/gender_naive_bayes_model.pkl', 'rb')
gender_clf = joblib.load(gender_nb_model)

app = FastAPI()

# Routes
@app.get('/')
async def index():
    return {'Project':'Twilio Predict'}

@app.get('/names/{name}')
async def get_names(name):
    return {'Name': name}


# Machine Learning Prediction Routes
@app.get('/predict/{name}')
async def predict(name):
    vectorized_name = gender_cv.transform([name]).toarray()
    prediction = gender_clf.predict(vectorized_name)

    if prediction[0] == 0:
        result = 'Female'
    else:
        result = 'Male'

    return {"Given name": name, "Prediction": result}

@app.post('/predict/{name}')
async def predict(name):
    vectorized_name = gender_cv.transform([name]).toarray()
    prediction = gender_clf.predict(vectorized_name)

    if prediction[0] == 0:
        result = 'Female'
    else:
        result = 'Male'

    return {"Given name": name, "Prediction": result}

@app.post('/hook')
async def process_sms(request: Request, From: str = Form(...), Body: str = Form(...)):
    validator = RequestValidator(os.environ["TWILIO_AUTH_TOKEN"])
    form_ = await request.form()
    if not validator.validate(
        str(request.url), 
        form_, 
        request.headers.get("X-Twilio-Signature", "")
    ):
        raise HTTPException(status_code=400, detail="Error in Twilio Signature")

    response = MessagingResponse()

    print(Body)

    vectorized_name = gender_cv.transform([Body]).toarray()
    prediction = gender_clf.predict(vectorized_name)
    if prediction[0] == 0:
        result = 'Female'
    else:
        result = 'Male'

    print(result)

    response.message(result)

    return Response(content=str(response), media_type="application/xml")
    

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)