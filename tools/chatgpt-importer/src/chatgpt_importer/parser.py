import json
from pathlib import Path
import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.conversation import (
    Conversation,
    Message,
)


def parse_chatgpt_export(
    file_path: str
) -> list[Conversation]:
    """
    Parse ChatGPT conversations.json
    into Athena Conversation objects.
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

            author = message.get(
                "author",
                {}
            )

            role = author.get(
                "role",
                "unknown"
            )

            content = message.get(
                "content",
                {}
            )

            parts = content.get(
                "parts",
                []
            )

            for part in parts:

                if not isinstance(
                    part,
                    str
                ):
                    continue

                messages.append(
                    Message(
                        role=role,
                        content=part
                    )
                )

        conversations.append(
            Conversation(
                title=item.get(
                    "title",
                    "Untitled ChatGPT Conversation"
                ),
                messages=messages,
                source="ChatGPT"
            )
        )

    return conversations
