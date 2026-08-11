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

# Problem 2 — List comprehensions & filtering

people = [
    {"name": "Alice", "age": 30, "city": "Helsinki"},
    {"name": "Bob", "age": 17, "city": "Turku"},
    {"name": "Charlie", "age": 25, "city": "Helsinki"},
    {"name": "Dana", "age": 15, "city": "Oulu"},
]

filtered_people = [
    person["name"]
    for person in people
    if person["age"] >= 18 and person["city"].strip().lower() == "helsinki"
]

# Problem 3 — Functions with default args & error handling


def safe_divide(a, b, Default=None):
    try:
        return a / b
    except ZeroDivisionError:
        return Default


safe_divide(10, 0)
