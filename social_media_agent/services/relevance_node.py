from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)

class RelevanceNode(BaseNode):
    """
    Relevance node that checks if the content is relevant to the query.
    """
    def run(self, state: OverallState) -> OverallState:
        content = state.get("content", "")
        query = state.get("query", "")

        if query.lower() in content.lower():
            state["is_relevant"] = True
            logger.info(f"[RelevanceNode] Content is relevant to the query.")
        else:
            state["is_relevant"] = False
            logger.info(f"[RelevanceNode] Content is NOT relevant to the query.")

        return state
    
