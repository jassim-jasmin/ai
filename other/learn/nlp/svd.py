from scipy import linalg
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn import decomposition

def predefined_data(vectorizer):
    categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
    remove = ('headers', 'footers', 'quotes')
    newsgroups_train = fetch_20newsgroups(subset='train', categories=categories, remove=remove)
    newsgroups_test = fetch_20newsgroups(subset='test', categories=categories, remove=remove)

    print(type(newsgroups_train.data))

    return vectorizer.fit_transform(newsgroups_train.data).todense()

fp = open("C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p27.txt", "r", encoding="utf8")
data = fp.read()
fp.close()
df = pd.DataFrame({"data": [data]})

data_list = [data]
print(type(data_list))
# print(df)
vectorizer = CountVectorizer(stop_words='english') #, tokenizer=LemmaTokenizer())
# vectors = predefined_data(vectorizer)
vectors = vectorizer.fit_transform(data_list).todense() # (documents, vocab)
print(vectors.shape) #, vectors.nnz / vectors.shape[0], row_means.shape
#
vocab = np.array(vectorizer.get_feature_names())
#
# print(vocab)
# print(vocab.shape)
# print(vocab[700:702])
#
U, s, Vh = linalg.svd(vectors, full_matrices=False)
#
# print(U.shape, s.shape, Vh.shape)
print('diagonal', np.diag(s[:4]))
#
#
num_top_words=8

def show_topics(a):
    top_words = lambda t: [vocab[i] for i in np.argsort(t)[:-num_top_words-1:-1]]
    topic_words = ([top_words(t) for t in a])
    return [' '.join(t) for t in topic_words]

topics = show_topics(Vh)
print(topics)

# NMF
d = 10
clf = decomposition.NMF(n_components=d, random_state=1)

W1 = clf.fit_transform(vectors)
H1 = clf.components_

topics = show_topics(H1)

print("nmf", topics)