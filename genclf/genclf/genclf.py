# Core packages

import os, joblib

class GenderClassifier(object):
    """genderClassifier"""
    def __init__(self, name=None):
        super(GenderClassifier, self).__init__()
        self.name = name

    def __repr__(self):
        return f'GenderClassifier(name={self.name})'
