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
    content = requests.get("https://www.buzzfeed.com/").content
    soup = Soup(content, "html.parser")
    for e in soup.find_all(class_="feedItem_title__0_9qB"):
        yield e.contents[0], 1
    # associated press
    content = requests.get("https://apnews.com/").content
    soup = Soup(content, "html.parser")
    for e in soup.find_all(class_="headline-0-2-153"):
        yield e.contents[0], 0

def get_path(file_name: str) -> str:
    return str(os.path.join(os.path.dirname(__file__), file_name))
