from athena_sdk.conversation import (
    Conversation,
    Message,
)

from gemini_importer.converter import (
    conversation_to_akp
)


def test_converter():

    conversation = Conversation(
        title="Gemini Test",
        messages=[
            Message(
                role="user",
                content="Hello"
            )
        ],
        source="Gemini"
    )

    package = conversation_to_akp(
        conversation
    )

    assert package.title == "Gemini Test"
    assert package.source["name"] == "Gemini"
    assert package.confidence["level"] == "low"
