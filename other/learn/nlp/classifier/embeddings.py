import gensim
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class Embeddings:
    def __init__(self, vector_size=100, window=5, min_count=2):
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.w2v_model = None
        self.d2v_model = None
        self.tfidf_model = None

    def word2vec(self, x_value):
        self.w2v_model = gensim.models.Word2Vec(x_value, vector_size=self.vector_size, window=self.window,
                                                min_count=self.min_count)

    @staticmethod
    def doc2vec_tagging(x_value):
        d2v_tagging = [gensim.models.doc2vec.TaggedDocument(v, [i]) for i, v in enumerate(x_value)]

        return d2v_tagging

    def doc2vec(self, tagged_docs):
        self.d2v_model = gensim.models.Doc2Vec(tagged_docs, vector_size=self.vector_size, window=self.window,
                                               min_count=self.min_count)

    def get_word2vec(self, x_value):
        words = set(self.w2v_model.wv.index_to_key)
        x_value_vector = np.array([np.array([self.w2v_model.wv[i] for i in ls if i in words]) for ls in x_value])

        return x_value_vector

    def get_doc2vec(self, tagged_docs):
        d2v_vector = [self.d2v_model.infer_vector(v.words) for v in tagged_docs]

        return d2v_vector

    def average_word2vec(self, x_value):
        x_value_vector = self.get_word2vec(x_value)
        X_train_vect_avg = []

        for v in x_value_vector:
            if v.size:
                X_train_vect_avg.append(v.mean(axis=0))
            else:
                X_train_vect_avg.append(np.zeros(100, dtype=float))

        return X_train_vect_avg

    def tfidf(self, x_value):
        self.tfidf_model = TfidfVectorizer()
        self.tfidf_model.fit(x_value.apply(lambda x: ' '.join(x)))

    def get_tfidf_vec(self, x_value):
        tfidf_vec = self.tfidf_model.transform(x_value.apply(lambda x: ' '.join(x)))

        return tfidf_vec

    def get_all_embeddings(self, X_train, X_test):
        embeddings = dict()
        self.tfidf(X_train)
        train_vectors = self.get_tfidf_vec(X_train)
        test_vectors = self.get_tfidf_vec(X_test)
        embeddings['tfidf'] = [train_vectors, test_vectors]

        tagged_docs_train = self.doc2vec_tagging(X_train)
        tagged_docs_test = self.doc2vec_tagging(X_test)
        self.doc2vec(tagged_docs_train)

        train_vectors = self.get_doc2vec(tagged_docs_train)
        test_vectors = self.get_doc2vec(tagged_docs_test)
        embeddings['doc2vec'] = [train_vectors, test_vectors]

        self.word2vec(X_train)

        x_train_vector_avg = self.average_word2vec(X_train)
        x_test_vector_avg = self.average_word2vec(X_test)
        embeddings['word2vec'] = (x_train_vector_avg, x_test_vector_avg)

        return embeddings
