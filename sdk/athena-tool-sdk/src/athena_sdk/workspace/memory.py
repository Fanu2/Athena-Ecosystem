from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class MemoryItem:

    content: str

    created_at: str = field(
        default_factory=lambda:
        datetime.now(
            timezone.utc
        ).isoformat()
    )

    access_count: int = 0

    important: bool = False


def mark_accessed(
    item: MemoryItem
):

    item.access_count += 1

    return item


def mark_important(
    item: MemoryItem
):

    item.important = True

    return item
