from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a senior AI engineering mentor. Give concise and technically accurate answers.",
        ),
        MessagesPlaceholder("messages")
    ]
)