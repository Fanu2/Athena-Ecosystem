from .parser import parse_repository
from .converter import repository_to_akp
from .exporter import export_akp
from .intelligence.analyzer import (
    analyze_repository
)


def import_repository(
    repo_path,
    output_dir
):

    repository = parse_repository(
        repo_path
    )

    analysis = analyze_repository(
        repo_path
    )

    package = repository_to_akp(
        repository,
        analysis
    )

    export_akp(
        package,
        output_dir,
        "repository.akp.json"
    )

    return {
        "status": "success",
        "repository":
            repository["name"],
        "analysis":
            analysis
    }
