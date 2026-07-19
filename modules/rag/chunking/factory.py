"""Factory for document chunkers."""

from .base import BaseChunker
from .markdown import MarkdownChunker
from .recursive import RecursiveChunker
from .semantic import SemanticChunker
from .token import TokenChunker


class ChunkerFactory:
    """Factory responsible for creating document chunkers."""

    _CHUNKERS: dict[str, type[BaseChunker]] = {
        "recursive": RecursiveChunker,
        "token": TokenChunker,
        "markdown": MarkdownChunker,
        "semantic": SemanticChunker,
    }

    @classmethod
    def create(cls, strategy: str) -> BaseChunker:
        """
        Create a chunker for the given strategy.

        Args:
            strategy: Chunking strategy name.

        Returns:
            An instance of the requested BaseChunker implementation.

        Raises:
            ValueError: If the requested strategy is not supported.
        """
        try:
            chunker_class = cls._CHUNKERS[strategy.lower()]
        except KeyError as error:
            supported = ", ".join(sorted(cls.CHUNKERS.keys()))
            raise ValueError(
                f"Unsupported chunking strategy '{strategy}'. "
                f"Supported strategies: {supported}"
            ) from error

        return chunker_class()

    @classmethod
    def register(
        cls,
        strategy: str,
        chunker: type[BaseChunker],
    ) -> None:
        """
        Register a new chunking strategy.

        This allows new chunkers to be added without modifying the factory.
        """
        cls._CHUNKERS[strategy.lower()] = chunker