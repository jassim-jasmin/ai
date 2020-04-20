from learn.ml.text_classification.google_training.sentiment_analysis.get_dataset import load_imdb_sentiment_analysis_dataset
from learn.ml.text_classification.google_training.sentiment_analysis.explore_data import save_and_get_report
from learn.ml.text_classification.google_training.sentiment_analysis.vectorize_data import ngram_vectorize

data_path = 'C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\dataset'

print("Loading dataset...")
((train_texts, train_labels), (test_texts, test_labels)) = load_imdb_sentiment_analysis_dataset(data_path)
print("Loading dataset completed!!!")


# save_and_get_report({'test': {'data': test_texts, 'labels': test_labels}, 'train': {'data': train_texts, 'labels': train_labels}}, 'dataset_report', 'imdb')T

x_train, x_val = ngram_vectorize(train_texts, train_labels, test_texts)
# (r,f) = x_train[0]
data, indptr, indices = x_train.data, x_train.indptr, x_train.indices

# print('vectorized train', x_train.data)
#
# print(type(x_train.data))
#
# import matplotlib.pyplot as plt
#
# X = x_train.todense()
# from sklearn.decomposition import PCA
# reduced_data = PCA(n_components=2).fit_transform(X)
#
# fig, ax = plt.subplots()
# for index, instance in enumerate(reduced_data):
#     # print instance, index, labels[index]
#     pca_comp_1, pca_comp_2 = reduced_data[index]
#     # color = labels_color_map[labels[index]]
#     ax.scatter(pca_comp_1, pca_comp_2)
# plt.show()
