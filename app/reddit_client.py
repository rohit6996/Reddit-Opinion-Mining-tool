# app/reddit_client.py
import praw
from app import config

def get_reddit():
    """Create a Reddit instance using credentials from config."""
    return praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT,
        request_timeout=10
    )

def search_posts(query, subreddits=["all"], limit=10, sort="relevance"):
    """Search multiple subreddits for a query and yield posts."""
    reddit = get_reddit()
    for subreddit in subreddits:
        for post in reddit.subreddit(subreddit).search(query, sort=sort, limit=limit):
            yield {
                "id": post.id,
                "title": post.title,
                "subreddit": str(post.subreddit),
                "score": post.score,
                "num_comments": post.num_comments,
                "permalink": f"https://reddit.com{post.permalink}",
                "selftext": post.selftext or "",
            }
