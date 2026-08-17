from deepseek_importer.models import (
    Conversation,
    Message
)

from deepseek_importer.converter import (
    conversation_to_akp
)


def test_converter():

    conversation = Conversation(
        title="Test AKP",
        messages=[
            Message(
                role="user",
                content="Hello"
            )
        ]
    )

    package = conversation_to_akp(
        conversation
    )

    assert package.title == "Test AKP"
    assert package.source["name"] == "DeepSeek"
    assert package.confidence["level"] == "low"
