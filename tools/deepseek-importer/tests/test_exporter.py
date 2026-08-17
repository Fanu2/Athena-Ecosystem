from deepseek_importer.models import (
    Conversation,
    Message
)

from deepseek_importer.converter import (
    conversation_to_akp
)

from deepseek_importer.exporter import (
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
        ]
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
        tmp_path /
        "test.akp.json"
    ).exists()
