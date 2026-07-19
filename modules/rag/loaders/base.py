from abc import ABC, abstractmethod
from pathlib import Path

from langchain_core.documents import Document


class BaseLoader(ABC):
    """Define the contract implemented by document loaders."""

    @abstractmethod
    def load(self, source: Path) -> list[Document]:
        """Load documents from the given source file."""
        ...
