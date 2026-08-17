from pathlib import Path

from claude_importer.importer import (
    import_claude
)


def test_pipeline(tmp_path):

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "claude-sample"
        / "conversations.json"
    )

    result = import_claude(
        str(sample),
        str(tmp_path)
    )

    assert result["input"] == 2
    assert result["exported"] == 2
    assert result["status"] == "success"
