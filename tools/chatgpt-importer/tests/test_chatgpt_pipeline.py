from pathlib import Path

from chatgpt_importer.importer import (
    import_chatgpt
)


def test_chatgpt_pipeline(tmp_path):

    project_root = Path(__file__).resolve().parents[3]

    sample_file = (
        project_root
        / "examples"
        / "chatgpt-sample"
        / "conversations.json"
    )

    result = import_chatgpt(
        str(sample_file),
        str(tmp_path)
    )

    assert result["input"] == 2
    assert result["exported"] == 2
    assert result["status"] == "success"
