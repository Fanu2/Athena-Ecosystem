from athena_sdk.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
    extract_entities,
    discover_relationships,
    save_graph,
    load_graph,
    search_nodes,
    evaluate_evidence_path,
)


def test_full_knowledge_pipeline(
    tmp_path
):

    text = (
        "Athena uses Python"
    )


    entities = extract_entities(
        text
    )


    edges = discover_relationships(
        entities,
        text
    )


    graph = KnowledgeGraph()


    for entity in entities:

        graph.add_node(
            KnowledgeNode(
                id=entity.name,
                node_type=entity.entity_type,
                title=entity.name,
            )
        )


    for edge in edges:

        graph.add_edge(
            edge
        )


    answer = KnowledgeNode(
        id="answer",
        node_type="answer",
        title="Athena Answer"
    )


    evidence = KnowledgeNode(
        id="evidence",
        node_type="evidence",
        title="Source Evidence"
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


    file = tmp_path / "graph.json"


    save_graph(
        graph,
        file
    )


    restored = load_graph(
        file
    )


    results = search_nodes(
        restored,
        "Athena"
    )


    assert len(results) >= 1


    score = evaluate_evidence_path(
        restored,
        "answer"
    )


    assert (
        score.score
        == 1.0
    )
