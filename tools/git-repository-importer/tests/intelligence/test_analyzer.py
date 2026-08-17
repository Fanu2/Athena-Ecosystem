from pathlib import Path

from git_repository_importer.intelligence.analyzer import (
    analyze_repository
)


def test_analyzer():

    root = Path(__file__).resolve().parents[4]

    repo = (
        root
        / "examples"
        / "git-sample-repo"
    )

    result = analyze_repository(
        str(repo)
    )

    assert result["total_files"] >= 1
    assert ".md" in result["extensions"]
