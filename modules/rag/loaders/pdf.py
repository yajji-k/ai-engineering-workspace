from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from .base import BaseLoader


class PDFLoader(BaseLoader):
    """Load PDF files using LangChain's ``PyPDFLoader``."""

    def load(self, source: Path) -> list[Document]:
        """Load and return the documents contained in a PDF file."""
        if not source.exists():
            raise FileNotFoundError(f"PDF file does not exist: {source}")

        return PyPDFLoader(str(source)).load()
