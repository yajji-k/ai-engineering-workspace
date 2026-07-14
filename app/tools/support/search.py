# app/tools/tavily/search.py
from langchain_core.tools import tool
from app.services.support.search_service import SearchService

search_service = SearchService()

@tool
def tavily_web_search(query: str) -> dict:
    """Search the web using Tavily for up-to-date information."""
    return search_service.search(query)