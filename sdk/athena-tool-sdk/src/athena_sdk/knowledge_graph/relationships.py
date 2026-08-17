from .models import (
    KnowledgeEdge,
)


def link_sources(
    source_node,
    target_node,
    relation="related_to"
):

    return KnowledgeEdge(

        source=source_node.id,

        target=target_node.id,

        relation=relation
    )
