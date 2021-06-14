from matplotlib import pyplot as plt
from pandas import DataFrame
from pandas.plotting import scatter_matrix
import numpy as np

from data.preprocessing.text.vectorization.binary_term_frequency.binary_term_frequency import BinaryTermFrequency


class Visualize:
    @staticmethod
    def apply(data: list):
        vectorizer = BinaryTermFrequency.get()
        vectorised_fit_data = vectorizer.fit_transform(data)

        df = DataFrame(vectorised_fit_data.toarray(), columns=vectorizer.get_feature_names())
        axarr = df.hist(bins=2)

        for ax in axarr.flatten():
            ax.set_xlabel("Feature presence")
            ax.set_ylabel("Presence count")

        plt.show()

        return plt

if __name__ == "__main__":
    corpus = ["This is a brown house. This house is big. The street number is 1.",
          "This is a small house. This house has 1 bedroom. The street number is 12.",
          "This dog is brown. This dog likes to play.",
          "The dog is in the bedroom.",
              "this is another string by house",
              "My dog ran away",
              "My house was empty",
              "I'm jassim jasmin",
              "My brother is jishal",
              "india", "japan", "arabia", "kerala", "nothing"]

    Visualize.apply(corpus)
