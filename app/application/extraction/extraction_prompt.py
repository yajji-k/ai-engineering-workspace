from langchain_core.prompts import ChatPromptTemplate


EXTRACTION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Extraction the user's information from the text"
        ),
        (
            "human",
            "{text}"
        )
    ]
)