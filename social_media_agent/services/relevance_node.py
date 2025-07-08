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
    
# if __name__ == '__main__':
#     newclas = RelevanceNode()
#     state = {"content": " caliber shoes and also the shoes are made in nepal which is of very good quality, loved by people and everbody wears it like evryday."
#     "It it very good for everyday use. I love the shoes. What is your take on it don't forget to rate it and use it ofcourse", "query": "dress"}
#     result = newclas.run(state)