from athena_sdk.conversation import (
    Conversation,
    Message,
)

from claude_importer.converter import (
    conversation_to_akp
)


def test_converter():

    conversation = Conversation(
        title="Claude Test",
        messages=[
            Message(
                role="human",
                content="Hello"
            )
        ],
        source="Claude"
    )

    package = conversation_to_akp(
        conversation
    )

    assert package.title == "Claude Test"
    assert package.source["name"] == "Claude"
    assert package.confidence["level"] == "low"
