import pandas as pd
from spacy.gold import GoldParse
import spacy

def build_crfsuit_dataset(dataset_csv_path):
    # Loading dataset
    try:
        df_dataset = pd.read_csv(dataset_csv_path)

        # Preprocessing
        def preprocess():
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

        def get_crf_preprocess():
            preprocess_data = preprocess()
            nlp = spacy.load('en_core_web_sm')
            dataset = []
            Y_train = []
            for index, each_row in preprocess_data.iterrows():
                dataset.append(json_to_crf(each_row, nlp))
                Y_train.append(each_row['label'])

            return dataset, Y_train

        def word2features(sent, i):
            word = sent[i][0]
            postag = sent[i][1]
            features = {
                'bias': 1.0,
                'word.lower()': word.lower(),
                'word[-3:]': word[-3:],
                'word[-2:]': word[-2:],
                'word.isupper()': word.isupper(),
                'word.istitle()': word.istitle(),
                'word.isdigit()': word.isdigit(),
                'postag': postag,
                'postag[:2]': postag[:2],
            }
            if i > 0:
                word1 = sent[i - 1][0]
                postag1 = sent[i - 1][1]
                features.update({
                    '-1:word.lower()': word1.lower(),
                    '-1:word.istitle()': word1.istitle(),
                    '-1:word.isupper()': word1.isupper(),
                    '-1:postag': postag1,
                    '-1:postag[:2]': postag1[:2],
                })
            else:
                features['BOS'] = True

            if i < len(sent) - 1:
                word1 = sent[i + 1][0]
                postag1 = sent[i + 1][1]
                features.update({
                    '+1:word.lower()': word1.lower(),
                    '+1:word.istitle()': word1.istitle(),
                    '+1:word.isupper()': word1.isupper(),
                    '+1:postag': postag1,
                    '+1:postag[:2]': postag1[:2],
                })
            else:
                features['EOS'] = True

            return features

        def sent2features(sent):
            return [word2features(sent, i) for i in range(len(sent))]

        def sent2labels(sent):
            return [label for token, postag, label in sent]

        dataset, Y_train = get_crf_preprocess()
        X_train = [sent2features(s) for s in dataset]
        y_train = [sent2labels(s) for s in dataset]
        # Y_train = [label for token, postag, label in dataset]

        return X_train, y_train
    except FileNotFoundError:
        print('ai should be run as working directory')
        exit()