#Tutorial 1
link: https://sklearn-crfsuite.readthedocs.io/en/latest/tutorial.html

In tutorial there is no mentioning about 
nltk.corpus.conll2002.iob_sents is directly used in the code, but need to download conll2002 dataset via nltk. For that
nltk.download('conll2002')
This will fix the issue.
RandomizedSearchCV has update in latest version of sklearn, it is imported as below.
from sklearn.model_selection import RandomizedSearchCV
