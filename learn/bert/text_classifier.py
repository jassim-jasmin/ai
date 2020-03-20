# https://towardsdatascience.com/bert-text-classification-in-3-lines-of-code-using-keras-264db7e7a358

import ktrain
from ktrain import text
def train():
    path = '/root/.keras/datasets/aclImdb'
    # path = '/root/mj/python/ai/dataset/aclImdb'

    # loading and preprocessing
    (x_train, y_tain), (x_test, y_test), preproc = text.texts_from_folder(path,maxlen=500,preprocess_mode='bert', classes=['pos','neg'])

    # loading bert model
    model = text.text_classifier('bert', (x_train,y_tain),preproc)
    learner = ktrain.get_learner(model, train_data=(x_train,y_tain), val_data=(x_test, y_test), batch_size=6)

    # trainig the model
    learner.fit_onecycle(2e-5,1)
    learner.validate(val_data=(x_test, y_test))

    predidtor = ktrain.get_predictor(learner.model, preproc)

    predidtor.save('/root/mj/python/ai/model_learn/aclimdb')

    return True

train()

test_text = """
Once again Mr. Costner has dragged out a movie for far longer than necessary. Aside from the terrific sea rescue sequences, of which there are very few I just did not care about any of the characters. Most of us have ghosts in the closet, and Costner's character are realized early on, and then forgotten until much later, by which time I did not care. The character we should really care about is a very cocky, overconfident Ashton Kutcher. The problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a cluttered closet. His only obstacle appears to be winning over Costner. Finally when we are well past the half way point of this stinker, Costner tells us all about Kutcher's ghosts. We are told why Kutcher is driven to be the best with no prior inkling or foreshadowing. No magic here, it was all I could do to keep from turning it off an hour in."""

predictor = ktrain.load_predictor('./model/aclimdb')
value = predictor.predict(test_text)

print(value)