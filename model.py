"""
The Naive Bayes classifier to work out if a title may
be clickbait or not.
"""

import re
import pandas as pd
from typing import List
from math import log, exp

df = pd.read_csv("data/words.csv")


def get_percent_of_word(clickbait: bool, word: str) -> float:
    sub_df = df[(df["clickbait"] == clickbait) & (df["word"] == word)]
    try:
        return sub_df.iloc[0]["frequency"]
    except IndexError:
        return -1


def clean_text(text: str) -> List[str]:
    words = re.findall("[a-zA-Z]+", text.lower())
    words = filter(lambda s: len(s) > 2, words)  # words with two or less characters won't really do much
    return list(words)


def predict_clickbait(text: str) -> float:
    text = clean_text(text)
    # logarithms are used as multiplying since
    # many small floats will give inaccurate values
    log_true = 0
    log_false = 0

    for word in text:
        prob_true = get_percent_of_word(True, word)
        prob_false = get_percent_of_word(False, word)

        if prob_true > -1 and prob_false > -1:
            log_true += log(prob_true)
            log_false += log(prob_false)

    prob_true = exp(log_true)
    prob_false = exp(log_false)
    # for dataset ratio of clickbait to non clickbait is practically 50/50
    # so the equation is simplified
    return prob_true / (prob_true + prob_false)
