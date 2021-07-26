import keras.backend as K


def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def load_data():
    import pandas as pd
    path = r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\sarcasm_news\Sarcasm_Headlines_Dataset.json'
    data = pd.read_json(path, lines=True)

    return data

news = load_data()
headlines = list(news['headline'])
labels = list(news['is_sarcastic'])

vocab_size = 10000
max_length = 120
embedding_dim = 30
truc_type = 'post'
padding_type = 'post'
oov_tok = '<oov>'
num_epoch = 25
fig_number = 19

data = load_data()

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import AveragePooling1D
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
import numpy as np

X_train, X_test, Y_train, Y_test = train_test_split(data['headline'], data['is_sarcastic'], test_size=0.2)

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(X_train)
word_index = tokenizer.word_index

training_sequence = np.array(tokenizer.texts_to_sequences(X_train))
training_padding = np.array(pad_sequences(training_sequence, maxlen=max_length, truncating='post', padding='post'))

test_sequence = np.array(tokenizer.texts_to_sequences(X_test))
test_padding = np.array(pad_sequences(test_sequence, maxlen=max_length, truncating='post', padding='post'))

model = Sequential()
# model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
model.add(Embedding(len(tokenizer.index_word)+1, embedding_dim, input_length=max_length))
# model.add(AveragePooling1D())
model.add(Flatten())
model.add(Dense(embedding_dim, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', precision_m, recall_m])
model.summary()


history = model.fit(training_padding, Y_train, epochs=num_epoch, validation_data=(test_padding, Y_test), verbose=2,
                    batch_size=max_length)

import matplotlib.pyplot as plt

for i in ['accuracy', 'precision_m', 'recall_m']:
    acc = history.history[i]
    val_acc = history.history['val_{}'.format(i)]
    epoch = range(1, len(acc) + 1)

    plt.Figure()
    plt.plot(epoch, acc, label='Trainig Accuracy')
    plt.plot(epoch, val_acc, label='Validation Accuracy')
    plt.title('Result for {}'.format(i))
    plt.legend()
    plt.savefig(f'{i}_fig_{fig_number}.png')
    plt.close()