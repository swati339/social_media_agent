from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

class ReviewerNode(BaseNode):
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: OverallState) -> OverallState:
        post = state.get("post", "").strip()
        
        if not post:
            print("[ReviewerNode] Error: No generated post available to review.")
            state["approved"] = "reject"  
            return state
        
        print("\n[ReviewerNode] Generated Post:\n")
        print(f"🔹 {post}\n")

        while True:
            decision = input("Approve, Edit, or Reject? [a/e/r]: ").strip().lower()
            if decision == "a":
                state["approved"] = "accept"
                print("[ReviewerNode] Post approved.")
                break
            elif decision == "e":
                # Your editing logic here (manual or llm)
                ...
            elif decision == "r":
                state["approved"] = "reject"
                print("[ReviewerNode] Post rejected.")
                break
            else:
                print("Invalid input. Please enter 'a', 'e', or 'r'.")

        return state
