import nltk
nltk.download('brown')
from textblob.taggers import NLTKTagger
from textblob import TextBlob

text = '''
other mortgage loan servicing obligations
'''
textArray = [
    'other mortgage loan servicing obligations',
    "NATL AR MOR'I'GAGE LLC D",
    "NATIONSTAR MORTGAGE LLC D / B / A MR"
]
nltk_tagger = NLTKTagger()
for t in textArray:
    blob = TextBlob(t, pos_tagger=nltk_tagger)
    noun_arr = blob.noun_phrases
    print(noun_arr)
# if noun_arr:
# if txt not in result: