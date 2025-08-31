# test_classifier.py
from app.classifier import classify_comment

examples = [
    "Yes, AI will definitely destroy us.",
    "No, AI is just a tool, stop worrying.",
    "Not sure about AI, depends on regulations.",
    "AI will steal my girlfriend 😂",
]

for text in examples:
    print(f"{text}  --->  {classify_comment(text)}")
