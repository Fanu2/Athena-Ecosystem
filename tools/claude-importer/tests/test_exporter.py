from athena_sdk.conversation import (
    Conversation,
    Message,
)

from claude_importer.converter import (
    conversation_to_akp
)

from claude_importer.exporter import (
    export_akp
)


def test_exporter(tmp_path):

    conversation = Conversation(
        title="Claude Export Test",
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

    export_akp(
        package,
        str(tmp_path),
        "test.akp.json"
    )

    assert (
        tmp_path / "test.akp.json"
    ).exists()
