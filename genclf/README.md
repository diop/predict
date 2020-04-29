## GenderClassifier Tool
Classify gender of individuals using their first names

### Installation
```bash
pip install genclf
```

### Usage
#### Basic usage
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Barack'
>>> g.predict()
```

#### Loading Different Models
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Jessica'
>>> g.load('logistic')
>>> g.predict()
```

#### Using the Classify Method
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.load('nb')
>>> g.classify("George")
```

#### Check Gender
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_male("Marcus")
```

```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_female("Abigail")
```

#### Requirements
+ Joblib
+ Scikit-learn

#### Maintainer
+ Fodé Diop