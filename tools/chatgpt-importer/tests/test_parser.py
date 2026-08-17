from pathlib import Path

from chatgpt_importer.parser import (
    parse_chatgpt_export
)


def test_parser():

    root = Path(__file__).resolve().parents[3]

    file = (
        root
        / "examples"
        / "chatgpt-sample"
        / "conversations.json"
    )

    conversations = parse_chatgpt_export(
        str(file)
    )

    assert len(conversations) == 2
    assert conversations[0].source == "ChatGPT"
    assert len(conversations[0].messages) > 0
