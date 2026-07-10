from langchain.messages import HumanMessage

from app.infrastructure.models.gemini import get_chat_model

def chat(message: str)->str:
    llm = get_chat_model()
    
    response = llm.invoke(
        [
            HumanMessage(content=message)
        ]
    )
    
    return response.content