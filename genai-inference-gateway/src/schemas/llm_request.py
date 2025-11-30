# src/schemas/llm_request.py

from pydantic import BaseModel

class LLMRequest(BaseModel):
    model: str
    prompt: str
    max_tokens: int = 512
    temperature: float = 0.2
    stream: bool = False
