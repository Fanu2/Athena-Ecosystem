from pathlib import Path

from claude_importer.parser import (
    parse_claude_export
)


def test_parser():

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "claude-sample"
        / "conversations.json"
    )

    conversations = parse_claude_export(
        str(sample)
    )

    assert len(conversations) == 2
    assert conversations[0].source == "Claude"
    assert len(conversations[0].messages) == 2
