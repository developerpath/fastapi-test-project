import httpx
from typing import List, Any
from pydantic import AnyHttpUrl
import asyncio

class HttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def get(self, url: AnyHttpUrl) -> dict:
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            return {"error": str(err)}

    async def make_requests(self, urls: List[AnyHttpUrl]) -> List[dict]:
        tasks = [self.get(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

    async def close(self):
        await self.client.aclose()
