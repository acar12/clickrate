"""
Test the model to see if it actually works.
"""
import os, sys
sys.path.append(os.path.dirname(__file__))

import pandas as pd
import unittest
from typing import Iterable
from model import ClickbaitClassifier
from commons import get_headlines, get_path, print_confusion_matrix

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = ClickbaitClassifier()

    def get_accuracy(self, iterable: Iterable[tuple[str, int]]) -> list[int]:
        confusion_matrix = [0, 0, 0, 0] # true positive, true negative, false positive, false negative

        for word, val in iterable:
            guess = round(self.model.predict_clickbait(word))
            if guess == val:
                if val == 0:
                    confusion_matrix[1] += 1
                elif val == 1:
                    confusion_matrix[0] += 1
            else:
                if val == 0:
                    confusion_matrix[2] += 1
                elif val == 1:
                    confusion_matrix[3] += 1
        
        return confusion_matrix

    def test_model_csv(self):
        df = pd.read_csv(get_path("data/test_headlines.csv"))
        confusion_matrix = self.get_accuracy((row for _, row in df.iterrows()))
        accuracy = print_confusion_matrix(confusion_matrix)
        self.assertGreaterEqual(accuracy, 85)

    def test_model_list(self):
        # a few headlines gathered from buzzfeed and reuters to test modern media
        confusion_matrix = self.get_accuracy(get_headlines())
        accuracy = print_confusion_matrix(confusion_matrix)
        self.assertGreaterEqual(accuracy, 85)

if __name__ == "__main__":
    unittest.main()
