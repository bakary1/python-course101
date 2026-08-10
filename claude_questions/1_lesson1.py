# 1. Problem 1 — Functions & string manipulation

# Write a function word_frequency(text) that takes a string of text and returns a
# dictionary mapping each word (lowercase, punctuation stripped) to how many times it appears.

from collections import Counter
import re


def word_frequency(sentence: str):
    clean_string = re.sub(r"[^\w\s]", "", sentence).strip().lower()
    word_list = clean_string.split()
    word_count = Counter(word_list)
    return dict(word_count)


word_frequency("The cat sat on the mat. The cat was happy.")
