from pathlib import Path
import subprocess


def parse_repository(
    repo_path: str
) -> dict:
    """
    Extract repository metadata.
    """

    path = Path(repo_path)

    files = []

    for item in path.rglob("*"):

        if item.is_file():

            files.append(
                str(
                    item.relative_to(path)
                )
            )

    try:

        latest_commit = subprocess.check_output(
            [
                "git",
                "-C",
                str(path),
                "log",
                "-1",
                "--oneline"
            ],
            text=True
        ).strip()

    except Exception:

        latest_commit = "No git history"


    readme = ""

    readme_file = path / "README.md"

    if readme_file.exists():

        readme = readme_file.read_text(
            encoding="utf-8"
        )


    return {
        "name": path.name,
        "files": files,
        "latest_commit": latest_commit,
        "readme": readme
    }
