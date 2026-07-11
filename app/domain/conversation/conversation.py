from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import ANY
from uuid import UUID, uuid4

from langchain_core.messages import BaseMessage


@dataclass(slots=True)
class Conversation:
    id: UUID = field(default_factory=uuid4)
    messages: list[BaseMessage] = field(default_factory=list)
    metadata: dict[str, ANY] = field(default_factory=dict)
    
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    
    def add_message(self, message: BaseMessage) -> None:
        self.messages.append(message)
        self.updated_at = datetime.now(UTC)
        
    def clear(self) -> None:
        self.messages.clear()
        self.updated_at = datetime.now(UTC)
        
    @property
    def message_count(self) -> int:
        return len(self.messages)
    
    @property
    def last_message(self) -> BaseMessage | None:
        if not self.messages:
            return None
        
        return self.messages[-1]