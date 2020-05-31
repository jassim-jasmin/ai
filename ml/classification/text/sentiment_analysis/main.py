from ml.classification.text.sentiment_analysis.train.main import train_ngram_model
from ml.classification.text.sentiment_analysis.get_dataset import load_local_csv_dataset, load_imdb_sentiment_analysis_dataset

path_dataset = "C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\dataset\\nalaxone_arm_validation.csv"
data_path = 'C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\dataset'
data =load_local_csv_dataset(path_dataset)
# data = load_imdb_sentiment_analysis_dataset(data_path)
model = train_ngram_model(data)