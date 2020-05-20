from ner_crf import build_model_from_csv
from ner_crf import get_ner
from os import sep

def test():
    model_name = "crf_zillow_v1"
    dataset_path = f"dataset{sep}test{sep}train_data_zillow.csv"
    model_path = f"{model_name}"
    fp = open(f"dataset{sep}test{sep}train_data_zillow_sample.txt", "r")
    input_data = fp.read()
    fp.close()

    build_model_from_csv(dataset_path, model_name)
    ner_data = get_ner(model_path, input_data)

    print(ner_data)

test()