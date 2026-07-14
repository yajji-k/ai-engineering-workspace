from langchain.agents import create_agent
from app.llm.provider import create_ollama_model
from app.tools.support.search import tavily_web_search
from app.prompts.support_agent import SUPPORT_AGENT_PROMPT

def create_support_agent():
    agent = create_agent(
        model=create_ollama_model(),
        tools=[tavily_web_search],
        system_prompt=SUPPORT_AGENT_PROMPT,
    )
    
    return agent
