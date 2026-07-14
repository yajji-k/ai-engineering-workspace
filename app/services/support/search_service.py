# app/services/search_service.py
from tavily import TavilyClient
from app.core.config import get_settings

settings = get_settings()

class SearchService:
    def __init__(self):
        self.client = TavilyClient(api_key=settings.tavily_api_key)

    def search(self, query: str, max_results: int = 5):
        return self.client.search(
            query=query,
            max_results=max_results,
            topic="general"   # or "news"
        )