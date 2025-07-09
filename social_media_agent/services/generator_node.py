import logging
import asyncio
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.experiments.test_llm import OpenAIAsync
from social_media_agent.configs.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

llm = OpenAIAsync()

MAX_CHARS = 12000  

def truncate_input(text: str, max_chars: int = MAX_CHARS) -> str:
    """
    Truncate input text to avoid exceeding LLaMA context length.
    """
    return text[:max_chars] + "..." if len(text) > max_chars else text


class GeneratorNode(BaseNode):
    """
    Generates a social media post using your local LLM server.
    """

    async def run(self, state: OverallState) -> OverallState:
        if not state.get("is_relevant", False):
            print("[GeneratorNode] Content is not relevant. Skipping generation.")
            return state

        truncated_content = truncate_input(state["content"])

        prompt = (
            "You are a helpful social media assistant. "
            "Based on the following content, generate a concise and engaging social media post:\n\n"
            f"Content:\n{truncated_content}\n\nPost:"
        )

        messages = [{"role": "user", "content": prompt}]

        try:
            response = await llm.chat_completion(messages)
            state["post"] = response.choices[0].message.content.strip()
            logger.info("[GeneratorNode] Post generated.")
        except Exception as e:
            logger.exception(f"[GeneratorNode] Failed to generate post: {e}")
            state["post"] = ""

        return state



