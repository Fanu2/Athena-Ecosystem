from .models import (
    KnowledgeNode,
    KnowledgeEdge,
)


def create_evidence_node(
    evidence_id: str,
    title: str,
    source_type: str
):

    return KnowledgeNode(

        id=evidence_id,

        node_type="evidence",

        title=title,

        metadata={
            "source_type": source_type
        }
    )


def link_evidence(
    answer_node,
    evidence_node
):

    return KnowledgeEdge(

        source=answer_node.id,

        target=evidence_node.id,

        relation="supported_by"
    )
