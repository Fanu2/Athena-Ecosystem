import json
from pathlib import Path

from .models import (
    Conversation,
    Message,
)


def parse_deepseek_export(
    file_path: str
) -> list[Conversation]:
    """
    Parse DeepSeek conversations.json
    """

    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    conversations = []

    for item in data:

        messages = []

        mapping = item.get(
            "mapping",
            {}
        )

        for node in mapping.values():

            message = node.get(
                "message"
            )

            if not message:
                continue

            fragments = message.get(
                "fragments",
                []
            )

            for fragment in fragments:

                content = fragment.get(
                    "content"
                )

                if not content:
                    continue

                role = fragment.get(
                    "type",
                    "unknown"
                )

                messages.append(
                    Message(
                        role=role,
                        content=content,
                        timestamp=message.get(
                            "inserted_at"
                        )
                    )
                )

        conversations.append(
            Conversation(
                title=item.get(
                    "title",
                    "Untitled"
                ),
                messages=messages,
                created_at=item.get(
                    "inserted_at"
                )
            )
        )

    return conversations
