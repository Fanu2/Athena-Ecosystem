from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Message:
    """
    Universal AI conversation message.
    """

    role: str
    content: str
    timestamp: Optional[str] = None


@dataclass
class Conversation:
    """
    Universal AI conversation model.
    """

    title: str

    messages: list[Message] = field(
        default_factory=list
    )

    created_at: Optional[str] = None

    source: str = "unknown"
