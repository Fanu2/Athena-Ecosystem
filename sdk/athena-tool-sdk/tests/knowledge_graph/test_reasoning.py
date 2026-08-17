from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
    evaluate_evidence_path,
)


def test_evidence_reasoning():

    graph = KnowledgeGraph()


    graph.add_node(
        KnowledgeNode(
            id="answer",
            node_type="answer",
            title="Answer"
        )
    )


    graph.add_node(
        KnowledgeNode(
            id="evidence",
            node_type="evidence",
            title="Citation"
        )
    )


    graph.add_edge(
        KnowledgeEdge(
            source="answer",
            target="evidence",
            relation="supported_by"
        )
    )


    result = evaluate_evidence_path(
        graph,
        "answer"
    )


    assert (
        result.score
        == 1.0
    )


    assert (
        "Evidence"
        in result.explanation
    )
