import praw

# 🔑 Fill in your credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT"
)

def fetch_post_and_comments(query, subreddit="technology", limit=1):
    """Search Reddit posts and fetch comments"""
    posts = reddit.subreddit("all").search(query, limit=1)
    
    for post in posts:
        print("🔎 Selected Post:")
        print("Title:", post.title)
        print("URL:", post.url)
        print("Score:", post.score)
        print("Comments:", post.num_comments)
        print("Link:", f"https://reddit.com{post.permalink}")
        
        # Fetch comments
        post.comments.replace_more(limit=0)  # flatten threads
        comments = [c.body for c in post.comments.list()]
        
        return {
            "title": post.title,
            "url": f"https://reddit.com{post.permalink}",
            "score": post.score,
            "num_comments": post.num_comments,
            "comments": comments
        }

if __name__ == "__main__":
    data = fetch_post_and_comments("Is AI dangerous?")
    print("\nFetched", len(data["comments"]), "comments")
    print("Sample Comment:", data["comments"][0] if data["comments"] else "No comments")
