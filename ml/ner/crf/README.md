#Conditional Random Fields (CRF)
##Named Entity Recognition
###sklearn-crfsuite `version: 0.36`

This is a general crf ner program. Mainly  `train.py` `prediction.py` `text_process\build_crfsuit_dataset.py` `commonn.py`

`main.py` is  a temporary test file.

Trained model is saved as `pkl` file in local directory `model` with an extesion of `pkl`

####Installation
    python setup.py install

####Implementation
#####For training
    from ner_crf import build_model_from_csv
    
    build_model_from_csv(dataset_path, model_name)

Model will be saved in model/model_name.pkl 

_Note!! directory **model** need to create manually_
#####For prediction
        from ner_crf import import get_ner
        
        prediction_data = get_ner(model_path, input_data)
