from athena_sdk.knowledge_graph import (
    KnowledgeNode,
    create_evidence_node,
    link_evidence,
)


def test_evidence_relationship():

    answer = KnowledgeNode(
        id="answer-001",
        node_type="answer",
        title="Athena response"
    )

    evidence = create_evidence_node(
        "evidence-001",
        "README citation",
        "document"
    )

    edge = link_evidence(
        answer,
        evidence
    )

    assert (
        edge.relation
        ==
        "supported_by"
    )

    assert (
        edge.source
        ==
        "answer-001"
    )

    assert (
        edge.target
        ==
        "evidence-001"
    )
