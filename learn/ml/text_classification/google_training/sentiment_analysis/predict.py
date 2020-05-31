import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Vectorization parameters

# Range (inclusive) of n-gram sizes for tokenizing text.
NGRAM_RANGE = (1, 2)

# Limit on the number of features. We use the top 20K features.
TOP_K = 20000

# Whether text should be split into word or character n-grams.
# One of 'word', 'char'.
TOKEN_MODE = 'word'

# Minimum document/corpus frequency below which a token will be discarded.
MIN_DOCUMENT_FREQUENCY = 2

# Limit on the length of text sequences. Sequences longer than this
# will be truncated.
MAX_SEQUENCE_LENGTH = 500

def get_vectorizer():
    kwargs = {
        'ngram_range': NGRAM_RANGE,  # Use 1-grams + 2-grams.
        'dtype': 'int32',
        'strip_accents': 'unicode',
        'decode_error': 'replace',
        'analyzer': TOKEN_MODE,  # Split text into word tokens.
        'min_df': MIN_DOCUMENT_FREQUENCY,
    }
    return TfidfVectorizer(**kwargs)

def save_model(train_texts, train_labels):
    """Vectorizes texts as ngram vectors.
    1 text = 1 tf-idf vector the length of vocabulary of uni-grams + bi-grams.
    # Arguments
        train_texts: list, training text strings.
        train_labels: np.ndarray, training labels.
        val_texts: list, validation text strings.
    # Returns
        x_train, x_val: vectorized training and validation texts
    """
    # Create keyword arguments to pass to the 'tf-idf' vectorizer.

    vectorizer = get_vectorizer()
    # Learn vocabulary from training texts and vectorize training texts.
    x_train = vectorizer.fit_transform(train_texts)
    pickle.dump(vectorizer, open('vector.pkl', 'wb'))

    # Select top 'k' of the vectorized features.
    selector = SelectKBest(f_classif, k=min(TOP_K, x_train.shape[1]))
    selector.fit(x_train, train_labels)

    pickle.dump(selector, open('feature.pkl', 'wb'))

    return selector


def predict(val_texts):
    # vectorizer = get_vectorizer()
    vectorizer = pickle.load(open('C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\learn\ml\\text_classification\\google_training\\sentiment_analysis\\vector.pkl', 'rb'))
    x_val = vectorizer.transform(val_texts)
    selector = pickle.load(open('C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\learn\ml\\text_classification\\google_training\\sentiment_analysis\\feature.pkl', 'rb'))

    x_val = selector.transform(x_val)
    x_val = x_val.astype('float32')

    return x_val

prediction_list = ["A =2 mg IN Naloxone (one 0.1 mL spray of the 20 mg/mL formulation in one nostril)", "one blah dddf odfjoi", "lkjf", "Naloxone", "one", "hello",
                   "D=1 mg IN Naloxone (two 2.1 mL spray of the 11 mg/mL formulation in two nostril)",
                   "D=1 mg IN Naloxone (two 10.2 mL spray of the 44 mg/mL formulation in two nostril)", "two", "hajlksdjklfkl"]
x_val = predict(prediction_list)

import tensorflow as tf
model = tf.keras.models.load_model("IMDb_mlp_model.h5")

p = model.predict(x_val)
# print("prediction::::", p, model.metrics_names)

from sklearn.preprocessing import MinMaxScaler, StandardScaler
# Normalizing Example  (mean 0, std 1)
norm = StandardScaler()
normalized = norm.fit_transform(p)
normalized_orig = norm.inverse_transform(normalized)

# print(normalized)
for each in zip(normalized.ravel(), prediction_list):
    # print(each)
    if each[0] > 0:
        print("nalaxone", each[1])

    else:
        print("other", each[1])
