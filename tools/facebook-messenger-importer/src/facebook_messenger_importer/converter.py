import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import KnowledgePackage
from athena_sdk.provenance import create_provenance


def conversation_to_akp(
    conversation
):

    content = "\n\n".join(
        f"{m.role}: {m.content}"
        for m in conversation.messages
    )

    return KnowledgePackage(
        title=conversation.title,

        content=content,

        source={
            "name": "Facebook Messenger",
            "type": "personal conversation"
        },

        confidence={
            "level": "medium",
            "reason": "User conversation archive"
        },

        evidence={
            "source_type": "Facebook Messenger export",
            "title": conversation.title
        },

        provenance=create_provenance(
            "athena-facebook-messenger-importer",
            "0.1"
        ),

        metadata={
            "conversation_source":
                conversation.source
        }
    )
