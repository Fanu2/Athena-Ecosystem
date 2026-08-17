import json

from deepseek_importer.importer import (
    import_deepseek
)


def test_full_pipeline(tmp_path):

    source = tmp_path / "conversations.json"

    data = [
        {
            "title": "Pipeline Test",
            "mapping": {
                "1": {
                    "message": {
                        "fragments": [
                            {
                                "type": "REQUEST",
                                "content": "Hello"
                            }
                        ]
                    }
                }
            }
        }
    ]

    source.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    output = tmp_path / "output"

    result = import_deepseek(
        str(source),
        str(output)
    )

    assert result["input"] == 1
    assert result["exported"] == 1
    assert result["status"] == "success"
