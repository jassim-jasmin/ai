from learn.ml.text_classification.google_training.get_dataset import load_imdb_sentiment_analysis_dataset
from learn.ml.text_classification.google_training.explore_data import plot_sample_length_distribution, plot_frequency_distribution_of_ngrams
from os import sep

data_path = 'C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\dataset'

((train_texts, train_labels), (test_texts, test_labels)) = load_imdb_sentiment_analysis_dataset(data_path)
print("Loading dataset complete")
plot_sample_length_distribution(train_texts, f'visualization{sep}imdb_train')
plot_sample_length_distribution(test_texts, f'visualization{sep}imdb_test')
plot_frequency_distribution_of_ngrams(train_texts, f'visualization{sep}imdb_train')
plot_frequency_distribution_of_ngrams(test_texts, f'visualization{sep}imdb_test')