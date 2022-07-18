from model import predict_clickbait
import pandas as pd
import unittest
from typing import Iterable

class TestModel(unittest.TestCase):
    def get_accuracy(self, iterable: Iterable[tuple[str, int]]) -> float:
        avg_accuracy = 0
        num_rows = 0

        for word, val in iterable:
            guess = round(predict_clickbait(word))
            if guess == val:
                avg_accuracy += 1
            num_rows += 1
        
        avg_accuracy /= num_rows
        return avg_accuracy

    def test_model_csv(self):
        df = pd.read_csv("data/test_headlines.csv")
        accuracy = self.get_accuracy((row for _, row in df.iterrows()))
        self.assertGreaterEqual(accuracy, 0.8)

    def test_model_list(self):
        # a few headlines gathered from buzzfeed and reuters (7/17/2022)
        # this is to see if it works with modern forms of clickbait
        accuracy = self.get_accuracy((
            ("This Sorting Quiz Will Tell You Which Hogwarts House You Truly Belong In", 1),
            ("Find Out Which Deadly Sin Best Describes Your Cold, Dark Heart", 1),
            ("Everyone Has A Disney Villain Alter Ego — Here's Yours", 1),
            ("'Climate change affects everyone': Europe battles wildfires in intense heat", 0),
            ("Ukraine's president fires security service chief and prosecutor general", 0),
            ("Sudan protesters decry violence in southern state", 0)
        ))
        self.assertGreaterEqual(accuracy, 0.8)

if __name__ == "__main__":
    unittest.main()
