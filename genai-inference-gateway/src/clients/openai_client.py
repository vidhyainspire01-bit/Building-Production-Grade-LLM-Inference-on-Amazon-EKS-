# src/clients/openai_client.py

from openai import AsyncOpenAI
from src.schemas.llm_request import LLMRequest
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIClient:
    async def generate(self, req: LLMRequest):
        completion = await client.chat.completions.create(
            model=req.model,
            messages=[{"role": "user", "content": req.prompt}],
            max_tokens=req.max_tokens,
            temperature=req.temperature,
        )
        return completion.choices[0].message
