from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from other.learn.nlp.classifier.random_forest import RandomForestClassifierModel
from other.learn.nlp.classifier.embeddings import Embeddings
from other.learn.nlp.classifier.preprocessing import simple_preprocessing
from other.learn.nlp.classifier.naive_bays_classifier import NaiveBayesClassifier


def spam_classifier():
    messages = pd.read_csv('spam.csv')
    messages['label'] = np.where(messages['label'] == 'spam', 1, 0)
    messages['clean_text'] = messages['text'].apply(lambda x: simple_preprocessing(x))

    X_train, X_test, y_train, y_test = train_test_split(messages['clean_text'], messages['label'], test_size=0.2)

    embeddings = Embeddings()

    all_embeddings = embeddings.get_all_embeddings(X_train, X_test)
    precision_list = []
    recall_list = []
    accuracy_list = []
    embeddings = []

    for name, values in all_embeddings.items():
        embeddings.append(f"Random forest_{name}")
        train_vectors, test_vectors = values
        rfc_model = RandomForestClassifierModel.get_model(train_vectors, y_train)

        precision, recall, accuracy = RandomForestClassifierModel.get_precision_and_recall(rfc_model, test_vectors,
                                                                                           y_test)
        print(f"Random forest, {name}, precision: {precision}, recall: {recall}, accuracy: {accuracy}")
        precision_list.append(precision)
        recall_list.append(recall)
        accuracy_list.append(accuracy)

        naive_bayes = NaiveBayesClassifier()
        naive_bayes.get_model(train_vectors, test_vectors, y_train, name)
        precision, recall, accuracy = naive_bayes.get_precision_and_recall(test_vectors, y_test, name)
        precision_list.append(precision)
        recall_list.append(recall)
        accuracy_list.append(accuracy)
        embeddings.append(f"naive_bayes_{name}")

    return precision_list, recall_list, accuracy_list, embeddings


def draw_graph(precision_list, recall_list, accuracy_list, embedding):
    import matplotlib.pyplot as plt
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))

    # Set position of bar on X axis
    br1 = np.arange(len(precision_list))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    # Make the plot
    plt.bar(br1, precision_list, color='r', width=barWidth,
            edgecolor='grey', label='precision')
    plt.bar(br2, recall_list, color='g', width=barWidth,
            edgecolor='grey', label='recall')
    plt.bar(br3, accuracy_list, color='b', width=barWidth,
            edgecolor='grey', label='accuracy')

    # Adding Xticks
    plt.xlabel('Model', fontweight='bold', fontsize=15)
    plt.ylabel('Values', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(precision_list))],
               embedding)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    precision_list, recall_list, accuracy_list, embedding = spam_classifier()
    draw_graph(precision_list, recall_list, accuracy_list, embedding)