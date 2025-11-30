# src/core/caching.py

import aioredis
import json

class Cache:
    def __init__(self):
        self.client = aioredis.from_url("redis://redis-service:6379")

    async def get(self, key):
        data = await self.client.get(key)
        return json.loads(data) if data else None

    async def set(self, key, value, ttl=3600):
        await self.client.set(key, json.dumps(value), ex=ttl)
