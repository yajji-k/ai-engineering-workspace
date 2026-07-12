from app.agents.support_agent import create_support_agent
from langchain_core.messages import HumanMessage


class ChatService:
    def __init__(self):
        self._agent = create_support_agent()
    
    def chat(self, message: str):
        return self._agent.invoke(
            {
                "messages": [
                    HumanMessage(content=message)
                ]
            }
        )