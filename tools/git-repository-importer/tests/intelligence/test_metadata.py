from git_repository_importer.converter import (
    repository_to_akp
)


def test_repository_analysis_metadata():

    repository = {
        "name": "analysis-test",
        "files": [
            "main.py"
        ],
        "latest_commit": "abc",
        "readme": "test"
    }

    analysis = {
        "total_files": 1,
        "extensions": {
            ".py": 1
        },
        "directories": [
            "."
        ]
    }

    package = repository_to_akp(
        repository,
        analysis
    )

    assert (
        "repository_analysis"
        in package.metadata
    )

    assert (
        package.metadata["repository_analysis"]
        ["total_files"]
        == 1
    )
