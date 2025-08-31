# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "reddit-opinion-polls:v1 (by u/your_username)")

if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
    raise EnvironmentError("❌ Missing Reddit credentials in .env file!")
