from .models import (
    Conversation,
    Message,
)


def normalize_role(
    role: str
) -> str:
    """
    Convert source roles into
    common AI roles.
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

    normalized_messages = []

    for message in conversation.messages:

        normalized_messages.append(
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
        messages=normalized_messages,
        created_at=conversation.created_at,
        source=conversation.source
    )
