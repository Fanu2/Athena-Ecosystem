from athena_sdk.conversation import (
    Conversation,
    Message,
)

from gemini_importer.converter import (
    conversation_to_akp
)

from gemini_importer.exporter import (
    export_akp
)


def test_exporter(tmp_path):

    conversation = Conversation(
        title="Gemini Export Test",
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

    export_akp(
        package,
        str(tmp_path),
        "test.akp.json"
    )

    assert (
        tmp_path / "test.akp.json"
    ).exists()
