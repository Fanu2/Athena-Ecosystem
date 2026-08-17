from dataclasses import dataclass, field


@dataclass
class Workspace:

    name: str

    description: str = ""

    knowledge: list[str] = field(
        default_factory=list
    )


    def add_knowledge(
        self,
        item: str
    ):

        self.knowledge.append(
            item
        )
