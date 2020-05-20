from text_process.common import sent2labels, sent2features
from spacy.gold import GoldParse
import spacy
import pandas as pd

def from_csv(dataset_csv_path):
    def remove_character(df_dataset):
        df_dataset["data"] = df_dataset["data"].str.replace(":", " ")
        df_dataset["data"] = df_dataset["data"].str.replace(".", " ")
        # df_dataset["data"] = df_dataset["data"].str.lower()

        return df_dataset

    def json_to_crf(each_row, nlp):
        entity_offsets = []
        doc = nlp(each_row['data'])

        entity_offsets.append(tuple((each_row['start'], each_row['end'], each_row['label'])))
        gold = GoldParse(doc, entities=entity_offsets)
        ents = [l[5] for l in gold.orig_annot]
        crf_format = [(doc[i].text, doc[i].tag_, ents[i]) for i in range(len(doc))]
        #    print(crf_format)
        return crf_format

    def get_crf_preprocess(df_dataset):
        preprocess_data = remove_character(df_dataset)
        nlp = spacy.load('en_core_web_sm')
        dataset = []
        Y_train = []

        for index, each_row in preprocess_data.iterrows():
            dataset.append(json_to_crf(each_row, nlp))
            Y_train.append(each_row['label'])

        return dataset, Y_train

    df_dataset = pd.read_csv(dataset_csv_path)
    dataset, Y_train = get_crf_preprocess(df_dataset)
    X_train = [sent2features(s) for s in dataset]
    y_train = [sent2labels(s) for s in dataset]

    return X_train, y_train