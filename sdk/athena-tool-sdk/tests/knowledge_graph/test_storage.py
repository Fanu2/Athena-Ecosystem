from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
    save_graph,
    load_graph,
)


def test_graph_storage(
    tmp_path
):

    file = tmp_path / "graph.json"


    graph = KnowledgeGraph()


    graph.add_node(
        KnowledgeNode(
            id="athena",
            node_type="project",
            title="Athena"
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


    save_graph(
        graph,
        file
    )


    loaded = load_graph(
        file
    )


    assert len(
        loaded.nodes
    ) == 2


    assert len(
        loaded.edges
    ) == 1
