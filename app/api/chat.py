from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from app.services.chat_service import ChatService
from app.agents.support_agent import create_support_agent

chat_router = APIRouter()

chat_service = ChatService()

@chat_router.post("/chat")
def chat(message: str):
    agent = create_support_agent()
    
    response = agent.invoke({
        "messages": [
            HumanMessage(content=message)
        ]
    })
    
    return response