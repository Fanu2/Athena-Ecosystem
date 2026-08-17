from pathlib import Path

from facebook_messenger_importer.importer import (
    import_messenger
)


def test_pipeline(tmp_path):

    root = Path(__file__).resolve().parents[3]

    sample = (
        root
        / "examples"
        / "facebook-messenger-sample"
        / "messages.json"
    )

    result = import_messenger(
        str(sample),
        str(tmp_path)
    )

    assert result["input"] == 2
    assert result["exported"] == 2
    assert result["status"] == "success"
