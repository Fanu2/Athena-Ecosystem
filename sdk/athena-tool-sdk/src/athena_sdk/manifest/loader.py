from pathlib import Path
import yaml

from .models import ToolManifest


def load_manifest(
    path: str
) -> ToolManifest:
    """
    Load tool_manifest.yaml
    """

    file = Path(path)

    with file.open(
        "r",
        encoding="utf-8"
    ) as f:
        data = yaml.safe_load(f)

    return ToolManifest(**data)
