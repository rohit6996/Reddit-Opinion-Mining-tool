# from collections import defaultdict
# from app.classifier import classify_comment   # ✅ fixed import
# from app.preprocessing import preprocess_text

# def analyze_and_classify(comments):
#     """
#     Takes a list of comments, preprocesses them, classifies each,
#     and returns a list of results.
#     """
#     results = []

#     for comment in comments:
#         clean_text = preprocess_text(comment)
#         label = classify_comment(clean_text)
#         results.append({
#             "original": comment,
#             "cleaned": clean_text,
#             "label": label
#         })

#     return results

from collections import defaultdict
from app.classifier import classify_comment   # ✅ fixed import
from app.preprocessing import preprocess_text



def analyze_and_classify(comments):
    """
    Analyze a list of Reddit comments and classify them into categories.
    Returns a dictionary summary with counts for each category.
    """

    # Categories we care about
    categories = ["Agree", "Neutral", "Not Agree", "Joke/Off-topic"]
    summary = defaultdict(int)

    # Classify each comment
    for comment in comments:
        label = classify_comment(comment)

        # Normalize label
        if label.lower() in ["agree", "yes", "support"]:
            summary["Agree"] += 1
        elif label.lower() in ["neutral", "mixed", "undecided"]:
            summary["Neutral"] += 1
        elif label.lower() in ["not_agree", "disagree", "no"]:
            summary["Not Agree"] += 1
        else:
            summary["Joke/Off-topic"] += 1

    # Ensure all categories exist (even if 0 count)
    for cat in categories:
        summary[cat] = summary.get(cat, 0)

    return dict(summary)
