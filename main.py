from app.fetch_reddit import fetch_post_and_comments
from app.analyze_comments import analyze_and_classify
from app.visualize_results import plot_results

def run_pipeline(question):
    # 1. Fetch Reddit post + comments
    post_data = fetch_post_and_comments(question, subreddit="technology", limit=1)

    print("\n🔎 Analyzing Post:")
    print("Title:", post_data["title"])
    print("URL:", post_data["url"])
    print("Score:", post_data["score"])
    print("Comments:", post_data["num_comments"])

    # 2. Analyze + classify all comments in one step
    analysis_results = analyze_and_classify(post_data["comments"])

    # 3. Summarize results
    summary = {}
    for item in analysis_results:
        summary[item["label"]] = summary.get(item["label"], 0) + 1

    print("\n📊 Analysis Summary:")
    for label, count in summary.items():
        print(f"{label}: {count}")

    # 4. Visualize results
    plot_results(summary)

    # 5. Show some sample comments per category
    samples = {cat: [] for cat in summary.keys()}
    for item in analysis_results:
        if len(samples[item["label"]]) < 2:  # keep 2 examples
            samples[item["label"]].append(item["original"])

    print("\n💬 Sample Comments:")
    for cat, texts in samples.items():
        print(f"\n{cat}:")
        for t in texts:
            print(" -", t[:120])  # first 120 chars

if __name__ == "__main__":
    run_pipeline("Is AI dangerous?")
