"""
Common patterns across the project.
"""

import re

def clean_text(text: str) -> list[str]:
    words = re.findall("[a-zA-Z]+", text.lower())
    words = filter(lambda s: len(s) > 2, words)  # words with two or less characters won't really do much
    return list(words)