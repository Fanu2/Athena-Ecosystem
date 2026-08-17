from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ContextItem:

    key: str

    value: str

    created_at: str = field(
        default_factory=lambda:
        datetime.now(
            timezone.utc
        ).isoformat()
    )


class ContextContinuity:


    def __init__(self):

        self.items = []


    def remember(
        self,
        key: str,
        value: str
    ):

        self.items.append(
            ContextItem(
                key=key,
                value=value
            )
        )


    def recall(
        self,
        key: str
    ):

        return [
            item
            for item in self.items
            if item.key == key
        ]
