# Read in and clean data
import gensim
import nltk
import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split
import string

stopwords = nltk.corpus.stopwords.words('english')

# from data.dataset import create_dataset
# create_dataset(r'C:\Users\MOHAMMED JASIM\Documents\resource\dataset\SMSSpamCollection', 'spam')

messages = pd.read_csv('spam.csv')
messages['label'] = np.where(messages['label']=='spam', 1, 0)

def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text

messages['clean_text'] = messages['text'].apply(lambda x: clean_text(x))
messages.head()

# Split data into train and test set
X_train, X_test, y_train, y_test = train_test_split(messages['clean_text'],
                                                    messages['label'], test_size=0.2)

# # Let's save the training and test sets to ensure we are using the same data for each model
# X_train.to_csv('X_train.csv')
# X_test.to_csv('X_test.csv')
# y_train.to_csv('y_train.csv')
# y_test.to_csv('y_test.csv')

# Train a basic word2vec model
w2v_model = gensim.models.Word2Vec(X_train, vector_size=100, window=5, min_count=2)

# Replace the words in each text message with the learned word vector
words = set(w2v_model.wv.index_to_key)
X_train_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words])
                         for ls in X_train])
X_test_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words])
                         for ls in X_test])

# Average the word vectors for each sentence (and assign a vector of zeros if the model
# did not learn any of the words in the text message during training
X_train_vect_avg = []
for v in X_train_vect:
    if v.size:
        X_train_vect_avg.append(v.mean(axis=0))
    else:
        X_train_vect_avg.append(np.zeros(100, dtype=float))

X_test_vect_avg = []

for v in X_test_vect:
    if v.size:
        X_test_vect_avg.append(v.mean(axis=0))
    else:
        X_test_vect_avg.append(np.zeros(100, dtype=float))

# Instantiate and fit a basic Random Forest model on top of the vectors
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf_model = rf.fit(X_train_vect_avg, y_train.values.ravel())

# Use the trained model to make predictions on the test data
y_pred = rf_model.predict(X_test_vect_avg)

# Evaluate the predictions of the model on the holdout test set
from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print('TFIDF\nPrecision: {} / Recall: {} / Accuracy: {}'.format(round(precision, 3), round(recall, 3),
                                                         round((y_pred==y_test).sum()/len(y_pred), 3)))

# WORD TO VEC
# Created TaggedDocument vectors for each text message in the training and test sets
tagged_docs_train = [gensim.models.doc2vec.TaggedDocument(v, [i])
                     for i, v in enumerate(X_train)]
tagged_docs_test = [gensim.models.doc2vec.TaggedDocument(v, [i])
                    for i, v in enumerate(X_test)]

# Train a basic doc2vec
d2v_model = gensim.models.Doc2Vec(tagged_docs_train, vector_size=100, window=5, min_count=2)

train_vectors = [d2v_model.infer_vector(v.words)for v in tagged_docs_train]
test_vectors = [d2v_model.infer_vector(v.words)for v in tagged_docs_test]

# Fit a basic model, make predictions on the holdout test set, and the generate the evaluation metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score

rf = RandomForestClassifier()
rf_model = rf.fit(train_vectors, y_train.values.ravel())

y_pred = rf_model.predict(test_vectors)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print('WORD2VEC\nPrecision: {} / Recall: {} / Accuracy: {}'.format(
    round(precision, 3), round(recall, 3), round((y_pred==y_test).sum()/len(y_pred), 3)))


# RNN
# Train the tokenizer and use that tokenizer to convert the sentences to sequences of numbers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Pad the sequences so each sequence is the same length
X_train_seq_padded = pad_sequences(X_train_seq, maxlen=50)
X_test_seq_padded = pad_sequences(X_test_seq, maxlen=50)

# Import the tools needed and use our previously defined functions to calculate precision and recall
import keras.backend as K
from keras.layers import Dense, Embedding, LSTM
from keras.models import Sequential

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

# Construct our basic RNN model framework
model = Sequential()

model.add(Embedding(len(tokenizer.index_word)+1, 32))
model.add(LSTM(32, dropout=0, recurrent_dropout=0))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# model.summary()

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', precision_m, recall_m])

# Fit the RNN
history = model.fit(X_train_seq_padded, y_train,
                    batch_size=32, epochs=10,
                    validation_data=(X_test_seq_padded, y_test))
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
    plt.show()

#TFIDF: Precision: 0.979 / Recall: 0.58 / Accuracy: 0.937
# WORD2VEC: Precision: 0.966 / Recall: 0.704 / Accuracy: 0.953
# rnn: 0.9830 - val_precision_m: 0.9586 - val_recall_m: 0.9164