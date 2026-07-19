from pathlib import Path

from langchain_core.documents import Document

from .base import BaseLoader
from .text import TextLoader


class MarkdownLoader(BaseLoader):
    """Load Markdown files as plain text documents."""

    def load(self, source: Path) -> list[Document]:
        """Load and return the document contained in a Markdown file."""
        return TextLoader().load(source)
