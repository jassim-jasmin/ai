from sklearn.feature_extraction.text import TfidfVectorizer


class BinaryTermFrequency:
    @staticmethod
    def parameter():
        return {
            'binary': True,
            'norm': False,
            'use_idf': False,
            'smooth_idf': False,
            'lowercase': True,
            'stop_words': 'english',
            'min_df': 1,
            'max_df': 1.0,
            'max_features': None,
            'ngram_range': (1, 1)
        }

    @classmethod
    def get(cls, parameter: dict = None):
        if not parameter:
            parameter = cls.parameter()

        vectoriser = TfidfVectorizer(**parameter)

        return vectoriser

if __name__ == "__main__":
    corpus = ["This is a brown house. This house is big. The street number is 1.",
          "This is a small house. This house has 1 bedroom. The street number is 12.",
          "This dog is brown. This dog likes to play.",
          "The dog is in the bedroom."]

    vectorizer = BinaryTermFrequency.get()
    vectorised_fit_data = vectorizer.fit_transform(corpus)
    print("vector data", vectorised_fit_data)
