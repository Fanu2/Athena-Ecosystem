from dataclasses import dataclass, field


@dataclass
class ModelProfile:

    name: str

    provider: str

    context_size: int

    memory_requirement: str

    speed: str

    specialization: list[str] = field(
        default_factory=list
    )
