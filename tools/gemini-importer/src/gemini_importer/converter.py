import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import KnowledgePackage
from athena_sdk.provenance import create_provenance


def conversation_to_akp(conversation):

    content = "\n\n".join(
        f"{m.role}: {m.content}"
        for m in conversation.messages
    )

    return KnowledgePackage(
        title=conversation.title
        or "Untitled Gemini Conversation",

        content=content,

        source={
            "name": "Gemini",
            "type": "AI conversation"
        },

        confidence={
            "level": "low",
            "reason": "AI-generated content"
        },

        evidence={
            "source_type": "Gemini export",
            "title": conversation.title
        },

        provenance=create_provenance(
            "athena-gemini-importer",
            "0.1"
        ),

        metadata={
            "conversation_source":
                conversation.source
        }
    )
