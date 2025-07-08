
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)

class ValidatorNode(BaseNode):
    """
    Validates the scraped content.
    Marks content as valid if it's not empty and sufficiently informative.
    """
    MIN_LENGTH = 100  # minimum character count for valid content

    def run(self, state: OverallState) -> OverallState:
        content = state.get("content", "")

        # Check for basic validity
        if content and len(content.strip()) >= self.MIN_LENGTH:
            state["is_valid"] = True
            logger.info(f"[ValidatorNode] Content is valid (length: {len(content.strip())} chars).")
        else:
            state["is_valid"] = False
            logger.info(f"[ValidatorNode] Content is NOT valid. (length: {len(content.strip())} chars).")

        return state
    
# if __name__ == '__main__':
#     clas = ValidatorNode()
#     state = {"content": "This is a valid content about the caliber shoes and also the shoes are made in nepal which is of very good quality, loved by people and everbody wears it like evryday."
#     "It it very good for everyday use. I love the shoes. What is your take on it don't forget to rate it and use it ofcourse"}
#     result = clas.run(state)