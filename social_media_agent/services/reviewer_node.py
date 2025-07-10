import logging
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class ReviewerNode(BaseNode):
    def __init__(self, llm):
        self.llm = llm

    async def run(self, state: OverallState) -> OverallState:
        original_post = state.get("post", "").strip()
        if not original_post:
            print("[ReviewerNode] Error: No generated post available to review.")
            state["approved"] = "reject"
            return state

        current_post = original_post  
        while True:
            print("\n[ReviewerNode] Current Post:\n")
            print(f"🔹 {current_post}\n")

            decision = input("Approve, Edit, or Reject? [a/e/r]: ").strip().lower()

            if decision == "a":
                if not current_post.strip():
                    print("[ReviewerNode] Cannot approve empty post.")
                    continue
                state["post"] = current_post  # save final post
                state["approved"] = "accept"
                print("[ReviewerNode] Post approved.")
                break

            elif decision == "e":
                edit_method = input("How would you like to edit?\n1. Manual edit\n2. Edit using LLM prompt\nChoose [1/2]: ").strip()

                if edit_method == "1":
                    edited_post = input("Enter the manually edited post:\n").strip()
                    if edited_post:
                        current_post = edited_post
                        print("[ReviewerNode] Post manually edited.")
                    else:
                        print("Edited post cannot be empty.")

                elif edit_method == "2":
                    instruction = input("Enter your instruction for the LLM (e.g. 'make it shorter'):\n").strip()

                    if not original_post:
                        print("[ReviewerNode] No original post to edit.")
                        continue

                    prompt = (
                        "You are a helpful assistant. "
                        "Regenerate the social media post with this instruction:\n\n"
                        f"Instruction: {instruction}\n\n"
                        f"Post:\n{original_post}\n\n"
                        "Edited Post:"
                    )

                    try:
                        revised_post = await self.llm.llm_chat(prompt)
                        if not revised_post.strip():
                            print("[ReviewerNode] LLM returned empty post, try again.")
                            continue
                        current_post = revised_post
                        print("[ReviewerNode] Post regenerated using LLM.")
                    except Exception as e:
                        logger.exception(f"[ReviewerNode] LLM edit failed: {e}")
                        print("LLM failed to regenerate the post. Try again or use manual edit.")
                        continue
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            elif decision == "r":
                state["approved"] = "reject"
                print("[ReviewerNode] Post rejected.")
                break

            else:
                print("Invalid input. Please enter 'a', 'e', or 'r'.")

        return state
