from app.prompts.support_agent import SEARCH_PROMPT
from .support.tavity_search_service import TavitySearchService
from app.llm.provider import create_ollama_model

search_service = TavitySearchService()

class ChatService:
    def __init__(self):
        self._model = create_ollama_model()
        self._chain = SEARCH_PROMPT | self._model

    def search(self, user_query: str):

        search_results = search_service.tavily_search.invoke(
            {"query": user_query}
        )

        response = self._chain.invoke(
            {
                "question": user_query,
                "search_results": search_results
            }
        )
        
        print(response)

        return response.content
