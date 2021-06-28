from keras.layers import Dense, Embedding, LSTM
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras.backend as K


class NeuralNetwork:
    @staticmethod
    def recall_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    @staticmethod
    def precision_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

    def sequence_feature(self, X_train, X_test):
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(X_train)


        X_train_seq = self.tokenizer.texts_to_sequences(X_train)
        X_test_seq = self.tokenizer.texts_to_sequences(X_test)

        return X_train_seq, X_test_seq

    def sequence_padding(self, X_train_seq, X_test_seq):
        # Pad the sequences so each sequence is the same length
        X_train_seq_padded = pad_sequences(X_train_seq, maxlen=50)
        X_test_seq_padded = pad_sequences(X_test_seq, maxlen=50)

        return X_train_seq_padded, X_test_seq_padded

    @staticmethod
    def get_precision_and_recall(history):
        accuracy = history.history['accuracy'].pop()
        precision_m = history.history['precision_m'].pop()
        recall_m = history.history['recall_m'].pop()
        print(f"Neural network: precision: {precision_m}, recall: {recall_m}, accuracy: {accuracy}")

        return accuracy, precision_m, recall_m


    def get_model(self, X_train, X_test, y_train, y_test):
        X_train_seq, X_test_seq = self.sequence_feature(X_train, X_test)
        X_train_seq_padded, X_test_seq_padded = self.sequence_padding(X_train_seq, X_test_seq)

        # Construct our basic RNN model framework
        self.model = Sequential()

        self.model.add(Embedding(len(self.tokenizer.index_word) + 1, 32))
        self.model.add(LSTM(32, dropout=0, recurrent_dropout=0))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        # model.summary()

        # Compile the model
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', self.precision_m, self.recall_m])
        # Fit the RNN
        history = self.model.fit(X_train_seq_padded, y_train,
                            batch_size=32, epochs=10,
                            validation_data=(X_test_seq_padded, y_test))

        return history