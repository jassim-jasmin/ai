import os
os.environ['DISABLE_V2_BEHAVIOR'] = '1'

import ktrain
from ktrain import text as txt
from pandas import DataFrame

data = [("hi this is jssim", "jassim", "name"),
        ("hi this is jssim", "hi", "t1"),
        ("hi this is jssim", "this", "t2"),
        ("hi this is jishal", "jishal", "name"),
        ("hi this is jishal", "hi", "t1"),
        ("hi this is jishal", "this", "t2"),
        ("hello I'm mark nice to meet you sec", "mark", "name"),
        ("what are you doing mr.Johan", "mr.Johan", "name"),
        ("can i meet you mr.", "you", "t1"),
        ("hello friend jassim", "jassim", "name")]

data = [("Rationale for Dose Selection In a randomized controlled trial comparing IN and IM naloxone for the treatment"\
         " of suspected heroin overdose, a dose in excess of 2 mg of IN naloxone was shown to result in a similar "\
         "response rate", "2 mg", "data"),
        ("Rationale for Dose Selection In a randomized controlled trial comparing IN and IM naloxone for the treatment"
         " of suspected heroin overdose, a dose in excess of 1 mg of IN naloxone was shown to result in a similar "
         "response rate", "1 mg", "data")]

df = DataFrame(data, columns=["data", "word", "label"])
# df.to_csv('dataset\\Book3.csv', encoding='utf-8', index=False)
# load data

path_model_save = 'model\\d_m_model'
path_dataset = 'dataset\\Book3.csv'
# path_dataset = 'dataset\\d1_unorder.csv'
sentence_column = 'data'
word_column = 'word'
tag_column = 'label'


(trn, val, preproc)  = txt.entities_from_df(df,
                    sentence_column=sentence_column,
                    word_column=word_column,
                    tag_column=tag_column)

# (trn, val, preproc) = txt.entities_from_txt(path_dataset,
#                                             sentence_column=sentence_column,
#                                             word_column=word_column,
#                                             tag_column=tag_column)
# load model
model = txt.sequence_tagger('bilstm-crf', preproc)

# wrap model and data in ktrain.Learner object
learner = ktrain.get_learner(model, train_data=trn, val_data=val)

# conventional training for 1 epoch using a learning rate of 0.001 (Keras default for Adam optmizer)
learner.fit(1e-3, 1)

predictor = ktrain.get_predictor(learner.model, preproc)

# predictor.save(path_model_save)

data = predictor.predict('Rationale for Dose Selection In a randomized controlled trial comparing IN and IM naloxone for'\
                         ' the treatment of suspected heroin overdose, a dose in excess of 2 mg of IN naloxone was '\
                         'shown to result in a similar response rate')

print(data)
# test_tesse)