# src/core/router.py

from src.clients.openai_client import OpenAIClient
from src.clients.vllm_client import VLLMClient
from src.core.caching import Cache
from src.core.batching import BatchManager
from src.core.model_selector import ModelSelector

class LLMRouter:
    def __init__(self):
        self.cache = Cache()
        self.batcher = BatchManager()
        self.selector = ModelSelector()
        self.openai_client = OpenAIClient()
        self.vllm_client = VLLMClient()

    async def dispatch(self, request):
        # -------- 1. Check Cache ----------
        cache_key = f"{request.model}:{request.prompt}"
        cached = await self.cache.get(cache_key)
        if cached:
            return {"cached": True, "response": cached}

        # -------- 2. Batching --------------
        batch_result = await self.batcher.add_request(request)
        if batch_result:
            return batch_result  # already processed

        # -------- 3. Select Provider -------
        provider = self.selector.choose(request.model)

        if provider == "openai":
            response = await self.openai_client.generate(request)
        else:
            response = await self.vllm_client.generate(request)

        # -------- 4. Cache Response --------
        await self.cache.set(cache_key, response, ttl=3600)

        return response
