from pathlib import Path

from gemini_importer.importer import (
    import_gemini
)


def test_pipeline(tmp_path):

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "gemini-sample"
        / "conversations.json"
    )

    result = import_gemini(
        str(sample),
        str(tmp_path)
    )

    assert result["input"] == 2
    assert result["exported"] == 2
    assert result["status"] == "success"
