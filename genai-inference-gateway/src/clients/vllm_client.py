# src/clients/vllm_client.py

import httpx
from src.schemas.llm_request import LLMRequest

class VLLMClient:
    async def generate(self, req: LLMRequest):
        payload = {
            "prompt": req.prompt,
            "max_tokens": req.max_tokens,
            "temperature": req.temperature
        }

        async with httpx.AsyncClient() as client:
            r = await client.post("http://vllm-service:8000/generate", json=payload)
            return r.json()
