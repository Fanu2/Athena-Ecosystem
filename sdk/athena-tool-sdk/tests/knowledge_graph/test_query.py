from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
    search_nodes,
    related_nodes,
)


def test_graph_query():

    graph = KnowledgeGraph()


    graph.add_node(
        KnowledgeNode(
            id="athena",
            node_type="project",
            title="Project Athena"
        )
    )


    graph.add_node(
        KnowledgeNode(
            id="python",
            node_type="technology",
            title="Python"
        )
    )


    graph.add_edge(
        KnowledgeEdge(
            source="athena",
            target="python",
            relation="uses"
        )
    )


    result = search_nodes(
        graph,
        "Athena"
    )


    assert len(result) == 1


    related = related_nodes(
        graph,
        "athena"
    )


    assert (
        "python"
        in related
    )
