from git_repository_importer.importer import (
    import_repository
)


def test_pipeline(tmp_path):

    result = import_repository(
        "examples/git-sample-repo",
        str(tmp_path)
    )

    assert result["status"] == "success"
    assert result["repository"] == "git-sample-repo"
