from dataclasses import dataclass, field

from .memory import (
    MemoryItem
)


@dataclass
class Workspace:

    name: str

    description: str = ""

    knowledge: list[str] = field(
        default_factory=list
    )

    memories: list[MemoryItem] = field(
        default_factory=list
    )


    def add_knowledge(
        self,
        item: str
    ):

        self.knowledge.append(
            item
        )

        self.memories.append(
            MemoryItem(
                content=item
            )
        )
