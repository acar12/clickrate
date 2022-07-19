"""
Test the model to see if it actually works.
"""

from model import ClickbaitClassifier
import pandas as pd
import unittest
from typing import Iterable
from commons import get_headlines

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = ClickbaitClassifier()

    def get_accuracy(self, iterable: Iterable[tuple[str, int]]) -> float:
        avg_accuracy = 0
        num_rows = 0

        for word, val in iterable:
            guess = round(self.model.predict_clickbait(word))
            if guess == val:
                avg_accuracy += 1
            num_rows += 1
        
        avg_accuracy /= num_rows
        return avg_accuracy

    def test_model_csv(self):
        df = pd.read_csv("data/test_headlines.csv")
        accuracy = self.get_accuracy((row for _, row in df.iterrows()))
        self.assertGreaterEqual(accuracy, 0.8)
        print(f"{int(accuracy * 100)}%")

    def test_model_list(self):
        # a few headlines gathered from buzzfeed and reuters to test modern media
        accuracy = self.get_accuracy(get_headlines())
        self.assertGreaterEqual(accuracy, 0.8)
        print(f"{int(accuracy * 100)}%")

if __name__ == "__main__":
    unittest.main()
