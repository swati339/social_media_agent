from social_media_agent.basemodel import BaseNode, OverallState

class ReviewerNode(BaseNode):
    """
    Human-in-the-loop: Reviews generated content and decides whether to approve, edit, or reject it.
    """
    def run(self, state: OverallState) -> OverallState:
        print("\n[ReviewerNode] Generated Post:\n")
        print(f"🔹 {state['post']}\n")

        while True:
            decision = input("Approve, Edit, or Reject? [a/e/r]: ").strip().lower()
            if decision == "a":
                state["approved"] = "accept"
                print("[ReviewerNode] Post approved.")
                break
            elif decision == "e":
                edited = input("Enter edited post: ").strip()
                state["post"] = edited
                state["approved"] = "edit"
                print("[ReviewerNode] Post edited and approved.")
                break
            elif decision == "r":
                state["approved"] = "reject"
                print("[ReviewerNode] Post rejected.")
                break
            else:
                print("Invalid input. Please enter 'a' (approve), 'e' (edit), or 'r' (reject).")

        return state

# if __name__ == '__main__':
#     newclass = ReviewerNode()
#     state = {
#         "post": "Discover the comfort and quality of Caliber shoes, proudly made in Nepal! 🇳🇵 Perfect for everyday wear, these shoes have captured the hearts of many. ❤️"
#     }
#     result = newclass.run(state)
#     print("\n[FINAL STATE]", result)