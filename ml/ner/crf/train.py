import sklearn_crfsuite
import joblib
from os import sep
from ml.ner.crf.text_process import build_crfsuit_dataset

def get_crf(max_iterations=100, all_possible_transitions=True, c2=None, c1=None, algorithm='lbfgs'):
    return sklearn_crfsuite.CRF(
        algorithm=algorithm,
        c1=c1,
        c2=c2,
        max_iterations=max_iterations,
        all_possible_transitions=all_possible_transitions)

def save_pickle(model, model_name):
    try:
        joblib.dump(model, f"model{sep}{model_name}.pkl")

    except Exception as e:
        print("error in save_pickle")

def get_model(model_name):
    try:
        model_path = f"model{sep}{model_name}.pkl"

        return joblib.load(model_path)

    except FileNotFoundError as e:
        print(model_path)
        print("error in get_model", e)

def train_model(X_train, Y_train, model_name):
    print("begin training")
    crf = get_crf(c1=0.1, c2=0.1)

    crf.fit(X_train, Y_train)

    save_pickle(crf, model_name)
    print(f"completed and saved model{sep}{model_name}.pkl")

    return crf

def build_model_from_csv(dataset_path, model_name):
    print("downloading dataset")
    X_train, Y_train = build_crfsuit_dataset.from_csv(dataset_path)
    crf = train_model(X_train, Y_train, model_name)
    print("completed")

    return crf
