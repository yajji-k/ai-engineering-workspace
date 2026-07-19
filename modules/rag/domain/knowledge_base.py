"""Knowledge base domain entity."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class KnowledgeBase:
    """Represent a named collection of knowledge sources."""

    name: str
    description: str | None = None
    id: UUID = field(default_factory=uuid4, init=False)
    created_at: datetime = field(default_factory=datetime.utcnow, init=False)

    def display_name(self) -> str:
        """Return the knowledge base name for display."""
        return self.name
