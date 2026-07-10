from app.application.extraction.extraction_schema import User
from app.application.extraction.extraction_prompt import EXTRACTION_PROMPT
from app.infrastructure.models.gemini import get_chat_model

class ExtractionService:
    def __init__(self):
        llm = get_chat_model()
        
        structured_llm = llm.with_structured_output(User)
        
        self._chain = EXTRACTION_PROMPT | structured_llm
        
    def extract(self, text: str) -> User:
        return self._chain.invoke(
            {
                "text": text
            }
        )
