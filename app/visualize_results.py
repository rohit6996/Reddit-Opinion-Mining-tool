import matplotlib.pyplot as plt
from app.analyze_comments import analyze_and_classify

import matplotlib.pyplot as plt

def plot_results(summary):
    """
    Takes a summary dictionary {label: count} and plots a pie chart.
    """
    labels = list(summary.keys())
    sizes = list(summary.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Reddit Opinion Poll Results")
    plt.show()


if __name__ == "__main__":
    comments = [
        "Yes, AI will definitely destroy us.",
        "No, AI is just a tool, stop worrying.",
        "Not sure about AI, depends on regulations.",
        "AI will steal my girlfriend 😂",
        "Absolutely agree, AI is risky!",
        "Nah, this is just hype."
    ]

    plot_results(comments)
