"""Semantic document chunking placeholder."""

from langchain_core.documents import Document

from .base import BaseChunker


class SemanticChunker(BaseChunker):
    """Reserve semantic chunking for a future embedding-enabled implementation."""

    def split(self, documents: list[Document]) -> list[Document]:
        """Raise until an embedding model is available."""
        raise NotImplementedError(
            "SemanticChunker requires an embedding model and will be implemented later."
        )
