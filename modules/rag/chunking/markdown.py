"""Markdown document chunking."""

from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

from .base import BaseChunker


class MarkdownChunker(BaseChunker):
    """Split Markdown documents on their header structure."""

    def __init__(self) -> None:
        """Initialize the Markdown header splitter."""
        self._splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
            ]
        )

    def split(self, documents: list[Document]) -> list[Document]:
        """Split the supplied documents into Markdown header chunks."""
        return [
            Document(page_content=chunk.page_content, metadata=document.metadata)
            for document in documents
            for chunk in self._splitter.split_text(document.page_content)
        ]
