"""
The Naive Bayes classifier to work out if a title may
be clickbait or not.
"""

import pandas as pd
from math import log, exp
from clickrate.commons import clean_text, get_path


class ClickbaitClassifier:
    def __init__(self):
        self.df = pd.read_csv(get_path("data/words.csv"))
        self.df_cache = {} # caching turned 47 seconds of testing into 17 seconds
    
    def get_percent_of_word(self, clickbait: bool, word: str) -> float:
        if (clickbait, word) in self.df_cache:
            return self.df_cache[clickbait, word]
        else:
            sub_df = self.df[(self.df["clickbait"] == clickbait) & (self.df["word"] == word)]
            try:
                freq = sub_df.iloc[0]["frequency"]
                self.df_cache[clickbait, word] = freq
                return freq
            except IndexError:
                self.df_cache[clickbait, word] = -1
                return -1
    
    def predict_clickbait(self, text: str) -> float:
        text = clean_text(text)
        # logarithms are used as multiplying since
        # many small floats will give inaccurate values
        log_true = 0
        log_false = 0

        for word in text:
            prob_true = self.get_percent_of_word(True, word)
            prob_false = self.get_percent_of_word(False, word)

            if prob_true > -1 and prob_false > -1:
                log_true += log(prob_true)
                log_false += log(prob_false)

        prob_true = exp(log_true)
        prob_false = exp(log_false)
        # for dataset ratio of clickbait to non clickbait is practically 50/50
        # so the equation is simplified
        return prob_true / (prob_true + prob_false)