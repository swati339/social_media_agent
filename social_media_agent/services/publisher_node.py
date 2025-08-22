import os
import tweepy
from dotenv import load_dotenv
from social_media_agent.basemodel import BaseNode, OverallState

class PublisherNode(BaseNode):
    """
    Publishes the post to Twitter using Tweepy with OAuth 2.0 user context.
    """
    def __init__(self):
        load_dotenv()

        self.client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_KEY_SECRETS"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_TOKEN_SECRETS")
        )

    def run(self, state: OverallState) -> OverallState:
        try:
            response = self.client.create_tweet(text=state["post"])

            tweet_id = response.data.get("id")
            print(f"Tweet posted successfully. Tweet ID: {tweet_id}")
            state["posted"] = True
            state["tweet_id"] = tweet_id
        except Exception as e:
            print(f"Failed to post tweet: {e}")
            state["posted"] = False
        return state
