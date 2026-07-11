from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.conversation import Conversation

class ConversationRepository(ABC):

    @abstractmethod
    def get(self, conversation_id: UUID) -> Conversation | None:
        pass

    @abstractmethod
    def save(self, conversation: Conversation) -> None:
        pass

    @abstractmethod
    def delete(self, conversation_id: UUID) -> None:
        pass
