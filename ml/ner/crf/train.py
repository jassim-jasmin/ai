import sklearn_crfsuite
import joblib
from os import sep
from ml.ner.crf.text_process import build_crfsuit_dataset
import joblib

def get_model(model_name):
    try:
        model_path = f"model{sep}{model_name}.pkl"

        return joblib.load(model_path)

    except FileNotFoundError as e:
        print(model_path)
        print("error in get_model", e)

def train_model(X_train, Y_train, model_name):
    print("begin training")
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True)

    crf.fit(X_train, Y_train)

    joblib.dump(crf, f"model{sep}{model_name}.pkl")
    print(f"completed and saved model{sep}{model_name}.pkl")

    return crf

def build_model_from_csv(dataset_path, model_name):
    print("downloading dataset")
    X_train, Y_train = build_crfsuit_dataset.from_csv(dataset_path)
    crf = train_model(X_train, Y_train, model_name)
    print("completed")

    return crf
