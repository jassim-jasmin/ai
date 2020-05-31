import re
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nameparser.parser import HumanName

def Sorting(lst):
    lst2 = sorted(lst, key=len,reverse=True)
    return lst2

capsWords = re.findall('([A-Z\s*.]{2,})', text)

capsWordsSorted = Sorting(capsWords)

for eachWords in capsWordsSorted:
    eachWordsNew = eachWords.title()
    text = text.replace(eachWords, eachWordsNew)
    resultString.append(eachWordsNew)

names = get_human_names(text)

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""

    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)