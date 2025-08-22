
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
    MIN_LENGTH = 100  

    def run(self, state: OverallState) -> OverallState:
        content = state.get("content", "")

        if content and len(content.strip()) >= self.MIN_LENGTH:
            state["is_valid"] = True
            logger.info(f"[ValidatorNode] Content is valid (length: {len(content.strip())} chars).")
        else:
            state["is_valid"] = False
            logger.info(f"[ValidatorNode] Content is NOT valid. (length: {len(content.strip())} chars).")

        return state
    
