from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score


class RandomForestClassifierModel:
    @staticmethod
    def get_model(x_train_vectors, y_train):
        rf = RandomForestClassifier()

        rf_model = rf.fit(x_train_vectors, y_train.values.ravel())

        return rf_model

    @staticmethod
    def get_precision_and_recall(rf_model, x_test_vectors, y_test):
        y_pred = rf_model.predict(x_test_vectors)
        precision = round(precision_score(y_test, y_pred), 3)
        recall = round(recall_score(y_test, y_pred), 3)
        accuracy = round((y_pred == y_test).sum() / len(y_pred), 3)

        return precision, recall, accuracy
