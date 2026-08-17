from git_repository_importer.converter import (
    repository_to_akp
)


def test_converter():

    repository = {
        "name": "test-repo",
        "files": [
            "README.md"
        ],
        "latest_commit": "abc123",
        "readme": "Test project"
    }

    package = repository_to_akp(
        repository
    )

    assert package.title == "test-repo"
    assert package.source["name"] == "Git Repository"
    assert package.confidence["level"] == "high"
