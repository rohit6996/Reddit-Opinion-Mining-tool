# app/preprocessing.py
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """Clean comment text: remove URLs, punctuation, stopwords, etc."""
    if not text:
        return ""

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove emojis/special chars
    text = text.encode("ascii", "ignore").decode("utf-8")

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords & short words
    tokens = [w for w in tokens if w not in STOPWORDS and len(w) > 2]

    return " ".join(tokens)

import re

def preprocess_text(text):
    """
    Cleans the input text by:
    - Lowercasing
    - Removing special characters, links, and extra spaces
    """
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[^a-z\s]", "", text)  # remove non-alphabetic
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text
