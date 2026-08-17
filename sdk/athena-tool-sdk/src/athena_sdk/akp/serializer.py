import json
from dataclasses import asdict
from pathlib import Path

from .models import KnowledgePackage


def serialize(
    package: KnowledgePackage,
    output_path: str
) -> None:
    """
    Serialize AKP package to JSON.
    """

    path = Path(output_path)

    with path.open(
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            asdict(package),
            f,
            indent=2,
            ensure_ascii=False
        )


def deserialize(
    input_path: str
) -> KnowledgePackage:
    """
    Deserialize AKP package from JSON.
    """

    path = Path(input_path)

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    return KnowledgePackage(**data)
