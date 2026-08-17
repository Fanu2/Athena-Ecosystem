from .parser import parse_repository
from .converter import repository_to_akp
from .exporter import export_akp


def import_repository(
    repo_path: str,
    output_dir: str
) -> dict:
    """
    Import a Git repository into AKP.
    """

    repository = parse_repository(
        repo_path
    )

    package = repository_to_akp(
        repository
    )

    export_akp(
        package,
        output_dir,
        "repository.akp.json"
    )

    return {
        "status": "success",
        "repository": repository["name"]
    }
