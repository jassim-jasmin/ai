import numpy as np
import tensorflow.keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# from sklearn.model_selection import train_test_split

def tokanize_word_list(word_list, vocab_size=100, oov_token='<oov>'):
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
    tokenizer.fit_on_texts(word_list)

    return tokenizer

def load_data():
    import pandas as pd
    path = r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\sarcasm_news\Sarcasm_Headlines_Dataset.json'
    data = pd.read_json(path, lines=True)

    return data

sentance = ['this is a test sentence', 'and this is another test sentance', 'i hope this will works']

# tokenizer = tokanize_word_list(sentance)
# padded_sequences = pad_sequences(tokenizer.texts_to_sequences(sentance),maxlen=50, padding='post', truncating='post')
# print(padded_sequences)

# news = load_data()
# headlines = list(news['headline'])
# labels = list(news['is_sarcastic'])
#
# tokenizer = tokanize_word_list(headlines)
# padding_sequence = pad_sequences(tokenizer.texts_to_sequences(headlines), maxlen=50, padding='post', truncating='post')
# print(padding_sequence)
#
# x_train, x_test, y_train, y_test = train_test_split(headlines, labels, test_size=0.2)

import tensorflow_datasets as tfds

data, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)

train_data, test_data = data['train'], data['test']
train_data_sentance = []
train_data_label = []
test_data_sentance = []
test_data_label = []


for sent, label in train_data:
    train_data_sentance.append(sent.numpy().decode('utf8'))
    train_data_label.append(label.numpy())

for sent, label in test_data:
    test_data_sentance.append(sent.numpy().decode('utf8'))
    test_data_label.append(label.numpy())

train_labels = np.array(train_data_label)
test_labels = np.array(test_data_label)

vocab_size = 10000
embedding_dim = 16
max_lenght = 150
truc_type = 'post'
oov_toc = '<oov>'

tokenizer = tokanize_word_list(word_list=train_data_sentance, vocab_size=vocab_size, oov_token=oov_toc)
import tensorflow as tf
train_padding = pad_sequences(tokenizer.texts_to_sequences(train_data_sentance), maxlen=max_lenght, truncating=truc_type)
test_padding = pad_sequences(tokenizer.texts_to_sequences(test_data_sentance), maxlen=max_lenght, truncating=truc_type)

# model = tensorflow.keras.Sequential(
#      tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_lenght),
#      tf.keras.layers.Flatten(),
#      tf.keras.layers.Dense(6, activation='relu'),
#      tf.keras.layers.Dense(1, activation='sigmoid')
#  )
model = tensorflow.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_lenght))
model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.AveragePooling1D())
model.add(tf.keras.layers.Dense(6, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
num_epochs = 10
model.fit(train_padding, train_labels, epochs=num_epochs, validation_data=(test_padding, test_labels))

l1 = model.layers[0]
weights = l1.get_weights()

import io

vectors = io.open('vectors.tsv', 'w', encoding='utf-8')
meta = io.open('meta.tsv', 'w', encoding='utf-8')

word_index = tokenizer.word_index
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
weights = l1.get_weights()[0]

for index in range(1, vocab_size):
    word = reverse_word_index[index]
    embeddings = weights[index]
    meta.write(word + '\n')
    vectors.write('\t'.join([str(x) for x in embeddings]) + "\n")

vectors.close()
meta.close()

