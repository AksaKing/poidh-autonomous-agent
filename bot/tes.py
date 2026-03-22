import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET")
)

try:
    client.create_tweet(text="Bot is online! Ready to verify poidh bounties. 🤖🚀")
    print("✅ Berhasil nge-tweet! Kunci lu udah sakti.")
except Exception as e:
    print(f"❌ Error: {e}")