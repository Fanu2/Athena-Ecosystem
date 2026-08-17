from git_repository_importer.converter import (
    repository_to_akp
)

from git_repository_importer.exporter import (
    export_akp
)


def test_exporter(tmp_path):

    repository = {
        "name": "export-test",
        "files": [],
        "latest_commit": "none",
        "readme": ""
    }

    package = repository_to_akp(
        repository
    )

    export_akp(
        package,
        str(tmp_path),
        "repository.akp.json"
    )

    assert (
        tmp_path / "repository.akp.json"
    ).exists()
