# app/tools/tavily/search.py
from langchain_core.tools import tool
from app.services.support.search_service import SearchService

search_service = SearchService()

@tool
def tavily_web_search(query: str) -> dict:
    """
    Search the web for the latest and factual information.

    Use this tool whenever the user's question involves:
    - current events
    - recent sports results
    - live information
    - recent news
    - recent software releases
    - information you are uncertain about

    Pass the user's latest question exactly as received.
    """

    print("--------------- using search Tavily ---------------")

    return search_service.search(query)