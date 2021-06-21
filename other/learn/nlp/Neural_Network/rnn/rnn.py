import keras.backend as k
import matplotlib.pyplot as plt
from keras.layers import Dense, Embedding, LSTM
from keras.models import Sequential
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from data.dataset import create_dataset

create_dataset(dtaset_path=r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\SMSSpamCollection', file_name='spam')

messages = pd.read_csv('spam.csv')
label = np.where(messages['label'] == 'spam', 1, 0)
x_train, x_test, y_train, y_test = train_test_split(messages['text'], label, test_size=0.2)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train)

x_train_seq = tokenizer.texts_to_sequences(x_train)
x_test_seq = tokenizer.texts_to_sequences(x_test)

x_train_seq_pad = pad_sequences(x_train_seq, 50)
x_test_seq_pad = pad_sequences(x_test_seq, 50)


def recall_m(y_true, y_pred):
    true_positive = k.sum(k.round(k.clip(y_true * y_pred, 0, 1)))
    possible_positive = k.sum(k.round(k.clip(y_true, 0, 1)))
    recall = true_positive / (possible_positive + k.epsilon())

    return recall


def precision_m(y_true, y_pred):
    true_positive = k.sum(k.round(k.clip(y_true * y_pred, 0, 1)))
    prediction_positive = k.sum(k.round(k.clip(y_pred, 0, 1)))
    precision = true_positive / (prediction_positive + k.epsilon())

    return precision


model = Sequential()
model.add(Embedding(len(tokenizer.index_word) + 1, 32))
model.add(LSTM(32, dropout=0, recurrent_dropout=0))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', precision_m, recall_m])
history = model.fit(x_train_seq_pad, y_train, batch_size=32, epochs=10, validation_data=(x_test_seq_pad, y_test))
"""
If epoch > then performance decreases, over fitting
If epoch < then performance still increases, under fitting.
"""
for i in ['accuracy', 'precision_m', 'recall_m']:
    acc = history.history[i]
    val_acc = history.history['val_{}'.format(i)]
    epoch = range(1, len(acc) + 1)

    plt.Figure()
    plt.plot(epoch, acc, label='Trainig Accuracy')
    plt.plot(epoch, val_acc, label='Validation Accuracy')
    plt.title('Result for {}'.format(i))
    plt.legend()
    plt.show()


"""
The three components in NN are inputs, process and output
"""