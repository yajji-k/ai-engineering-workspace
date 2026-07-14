from langchain_core.chat_history import InMemoryChatMessageHistory

class ConversationHistoryManager:
    def __init__(self):
        self._store: dict[str, InMemoryChatMessageHistory] = {}

    def get_history(self, conversation_id: str) -> InMemoryChatMessageHistory:
        """
        Returns the chat history for a conversation.
        Creates one if it doesn't already exist.
        """
        if conversation_id not in self._store:
            self._store[conversation_id] = InMemoryChatMessageHistory()

        return self._store[conversation_id]
    
    def clear_history(self, conversation_id: str) -> None:
        if conversation_id in self._store:
            del self._store[conversation_id]