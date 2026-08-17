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


def parse_gemini_export(file_path: str):
    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    conversations = []

    for item in data:

        messages = []

        for message in item.get(
            "messages",
            []
        ):
            messages.append(
                Message(
                    role=message.get(
                        "role",
                        "unknown"
                    ),
                    content=message.get(
                        "text",
                        ""
                    )
                )
            )

        conversations.append(
            Conversation(
                title=item.get(
                    "title",
                    "Untitled Gemini Conversation"
                ),
                messages=messages,
                created_at=item.get(
                    "created_at"
                ),
                source="Gemini"
            )
        )

    return conversations
