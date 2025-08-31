# app/classifier.py
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import re

# Make sure VADER is downloaded once
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def classify_comment(text: str) -> str:
    if not text or len(text.strip()) == 0:
        return "🤔 Neutral"

    text_lower = text.lower()

    # Rule: detect jokes
    if re.search(r"(lol|haha|😂|lmao|rofl)", text_lower):
        return "😂 Joke/Off-topic"

    # Rule: explicit agreement/disagreement keywords
    if re.search(r"\b(yes|agree|absolutely|definitely|of course|sure)\b", text_lower):
        return "✅ Agree"
    if re.search(r"\b(no|not at all|disagree|never|nah)\b", text_lower):
        return "❌ Not Agree"

    # Sentiment-based fallback
    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.3:
        return "✅ Agree"
    elif compound <= -0.3:
        return "❌ Not Agree"
    else:
        return "🤔 Neutral"

