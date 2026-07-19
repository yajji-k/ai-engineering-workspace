"""Factory for document loaders."""

from pathlib import Path

from .base import BaseLoader
from .markdown import MarkdownLoader
from .pdf import PDFLoader
from .text import TextLoader


class LoaderFactory:
    """Factory responsible for creating document loaders."""

    _LOADERS : dict[str, type[BaseLoader]] = {
        ".pdf": PDFLoader,
        ".txt": TextLoader,
        ".md": MarkdownLoader,
    }

    @classmethod
    def create(cls, source: Path) -> BaseLoader:
        """
        Create a loader for the given source file.

        Args:
            source: Path to the document.

        Returns:
            An instance of the appropriate BaseLoader implementation.

        Raises:
            ValueError: If the file extension is not supported.
        """
        try:
            loader_class = cls._LOADERS[source.suffix.lower()]
        except KeyError as error:
            supported = ", ".join(sorted(cls.LOADERS.keys()))
            raise ValueError(
                f"Unsupported file extension '{source.suffix or '<none>'}'. "
                f"Supported extensions: {supported}"
            ) from error

        return loader_class()

    @classmethod
    def register(
        cls,
        extension: str,
        loader: type[BaseLoader],
    ) -> None:
        """
        Register a new loader implementation.

        This allows additional document types to be supported without
        modifying the factory.
        """
        cls._LOADERS[extension.lower()] = loader