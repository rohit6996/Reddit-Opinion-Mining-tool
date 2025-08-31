# run_search.py
from app.reddit_client import search_posts

if __name__ == "__main__":
    print("🔍 Searching Reddit for: 'Is AI dangerous?' in r/technology & r/machinelearning\n")
    results = list(search_posts("Is AI dangerous?", subreddits=["technology", "machinelearning"], limit=3))

    for i, post in enumerate(results, 1):
        print(f"[{i}] {post['title']} (r/{post['subreddit']})")
        print(f"    Score: {post['score']} | Comments: {post['num_comments']}")
        print(f"    Link: {post['permalink']}\n")
