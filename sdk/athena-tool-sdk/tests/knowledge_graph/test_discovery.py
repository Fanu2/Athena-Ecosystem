from athena_sdk.knowledge_graph import (
    extract_entities,
    discover_relationships,
)


def test_relationship_discovery():

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


    assert len(edges) == 1


    assert (
        edges[0].relation
        ==
        "uses"
    )
