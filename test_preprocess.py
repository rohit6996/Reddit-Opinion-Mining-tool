# test_preprocess.py
from app.preprocessing import clean_text

if __name__ == "__main__":
    raw = "AI will destroy us all!!! 😂😂 Check: https://example.com"
    print("Raw:", raw)
    print("Cleaned:", clean_text(raw))
