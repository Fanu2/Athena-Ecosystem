from .models import (
    KnowledgeEdge,
)


RELATION_WORDS = {
    "uses": "uses",
    "using": "uses",
    "contains": "contains",
    "includes": "contains",
    "belongs": "belongs_to",
}


def discover_relationships(
    entities,
    text: str
):

    edges = []

    words = text.lower().split()


    relation = None

    for word in words:

        clean = word.strip(
            ".,!?()[]{}"
        )

        if clean in RELATION_WORDS:

            relation = RELATION_WORDS[
                clean
            ]

            break


    if not relation:

        return edges


    if len(entities) >= 2:

        edges.append(
            KnowledgeEdge(

                source=entities[0].name,

                target=entities[1].name,

                relation=relation
            )
        )


    return edges
