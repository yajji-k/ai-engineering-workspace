"""Shared contract for document chunkers."""

from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseChunker(ABC):
    """Define the contract implemented by document chunkers."""

    @abstractmethod
    def split(self, documents: list[Document]) -> list[Document]:
        """Split documents into smaller documents."""
        ...
