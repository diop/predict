# Core packages

import os, joblib
import warnings 
warnings.filterwarnings('ignore')

PACKAGE_DIR = os.path.dirname(__file__)

class GenderClassifier(object):
    """genderClassifier"""
    def __init__(self, name=None):
        super(GenderClassifier, self).__init__()
        self.name = name

    def __repr__(self):
        return f'GenderClassifier(name={self.name})'

    def predict(self):
        # Load vectorizer
        gender_vectorizer = open(os.path.join(PACKAGE_DIR, 'models/gender_vectorizer.pkl'), 'rb')
        gender_cv = joblib.load(gender_vectorizer)

        # Load Models
        gender_nb_model = open(os.path.join(PACKAGE_DIR, 'models/gender_naive_bayes_model.pkl'), 'rb')
        gender_clf = joblib.load(gender_nb_model)
        
        # Vectorization
        vectorized_data = gender_cv.transform([self.name]).toarray()
        prediction = gender_clf.predict(vectorized_data)

        if prediction[0] == 0:
            result = 'female'
        elif prediction[0] == 1:
            result = 'male'

        return result

    def load(self, model_type):
        if model_type == 'nb':
            gender_nb_model = open(os.path.join(PACKAGE_DIR, 'models/gender_naive_bayes_model.pkl'), 'rb')
            gender_clf = joblib.load(gender_nb_model)
        elif model_type == 'logistic':
            gender_logistic_model = open(os.path.join(PACKAGE_DIR, 'models/gender_logistic_model.pkl'), 'rb')
            gender_clf = joblib.load(gender_logistic_model)
        else:
            print('Please chose a model [nb:naiveBayes, logistic:logisticRegression]')

        return gender_clf
