from fastapi import APIRouter

from app.services.chat_service import ChatService

chat_router = APIRouter()

chat_service = ChatService()

@chat_router.post("/chat")
def chat(message: str):
    return chat_service.chat(message)