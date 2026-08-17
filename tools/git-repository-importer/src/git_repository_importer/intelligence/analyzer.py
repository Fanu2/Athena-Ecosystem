from pathlib import Path
from collections import Counter


def analyze_repository(
    repo_path: str
) -> dict:

    path = Path(repo_path)

    files = [
        p for p in path.rglob("*")
        if p.is_file()
    ]

    extensions = Counter(
        p.suffix.lower()
        for p in files
    )

    directories = set()

    for file in files:
        directories.add(
            str(file.parent.relative_to(path))
        )

    return {
        "total_files": len(files),
        "extensions": dict(extensions),
        "directories": sorted(
            directories
        )
    }
