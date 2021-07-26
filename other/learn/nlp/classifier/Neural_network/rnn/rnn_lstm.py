from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential


def load_data():
    import pandas as pd
    path = r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\sarcasm_news\Sarcasm_Headlines_Dataset.json'
    data = pd.read_json(path, lines=True)

    return data

news = load_data()
headlines = list(news['headline'])
labels = list(news['is_sarcastic'])

vocab_size=10000
max_length = 120
embedding_dim = 32
trunc_type = 'post'
padding_type = 'post'
oov_toc = '<oov>'
training_size = 20000

train_sentance, test_sentance, train_labels, test_labels = train_test_split(headlines, labels, test_size=0.2)

tokenizer = Tokenizer(vocab_size,oov_token=oov_toc)
tokenizer.fit_on_texts(train_sentance)
word_index = tokenizer.word_index

training_sequence = tokenizer.texts_to_sequences(train_sentance)
training_padded = pad_sequences(training_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

test_sequence = tokenizer.texts_to_sequences(test_sentance)
test_padded = pad_sequences(test_sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)

import numpy as np

training_padded = np.array(training_padded)
test_padded = np.array(test_padded)
train_labels = np.array(train_labels)
test_labels = np.array(test_labels)

from tensorflow.keras.layers import Dense, LSTM, Embedding, Bidirectional
import tensorflow as tf

# model = Sequential()
# # model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
# model.add(Embedding(len(tokenizer.index_word)+1, embedding_dim, input_length=max_length))
# model.add(Bidirectional(LSTM(64, return_sequences=True)))
# model.add(Bidirectional(LSTM(32)))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.summary()
#
# epoch = 32
#
# history = model.fit(training_padded, train_labels, epochs=epoch, validation_data=[test_padded, test_sequence], verbose=2)



model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
