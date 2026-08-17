from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolManifest:
    """
    Athena Tool Manifest v1.0
    """

    name: str
    version: str
    description: str

    akp_versions: list[str] = field(
        default_factory=lambda: ["1.0"]
    )

    permissions: dict[str, Any] = field(
        default_factory=dict
    )
