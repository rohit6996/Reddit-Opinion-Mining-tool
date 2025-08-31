# test_reddit.py
import os
from dotenv import load_dotenv
import praw

load_dotenv()

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT", "reddit-opinion-polls:v1 (by u/your_username)")

def get_reddit():
    if not CLIENT_ID or not CLIENT_SECRET:
        raise SystemExit("Missing REDDIT_CLIENT_ID or REDDIT_CLIENT_SECRET in .env")
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        request_timeout=10
    )

def simple_search(query="Is AI dangerous?", subreddit="all", limit=3):
    reddit = get_reddit()
    print(f"Searching r/{subreddit} for: {query}")
    # for quick test we use subreddit.search; in main app we'll combine subreddits
    results = reddit.subreddit(subreddit).search(query, sort="relevance", limit=limit)
    for i, post in enumerate(results, 1):
        print(f"\n[{i}] Title: {post.title}")
        print(f"    Subreddit: {post.subreddit}")
        print(f"    Score: {post.score} • Comments: {post.num_comments}")
        print(f"    Permalink: https://reddit.com{post.permalink}")
        # print a short snippet of selftext
        snippet = (post.selftext or "")[:300].replace("\n", " ")
        if snippet:
            print("    Snippet:", snippet + ("..." if len(snippet) == 300 else ""))
        else:
            print("    (no selftext)")

if __name__ == "__main__":
    simple_search()
