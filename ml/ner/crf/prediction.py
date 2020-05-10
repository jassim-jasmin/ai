from os import sep
import joblib
from ml.ner.crf.text_process.common import tagging, features, get_entity

def get_trained_model(model_path):
    try:
        model_path = f"model{sep}{model_path}.pkl"

        print("loading model ", model_path)
        model = joblib.load(model_path)
        print("completed")

        return model

    except Exception as e:
        print("error in get_trained_model", e)

def get_ner(model_path, input_text):
    model = get_trained_model(model_path)

    if model:
        tagged_text = tagging(input_text)

        if tagged_text:
            try:
                parsed = features([tagged_text])
                prediction = model.predict(parsed)

                return get_entity(prediction[0], tagging(input_text))

            except Exception as e:
                print("error in get_ner", e)
