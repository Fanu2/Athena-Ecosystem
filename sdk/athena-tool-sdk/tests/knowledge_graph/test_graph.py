from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
)


def test_graph():

    graph = KnowledgeGraph()


    project = KnowledgeNode(
        id="project-athena",
        node_type="project",
        title="Project Athena"
    )


    repo = KnowledgeNode(
        id="git-athena",
        node_type="repository",
        title="Athena Repository"
    )


    graph.add_node(
        project
    )

    graph.add_node(
        repo
    )


    graph.add_edge(
        KnowledgeEdge(
            source="git-athena",
            target="project-athena",
            relation="belongs_to"
        )
    )


    assert len(
        graph.nodes
    ) == 2


    assert len(
        graph.edges
    ) == 1
