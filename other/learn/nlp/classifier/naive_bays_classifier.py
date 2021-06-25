from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, recall_score


class NaiveBayesClassifier:
    def __init__(self):
        self.model = None

    def get_model(self, train_vectors, y_train, embedding_name=None):
        """
        features in decimal form
        """
        self.model = GaussianNB()

        if embedding_name == 'tfidf':
            self.model.fit(train_vectors.toarray(), y_train)
        else:
            self.model.fit(train_vectors, y_train)

    def get_precision_and_recall(self, test_vectors, y_test, embedding_name=None):
        if embedding_name == 'tfidf':
            y_pred = self.model.predict(test_vectors.toarray())

        else:
            y_pred = self.model.predict(test_vectors)
        precision = round(precision_score(y_test, y_pred), 3)
        recall = round(recall_score(y_test, y_pred), 3)
        accuracy = round((y_pred == y_test).sum() / len(y_pred), 3)
        print(f"Naive Bayes, {embedding_name}, precision: {precision}, recall: {recall}, accuracy: {accuracy}")

        return precision, recall, accuracy