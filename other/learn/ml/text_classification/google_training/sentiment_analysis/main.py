from other.learn.ml.text_classification.google_training.sentiment_analysis.get_dataset import load_imdb_sentiment_analysis_dataset

data_path = '/dataset'
path_dataset = "/dataset/nalaxone_arm_validation.csv"

print("Loading dataset...")
((train_texts, train_labels), (test_texts, test_labels)) = load_imdb_sentiment_analysis_dataset(data_path)
# ((train_texts, train_labels), (test_texts, test_labels)) = load_local_csv_dataset(path_dataset)
print("Loading dataset completed!!!")


# save_and_get_report({'test': {'data': test_texts, 'labels': test_labels}, 'train': {'data': train_texts, 'labels': train_labels}}, 'dataset_report', 'ta_arm')

# x_train, x_val = ngram_vectorize(train_texts, train_labels, test_texts)
# # (r,f) = x_train[0]
# data, indptr, indices = x_train.data, x_train.indptr, x_train.indices
#
# t = x_val.toarray()
# print(t)

# min_value = min(t)


# for i in range(len(t)):
#     each_max = max(t[i])
#
#     if each_max == 0:
#         print('other', i)
#     else:
#         print("nalaxone", i)

# for data in x_val:
#     print("values", data[0,...])
#     print("data", data)
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

def _get_last_layer_units_and_activation(num_classes):
    """Gets the # units and activation function for the last network layer.

    # Arguments
        num_classes: int, number of classes.

    # Returns
        units, activation values.
    """
    if num_classes == 2:
        activation = 'sigmoid'
        units = 1
    else:
        activation = 'softmax'
        units = num_classes
    return units, activation

# build ngram model
from tensorflow.python.keras import models
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Dropout

def mlp_model(layers, units, dropout_rate, input_shape, num_classes):
    """Creates an instance of a multi-layer perceptron model.

    # Arguments
        layers: int, number of `Dense` layers in the model.
        units: int, output dimension of the layers.
        dropout_rate: float, percentage of input to drop at Dropout layers.
        input_shape: tuple, shape of input to the model.
        num_classes: int, number of output classes.

    # Returns
        An MLP model instance.
    """
    op_units, op_activation = _get_last_layer_units_and_activation(num_classes)
    model = models.Sequential()
    model.add(Dropout(rate=dropout_rate, input_shape=input_shape))

    for _ in range(layers-1):
        model.add(Dense(units=units, activation='relu'))
        model.add(Dropout(rate=dropout_rate))

    model.add(Dense(units=op_units, activation=op_activation))
    return model