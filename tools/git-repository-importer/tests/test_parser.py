from pathlib import Path

from git_repository_importer.parser import (
    parse_repository
)


def test_parser():

    root = Path(__file__).resolve().parents[3]

    repo = (
        root
        / "examples"
        / "git-sample-repo"
    )

    result = parse_repository(
        str(repo)
    )

    assert result["name"] == "git-sample-repo"
    assert "README.md" in result["files"]
