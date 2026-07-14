from langchain_ollama import ChatOllama

from app.core.config import get_settings

settings = get_settings()


def create_ollama_model() -> ChatOllama:
    return ChatOllama(
        model=settings.ollama_model,
        base_url=settings.ollama_base_url,
        temperature=0,
    )
