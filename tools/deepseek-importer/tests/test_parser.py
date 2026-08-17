import json

from deepseek_importer.parser import parse_deepseek_export


def test_parser(tmp_path):

    data = [
        {
            "title": "Test Conversation",
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

    file = tmp_path / "conversations.json"

    file.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    result = parse_deepseek_export(
        str(file)
    )

    assert len(result) == 1
    assert result[0].title == "Test Conversation"
    assert len(result[0].messages) == 1
