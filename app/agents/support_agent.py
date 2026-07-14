from langchain.agents import create_agent
from app.llm.provider import create_ollama_model
from app.tools.support import search_tavily

def create_support_agent():
    agent = create_agent(
        model=create_ollama_model(),
        tools=[search_tavily],
        system_prompt="""
            when asked any query from the agent put the user_query as it is to the search_tavily tool and then use the response to generate a response
        """
    )
    
    return agent
