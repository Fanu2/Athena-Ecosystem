from dataclasses import dataclass, field


@dataclass
class KnowledgeNode:

    id: str

    node_type: str

    title: str

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class KnowledgeEdge:

    source: str

    target: str

    relation: str


@dataclass
class KnowledgeGraph:

    nodes: list[KnowledgeNode] = field(
        default_factory=list
    )

    edges: list[KnowledgeEdge] = field(
        default_factory=list
    )


    def add_node(
        self,
        node: KnowledgeNode
    ):

        self.nodes.append(
            node
        )


    def add_edge(
        self,
        edge: KnowledgeEdge
    ):

        self.edges.append(
            edge
        )
