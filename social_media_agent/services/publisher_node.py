import os
import tweepy
from dotenv import load_dotenv
from social_media_agent.basemodel import BaseNode, OverallState

class PublisherNode(BaseNode):
    """
    Publishes the post to Twitter using Tweepy.
    """
    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_KEY_SECRETS"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_TOKEN_SECRETS")
        )

    def run(self, state: OverallState) -> OverallState:
        try:
            response = self.client.create_tweet(text=state["post"])
            print("Tweet posted successfully. Tweet ID:", response.data.get("id"))
            state["posted"] = True
        except Exception as e:
            print("Failed to post tweet:", str(e))
            state["posted"] = False
        return state
