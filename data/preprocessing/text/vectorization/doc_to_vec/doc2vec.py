import gensim.utils
import pandas as pd
from sklearn.model_selection import train_test_split

# from data.dataset import create_dataset


# create_dataset(dtaset_path=r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\SMSSpamCollection', file_name='spam')

message = pd.read_csv('spam.csv')
message['clean_text'] = message['text'].apply(lambda x: gensim.utils.simple_preprocess(x))

x_train, x_test, y_train, y_test = train_test_split(message['clean_text'], message['label'], test_size=0.2)

tagged_docs = [gensim.models.doc2vec.TaggedDocument(x, [i]) for i, x in enumerate(x_train)]

# print(tagged_docs[0])

# doc2vec_model = gensim.models.Doc2Vec(tagged_docs, vector_size=100, window=5, min_count=2)
d2v_model = gensim.models.Doc2Vec(tagged_docs, vector_size=100, window=5, min_count=2)

# print(d2v_model.infer_vector(['I', 'am', 'learning', 'nlp']))

vector = [[d2v_model.infer_vector(x)] for x in x_test]
print(vector[0])
