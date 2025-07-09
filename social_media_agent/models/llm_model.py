import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class LLMModel:
    @staticmethod
    def llm_chat(prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 100, temperature: float = 0.7) -> str:
        """
        Sends a prompt to OpenAI chat model and returns the response text.
        """
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
