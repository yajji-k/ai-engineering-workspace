from fastapi import APIRouter

from app.services.chat_service import ChatService

chat_router = APIRouter()

chat_service = ChatService()

@chat_router.post("/chat")
def chat(user_input: str, conversation_id: str):
    return chat_service.send_message(
        conversation_id=conversation_id,
        user_input=user_input,
    )