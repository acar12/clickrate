"""
Gets all the words and their frequencies and groups
by if it's clickbait or not from 'headlines.csv'.
"""

import pandas as pd
from collections import Counter
from clickrate.commons import clean_text, get_path

def read_and_write(read_file: str, write_file: str) -> None:
    df: pd.DataFrame = pd.read_csv(read_file)

    fake_counter: Counter = Counter() # clickbait
    real_counter: Counter = Counter() # non-clickbait

    for _, row in df.iterrows():
        if row[1] == 1:
            counter = fake_counter
        else:
            counter = real_counter
        counter.update(clean_text(row[0]))

    freq = [(True, word, fake_counter[word] / fake_counter.total()) for word in fake_counter] + \
        [(False, word, real_counter[word] / real_counter.total()) for word in real_counter]
    df: pd.DataFrame = pd.DataFrame(freq)
    df.columns = ("clickbait", "word", "frequency")
    df.to_csv(write_file, index=False)

if __name__ == "__main__":
    read_and_write(get_path("data/headlines.csv"), get_path("data/words.csv"))
