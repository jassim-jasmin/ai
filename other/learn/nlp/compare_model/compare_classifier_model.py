from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from other.learn.nlp.classifier.random_forest import RandomForestClassifierModel
from other.learn.nlp.classifier.embeddings import Embeddings
from other.learn.nlp.classifier.preprocessing import simple_preprocessing


def spam_classifier():
    messages = pd.read_csv('spam.csv')
    messages['label'] = np.where(messages['label'] == 'spam', 1, 0)
    messages['clean_text'] = messages['text'].apply(lambda x: simple_preprocessing(x))

    X_train, X_test, y_train, y_test = train_test_split(messages['clean_text'], messages['label'], test_size=0.2)

    embeddings = Embeddings()

    all_embeddings = embeddings.get_all_embeddings(X_train, X_test)

    for name, values in all_embeddings.items():
        train_vectors, test_vectors = values
        rfc_model = RandomForestClassifierModel.get_model(train_vectors, y_train)

        precision, recall, accuracy = RandomForestClassifierModel.get_precision_and_recall(rfc_model, test_vectors,
                                                                                           y_test)
        print(f"Random forest, {name}, precision: {precision}, recall: {recall}, accuracy: {accuracy}")


if __name__ == "__main__":
    spam_classifier()
