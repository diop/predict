from genclf import __version__
from genclf import GenderClassifier

def test_version():
    assert __version__ == '0.0.1'

def test_genclf_for_male():
    g = GenderClassifier()
    g.name = 'Mark'
    result = g.predict()
    assert result == 'male'

def test_genclf_for_female():
    g = GenderClassifier()
    g.name = 'Abigail'
    result = g.predict()
    assert result == 'female'
