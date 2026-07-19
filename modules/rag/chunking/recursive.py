"""Recursive character-based document chunking."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .base import BaseChunker


class RecursiveChunker(BaseChunker):
    """Split documents with LangChain's recursive character splitter."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200) -> None:
        """Initialize the splitter with chunk sizing options."""
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, documents: list[Document]) -> list[Document]:
        """Split the supplied documents into recursive character chunks."""
        return self._splitter.split_documents(documents)
