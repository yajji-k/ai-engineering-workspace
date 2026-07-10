from app.infrastructure.models.gemini import get_chat_model
from app.application.chat.prompt import CHAT_PROMPT
from langchain_core.messages import BaseMessage

class ChatService():
    def __init__(self):
        self._chat_model = get_chat_model()
        self._chain = CHAT_PROMPT | self._chat_model

    
    def chat(self, messages: list[BaseMessage]) -> str:
        response = self._chain.invoke(
            {
                "messages": messages
            }
        )

        return response.content
    
    async def achat(self, messages: list[BaseMessage]) -> str:
        response = await self._chain.ainvoke(
            {
                "messages": messages
            }
        )

        return response.content
    
    def stream(self, messages: list[BaseMessage]):
        for chunk in self._chain.stream(
            {
                "messages": messages
            }
        ):
            yield chunk
    
    async def astream(self, messages: list[BaseMessage]):
        async for chunk in self._chain.astream(
            {
                "messages": messages
            }
        ):
            yield chunk
            