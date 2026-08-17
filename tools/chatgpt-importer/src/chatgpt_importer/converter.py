import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import KnowledgePackage
from athena_sdk.provenance import create_provenance

from athena_sdk.conversation import Conversation


def conversation_to_akp(
    conversation: Conversation
) -> KnowledgePackage:
    """
    Convert ChatGPT conversation
    into Athena Knowledge Package.
    """

    content_parts = []

    for message in conversation.messages:
        content_parts.append(
            f"{message.role}: {message.content}"
        )

    content = "\n\n".join(
        content_parts
    )

    title = (
        conversation.title
        if conversation.title
        else "Untitled ChatGPT Conversation"
    )

    return KnowledgePackage(
        title=title,

        content=content,

        source={
            "name": "ChatGPT",
            "type": "AI conversation"
        },

        confidence={
            "level": "low",
            "reason": "AI-generated content"
        },

        evidence={
            "source_type": "ChatGPT export",
            "title": title
        },

        provenance=create_provenance(
            "athena-chatgpt-importer",
            "0.1"
        ),

        metadata={
            "conversation_source":
                conversation.source
        }
    )
