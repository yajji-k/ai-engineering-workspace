from langchain_core.messages import AIMessage, HumanMessage

from app.application.chat.chat_service import ChatService
from app.domain.conversation import Conversation


class ConversationService:

    def __init__(self, chat_service: ChatService) -> None:
        self._chat_service = chat_service

    def chat(self, conversation: Conversation, user_input: str) -> str:
        conversation.add_message(
            HumanMessage(content=user_input)
        )

        response = self._chat_service.chat(
            messages=conversation.messages
        )

        conversation.add_message(
            AIMessage(content=response)
        )

        return response
    
    async def achat(self, conversation: Conversation, user_input: str) -> str:
        conversation.add_message(
            HumanMessage(content=user_input)
        )
        
        response = await self._chat_service.achat(
            messages=conversation.messages
        )
        
        conversation.add_message(
            AIMessage(content=response)
        )
        
        return response
