"""Token-based document chunking."""

from langchain_core.documents import Document
from langchain_text_splitters import TokenTextSplitter

from .base import BaseChunker


class TokenChunker(BaseChunker):
    """Split documents with LangChain's token splitter."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200) -> None:
        """Initialize the splitter with chunk sizing options."""
        self._splitter = TokenTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, documents: list[Document]) -> list[Document]:
        """Split the supplied documents into token chunks."""
        return self._splitter.split_documents(documents)
