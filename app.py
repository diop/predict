import uvicorn
from fastapi import FastAPI

# Machine Learning Package
import os, joblib

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


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)