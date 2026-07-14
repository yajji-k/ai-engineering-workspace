from langchain_core.tools import tool
from app.services.chat_service import ChatService
from app.core.config import get_settings

settings = get_settings()

chat_service = ChatService()

@tool
def search_tavily(user_query: str):
    """
        pass the user_query as it is to perform the service
    """
    return chat_service.search(user_query=user_query)
