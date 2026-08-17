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


def parse_claude_export(
    file_path: str
) -> list[Conversation]:
    """
    Parse Claude conversation export
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

        for chat_message in item.get(
            "chat_messages",
            []
        ):

            messages.append(
                Message(
                    role=chat_message.get(
                        "sender",
                        "unknown"
                    ),
                    content=chat_message.get(
                        "text",
                        ""
                    )
                )
            )

        conversations.append(
            Conversation(
                title=item.get(
                    "name",
                    "Untitled Claude Conversation"
                ),
                messages=messages,
                created_at=item.get(
                    "created_at"
                ),
                source="Claude"
            )
        )

    return conversations
