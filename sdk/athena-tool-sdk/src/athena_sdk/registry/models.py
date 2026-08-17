from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolRegistryEntry:

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

    capabilities: list[str] = field(
        default_factory=list
    )

    inputs: list[str] = field(
        default_factory=list
    )

    outputs: list[str] = field(
        default_factory=list
    )

    state: str = "verified"
