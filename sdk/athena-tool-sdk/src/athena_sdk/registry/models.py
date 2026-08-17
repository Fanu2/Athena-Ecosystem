from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolRegistryEntry:
    """
    Athena Tool Registry Entry.
    """

    name: str

    version: str

    description: str

    path: str

    akp_versions: list[str] = field(
        default_factory=list
    )

    permissions: dict[str, Any] = field(
        default_factory=dict
    )
