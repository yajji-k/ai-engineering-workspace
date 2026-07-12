from langchain.agents import create_agent
from langchain_core.runnables import Runnable

from app.llm.provider import create_gemini_model

from app.prompts import SUPPORT_AGENT_SYSTEM_PROMPT

def create_support_agent() -> Runnable:
    gemini_model = create_gemini_model()
    
    return create_agent(
        model=gemini_model,
        system_prompt=SUPPORT_AGENT_SYSTEM_PROMPT
    )