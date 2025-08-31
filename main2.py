from app.fetch_reddit import fetch_post_and_comments
from app.analyze_comments import analyze_and_classify
from app.visualize_results import plot_results

def run_pipeline(question):
    print(f"\n🔍 Fetching Reddit comments for: {question}")
    comments = fetch_post_and_comments(question, limit=500)

    print("\n⚙️ Analyzing comments...")
    summary = analyze_and_classify(comments)

    print("\n📊 Plotting results...")
    plot_results(summary)

if __name__ == "__main__":
    # Take input from user
    question = input("Enter your Reddit poll question: ")
    run_pipeline(question)
