# src/core/batching.py

import asyncio

class BatchManager:
    def __init__(self):
        self.queue = []
        self.batch_size = 8
        self.lock = asyncio.Lock()

    async def add_request(self, request):
        async with self.lock:
            self.queue.append(request)
            if len(self.queue) >= self.batch_size:
                return await self.process_batch()

    async def process_batch(self):
        batch = self.queue[:]
        self.queue = []
        # Custom batching logic for vLLM or OpenAI
        # (Can add token batching, sequence batching)
        return {"batch_size": len(batch), "responses": "batched_result"}
