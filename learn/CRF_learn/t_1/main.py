import nltk
from ml.ner.crf.text_process.common import sent2features, sent2labels
from ml.ner.crf.train import train_model, get_model, get_crf, save_pickle
from sklearn_crfsuite import metrics

# loading train, test data
nltk.download('conll2002')
train_sents = list(nltk.corpus.conll2002.iob_sents('esp.train'))
test_sents = list(nltk.corpus.conll2002.iob_sents('esp.testb'))

X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

X_test = [sent2features(s) for s in test_sents]
y_test = [sent2labels(s) for s in test_sents]
#
# crf = train_model(X_train, y_train, model_name) # If model saved local no need to train again, comment it.

model_name = "crf_conll2002_spanish"
crf = get_model(model_name) # loading pretrained model

# Evaluation
labels = list(crf.classes_)
labels.remove('O')
print(labels)

y_pred = crf.predict(X_test)
socre = metrics.flat_f1_score(y_test, y_pred,
                      average='weighted', labels=labels)
print(socre)

# group B and I results
sorted_labels = sorted(
    labels,
    key=lambda name: (name[1:], name[0])
)

print(metrics.flat_classification_report(
    y_test, y_pred, labels=sorted_labels, digits=3
))

# Hyperparameter Optimization
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV

crf = get_crf()

params_space = {
    'c1': scipy.stats.expon(scale=0.5),
    'c2': scipy.stats.expon(scale=0.05),
}

# use the same metric for evaluation
f1_scorer = make_scorer(metrics.flat_f1_score,
                        average='weighted', labels=labels)

# search
rs = RandomizedSearchCV(crf, params_space,
                        cv=3,
                        verbose=1,
                        n_jobs=-1,
                        n_iter=50,
                        scoring=f1_scorer)
rs.fit(X_train, y_train)
# save_pickle(rs, "crf_randomized_search_cv_t_1")
rs = get_model("crf_randomized_search_cv_t_1")
# crf = rs.best_estimator_
print('best params:', rs.best_params_)
print('best CV score:', rs.best_score_)
print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))

# Check parameter space
_x = [s.parameters['c1'] for s in rs.grid_scores_]
_y = [s.parameters['c2'] for s in rs.grid_scores_]
_c = [s.mean_validation_score for s in rs.grid_scores_]

import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig = plt.figure()
fig.set_size_inches(12, 12)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('C1')
ax.set_ylabel('C2')
ax.set_title("Randomized Hyperparameter Search CV Results (min={:0.3}, max={:0.3})".format(
    min(_c), max(_c)
))

ax.scatter(_x, _y, c=_c, s=60, alpha=0.9, edgecolors=[0, 0, 0])

print("Dark blue => {:0.4}, dark red => {:0.4}".format(min(_c), max(_c)))