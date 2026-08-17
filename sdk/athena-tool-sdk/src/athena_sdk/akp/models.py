from dataclasses import dataclass, field
from typing import Any


@dataclass
class KnowledgePackage:
    """
    Athena Knowledge Package (AKP) v1.0
    """

    title: str
    content: str
    source: dict[str, Any]
    confidence: dict[str, Any]
    evidence: dict[str, Any]

    akp_version: str = "1.0"
    knowledge_type: str = "document"

    provenance: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
