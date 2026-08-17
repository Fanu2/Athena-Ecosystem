from pathlib import Path

from gemini_importer.parser import (
    parse_gemini_export
)


def test_parser():

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "gemini-sample"
        / "conversations.json"
    )

    conversations = parse_gemini_export(
        str(sample)
    )

    assert len(conversations) == 2
    assert conversations[0].source == "Gemini"
    assert len(conversations[0].messages) == 2
