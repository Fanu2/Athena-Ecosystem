from deepseek_importer.models import (
    Conversation,
    Message
)

from deepseek_importer.normalizer import (
    normalize_conversation
)


def test_normalizer():

    conversation = Conversation(
        title="Test",
        messages=[
            Message(
                role="REQUEST",
                content="Hello"
            ),
            Message(
                role="RESPONSE",
                content="Hi"
            )
        ]
    )

    result = normalize_conversation(
        conversation
    )

    assert result.messages[0].role == "user"
    assert result.messages[1].role == "assistant"
