from athena_sdk.conversation import (
    Conversation,
    Message,
)

from facebook_messenger_importer.converter import (
    conversation_to_akp
)


def test_converter():

    conversation = Conversation(
        title="Messenger Test",
        messages=[
            Message(
                role="User",
                content="Hello"
            )
        ],
        source="Facebook Messenger"
    )

    package = conversation_to_akp(
        conversation
    )

    assert package.source["name"] == "Facebook Messenger"
    assert package.confidence["level"] == "medium"
