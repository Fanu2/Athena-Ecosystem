from athena_sdk.conversation import (
    Conversation,
    Message,
)

from chatgpt_importer.converter import (
    conversation_to_akp
)


def test_converter():

    conversation = Conversation(
        title="Test ChatGPT",
        messages=[
            Message(
                role="user",
                content="Hello"
            )
        ],
        source="ChatGPT"
    )

    package = conversation_to_akp(
        conversation
    )

    assert package.title == "Test ChatGPT"
    assert package.source["name"] == "ChatGPT"
    assert package.confidence["level"] == "low"
