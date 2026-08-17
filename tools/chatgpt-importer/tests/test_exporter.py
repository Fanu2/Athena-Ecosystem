from athena_sdk.conversation import (
    Conversation,
    Message,
)

from chatgpt_importer.converter import (
    conversation_to_akp
)

from chatgpt_importer.exporter import (
    export_akp
)


def test_exporter(tmp_path):

    conversation = Conversation(
        title="Export Test",
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

    export_akp(
        package,
        str(tmp_path),
        "test.akp.json"
    )

    assert (
        tmp_path / "test.akp.json"
    ).exists()
