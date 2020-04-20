import sklearn_crfsuite
import joblib
from os import sep

from learn.CRF_learn.training_dir.load_dataset import build_crfsuit_dataset

def build_model(dataset_path, model_name):
    X_train, Y_train = build_crfsuit_dataset(dataset_path)

    crf = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100,
            all_possible_transitions=True)

    crf.fit(X_train, Y_train)

    joblib.dump(crf, f"model{sep}{model_name}.pkl")

    return crf

model_path = 'test_2'

dataset_path = f'dataset{sep}train_data_zillow.csv'
dataset_path = "C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\dataset\\test\\train_data_zillow.csv"

# build_model(dataset_path, model_path)