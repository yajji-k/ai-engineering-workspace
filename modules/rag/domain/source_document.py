"""Source document domain entity."""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class SourceDocument:
    """Represent a file that belongs to a knowledge base."""

    knowledge_base_id: UUID
    source: Path
    id: UUID = field(default_factory=uuid4, init=False)
    file_name: str = field(init=False)
    extension: str = field(init=False)
    created_at: datetime = field(default_factory=datetime.utcnow, init=False)

    def __post_init__(self) -> None:
        """Validate the source file and derive its file attributes."""
        if not self.source.exists():
            raise FileNotFoundError(f"Source file does not exist: {self.source}")
        if not self.source.is_file():
            raise ValueError(f"Source path is not a file: {self.source}")

        object.__setattr__(self, "file_name", self.source.name)
        object.__setattr__(self, "extension", self.source.suffix.lower())
