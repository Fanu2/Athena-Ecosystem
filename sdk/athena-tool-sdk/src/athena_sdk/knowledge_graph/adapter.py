from .models import (
    KnowledgeNode,
)


def akp_to_node(
    akp: dict
):

    return KnowledgeNode(

        id=str(
            akp.get(
                "id",
                akp.get(
                    "title",
                    "unknown"
                )
            )
        ),

        node_type=akp.get(
            "source",
            {}
        ).get(
            "type",
            "knowledge"
        ),

        title=akp.get(
            "title",
            "Untitled"
        ),

        metadata={
            "source": akp.get(
                "source",
                {}
            )
        }
    )
