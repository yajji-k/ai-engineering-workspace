from uuid import UUID

from app.domain.conversation import Conversation, ConversationRepository

class InMemoryConversationRepository(ConversationRepository):
    def __init__(self):
        self._conversations: dict[UUID, Conversation] = {}
    
    def get(self, conversation_id: UUID) -> Conversation:
        return self._conversations.get(conversation_id)
    
    def save(self, conversation: Conversation) -> None:
        self._conversations[conversation.id] = conversation
    
    def delete(self, conversation_id):
        self._conversations.pop(conversation_id, None)