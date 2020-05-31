import re
import string
import spacy


def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i - 1][0]
        postag1 = sent[i - 1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True
    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        postag1 = sent[i + 1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True
    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def preprocess(data):
    finallist_single_line = []
    finallist_single_line.append(tagging(data))
    test_single_line = [sent2features(s) for s in finallist_single_line]

    return test_single_line

def extractEntities(predicted,tagged):
    rslt = {}
    label=''
    for i in range(len(predicted)):
#        print(y_pred[0][j])
        if predicted[i].startswith('U-'):
            label = tagged[i][0]
            try:
                rslt[predicted[i][2:]].append(label)
            except:
                rslt[predicted[i][2:]] = [label]
            label=''
            continue
        if predicted[i].startswith('B-'):
            label += tagged[i][0]+" "
        if predicted[i].startswith('I-'):
            label += tagged[i][0]+" "
        if predicted[i].startswith('L-'):
            label += tagged[i][0]
            try:
                rslt[predicted[i][2:]].append(label)
            except:
                rslt[predicted[i][2:]] = [label]
            label=''
            continue
    return rslt

def tagging(data):
    nlp = spacy.load('en_core_web_sm')
    # data = data.lower()
    processed_text = re.sub(f'[^{re.escape(string.printable)}]', '', data)
    parsed = nlp(processed_text)
    tagged = []

    for i in range(len(parsed)):
        tagged.append((str(parsed[i]), parsed[i].tag_))

    return tagged