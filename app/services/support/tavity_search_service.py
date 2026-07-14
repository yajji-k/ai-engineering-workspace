from langchain_core.tools import tool
from tavily import TavilyClient
from app.core.config import get_settings

settings = get_settings()

class TavitySearchService:
    
    @tool
    def tavily_search(query: str) -> dict:
        """Search the web for up-to-date and accurate information using Tavily.
        
        Args:
            query (str): The search query string.
        """    
        client = TavilyClient(api_key=settings.tavily_api_key)
        response = client.search(query, max_results=5, topic="news")
        
        return response


    
    
    