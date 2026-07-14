from langchain_core.prompts import ChatPromptTemplate

SEARCH_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a support assistant.

Answer ONLY using the search results.

If the search results don't contain the answer, say so.

Keep answers concise.
"""
    ),
    (
        "human",
        """
Question:
{question}

Search Results:
{search_results}
"""
    )
])