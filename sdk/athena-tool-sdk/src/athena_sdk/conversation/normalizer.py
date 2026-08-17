from .models import (
    Conversation,
    Message,
)


def normalize_role(
    role: str
) -> str:
    """
    Convert provider roles into
    common Athena roles.
    """

    role = role.lower()

    if role in (
        "request",
        "user",
        "human"
    ):
        return "user"

    if role in (
        "response",
        "assistant",
        "ai"
    ):
        return "assistant"

    return "unknown"


def normalize_conversation(
    conversation: Conversation
) -> Conversation:
    """
    Normalize conversation roles.
    """

    messages = []

    for message in conversation.messages:
        messages.append(
            Message(
                role=normalize_role(
                    message.role
                ),
                content=message.content,
                timestamp=message.timestamp
            )
        )

    return Conversation(
        title=conversation.title,
        messages=messages,
        created_at=conversation.created_at,
        source=conversation.source
    )
