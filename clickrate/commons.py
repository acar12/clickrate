"""
Common patterns across the project.
"""

import os
import re
import requests
from bs4 import BeautifulSoup as Soup

def clean_text(text: str) -> list[str]:
    words = re.findall("[a-zA-Z]+", text.lower())
    words = filter(lambda s: len(s) > 2, words)  # words with two or less characters won't really do much
    return list(words)

def get_headlines():
    # buzzfeed
    content = requests.get("https://web.archive.org/web/20220721140241/https://www.buzzfeed.com/").content
    soup = Soup(content, "html.parser")
    for e in soup.find_all(class_="feedItem_title__0_9qB"):
        yield e.contents[0], 1
    # associated press
    content = requests.get("https://web.archive.org/web/20220722180934/https://apnews.com/hub/ap-top-news").content
    soup = Soup(content, "html.parser")
    for e in soup.find_all("h2"):
        yield e.contents[0], 0

def get_path(file_name: str) -> str:
    return str(os.path.join(os.path.dirname(__file__), file_name))

def print_confusion_matrix(matrix: list[int]) -> float:
    true_pos, true_neg, false_pos, false_neg = matrix
    false_pos_rate = false_pos / (true_pos + false_pos) * 100
    false_neg_rate = false_neg / (true_neg + false_neg) * 100
    accuracy = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg) * 100

    print(f"\nFalse positive rate: {false_pos_rate:.1f}%")
    print(f"False negative rate: {false_neg_rate:.1f}%")
    print(f"Accuracy: {accuracy:.1f}%")

    return accuracy
