# import gensim.downloader as api

# wikipedia_embeddings = api.load('glove-wiki-gigaword-100')
# value_of_king = wikipedia_embeddings['king']
# value_with_similarity_of_king = wikipedia_embeddings.most_similar('king')
import gensim.utils
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


def create_dataset():
    data = ''

    with open(r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\SMSSpamCollection', mode='r') as fp:
        data = fp.read()


    list_data = data.split('\n')

    dataframe = pd.DataFrame(columns=['label', 'text'])

    for index, each_data in enumerate(list_data):
        each_data = each_data.replace('\t', ' ')
        split_data = each_data.split(' ', 1)

        if split_data[0]:
            dataframe.loc[index] = split_data

    dataframe.to_csv('spam.csv')


# create_dataset()

dataframe = pd.read_csv('spam.csv')
dataframe['clean_text'] = dataframe['text'].apply(lambda x: gensim.utils.simple_preprocess(x))
# print(dataframe)
x_train, x_test, y_train, y_test = train_test_split(dataframe['clean_text'], dataframe['label'])
w2v_model = gensim.models.Word2Vec(x_train, vector_size=100, window=5, min_count=2)
# print(w2v_model)
# print(w2v_model.wv.index_to_key)
# print(x_test)

w2v_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in w2v_model.wv.index_to_key]) for ls in x_test])
# #
# # print(w2v_vect)
# #
# for index, v in enumerate(w2v_vect):
#     print(len(x_test.iloc[index]), len(v))

w2v_vec_avg = []

for vec in w2v_vect:
    if len(vec) != 0:
        w2v_vec_avg.append(vec.mean(axis=0))

    else:
        w2v_vec_avg.append(np.zeros(100))

for index, v in enumerate(w2v_vec_avg):
    print(len(x_test.iloc[index]), len(v))