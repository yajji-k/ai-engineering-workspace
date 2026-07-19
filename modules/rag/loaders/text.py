from pathlib import Path

from langchain_community.document_loaders import TextLoader as LangChainTextLoader
from langchain_core.documents import Document

from .base import BaseLoader


class TextLoader(BaseLoader):
    """Load plain-text files using LangChain's ``TextLoader``."""

    def load(self, source: Path) -> list[Document]:
        """Load and return the document contained in a text file."""
        if not source.exists():
            raise FileNotFoundError(f"Text file does not exist: {source}")

        return LangChainTextLoader(str(source)).load()
