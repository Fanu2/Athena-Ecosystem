from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
)

from athena_sdk.assistant import (
    build_graph_context,
)


def test_graph_context():

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
            title="Evidence"
        )
    )


    graph.add_edge(
        KnowledgeEdge(
            source="answer",
            target="evidence",
            relation="supported_by"
        )
    )


    context = build_graph_context(
        graph,
        "answer"
    )


    assert (
        "evidence"
        in context
    )
