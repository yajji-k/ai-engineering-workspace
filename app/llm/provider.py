from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import get_settings

settings = get_settings()


def create_gemini_model() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.google_model,
        google_api_key=settings.google_api_key,
        temperature=0,
    )