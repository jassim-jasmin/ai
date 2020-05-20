from os import sep
import joblib
from text_process import tagging, features, get_entity

def get_trained_model(model_name):
    """
    Defalut root directory is model/
    Parameters
    ----------
    model_path name without extension, it save with pkl extesion

    Returns
    -------
    pickle model
    """
    try:
        model_name = f"model{sep}{model_name}.pkl"

        print("loading model ", model_name)
        model = joblib.load(model_name)
        print("completed")

        return model

    except Exception as e:
        print("error in get_trained_model", e)

def get_ner(model_path=None, input_text=None, model=None):
    """
    get named entity
    Parameters
    ----------
    model_path this is optional, when provided load from path else look for model parameter
    input_text processed text, it's mandatory field
    model optional pre loaded model, to avoid model loading from disc

    Returns
    -------
    named entity data
    """
    if model_path:
        model = get_trained_model(model_path)

    if model and input_text:
        tagged_text = tagging(input_text)

        if tagged_text:
            try:
                parsed = features([tagged_text])
                prediction = model.predict(parsed)

                return get_entity(prediction[0], tagging(input_text))

            except Exception as e:
                print("error in get_ner", e)
