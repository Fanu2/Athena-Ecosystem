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


def parse_messenger_export(
    file_path: str
):

    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    conversations = []

    for thread in data:

        messages = []

        for item in thread.get(
            "messages",
            []
        ):

            messages.append(
                Message(
                    role=item.get(
                        "sender_name",
                        "unknown"
                    ),
                    content=item.get(
                        "content",
                        ""
                    )
                )
            )

        conversations.append(
            Conversation(
                title=thread.get(
                    "thread_name",
                    "Untitled Messenger Conversation"
                ),
                messages=messages,
                source="Facebook Messenger"
            )
        )

    return conversations
