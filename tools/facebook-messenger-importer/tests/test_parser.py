from pathlib import Path

from facebook_messenger_importer.parser import (
    parse_messenger_export
)


def test_parser():

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "facebook-messenger-sample"
        / "messages.json"
    )

    conversations = parse_messenger_export(
        str(sample)
    )

    assert len(conversations) == 2
    assert conversations[0].source == "Facebook Messenger"
    assert len(conversations[0].messages) == 2
