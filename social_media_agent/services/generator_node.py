import os
import openai
from openai import OpenAI   
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)


client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class GeneratorNode(BaseNode):
    """
    Generates social media post using OpenAI's GPT after relevance is true.
    """
    def run(self, state: OverallState) -> OverallState:
        if not state.get("is_relevant", False):
            print("[GeneratorNode] Content is not relevant. Skipping generation.")
            return state

        prompt = f"""You are a helpful social media assistant. Based on the following content, generate a concise and engaging social media post:

Content:
{state['content']}

Post:"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.7,
            )
            post = response.choices[0].message.content.strip()
            state["post"] = post
            logger.info("[GeneratorNode] Post generated.")
        except Exception as e:
            logger.info(f"[GeneratorNode] Failed to generate post: {e}")
            state["post"] = ""

        return state
if __name__ == '__main__':
    clas = GeneratorNode()
    state = {"content": "This is a relevant content about the caliber shoes and also the shoes are made in nepal which is of very good quality, loved by people and everbody wears it like evryday. It it very good for everyday use. I love the shoes. What is your take on it don't forget to rate it and use it ofcourse",
             "is_relevant": True}
    result = clas.run(state)
    logger.info(f"Generated Post: {result['post']}")
