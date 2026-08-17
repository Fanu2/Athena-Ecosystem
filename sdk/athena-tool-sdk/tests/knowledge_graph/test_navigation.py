from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
    build_path,
)


def test_navigation():

    graph = KnowledgeGraph()


    answer = KnowledgeNode(
        id="answer",
        node_type="answer",
        title="Answer"
    )

    evidence = KnowledgeNode(
        id="evidence",
        node_type="evidence",
        title="Evidence"
    )


    graph.add_node(
        answer
    )

    graph.add_node(
        evidence
    )


    graph.add_edge(
        KnowledgeEdge(
            source="answer",
            target="evidence",
            relation="supported_by"
        )
    )


    path = build_path(
        graph,
        "answer"
    )


    assert (
        "evidence"
        in path
    )
