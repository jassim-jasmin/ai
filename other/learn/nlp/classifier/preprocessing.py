import nltk
import re
import string


def simple_preprocessing(text):
    stopwords = nltk.corpus.stopwords.words('english')
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split(r'\W+', text)
    text = [word for word in tokens if word not in stopwords]

    return text
