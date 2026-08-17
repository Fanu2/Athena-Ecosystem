from git_repository_importer.importer import (
    import_repository
)


def test_git_importer_regression(tmp_path):

    result = import_repository(
        "examples/git-sample-repo",
        str(tmp_path)
    )

    assert result["status"] == "success"

    assert (
        "analysis"
        in result
    )
