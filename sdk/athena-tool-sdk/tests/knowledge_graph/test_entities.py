from athena_sdk.knowledge_graph import (
    extract_entities,
)


def test_entity_extraction():

    entities = extract_entities(
        "Project Athena uses Python"
    )


    names = [
        entity.name
        for entity in entities
    ]


    assert (
        "Project"
        in names
    )


    assert (
        "Athena"
        in names
    )
