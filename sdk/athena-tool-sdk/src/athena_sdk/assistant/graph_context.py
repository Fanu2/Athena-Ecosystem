from athena_sdk.knowledge_graph import (
    build_path,
)


def build_graph_context(
    graph,
    node_id: str,
    depth: int = 1
):

    path = build_path(
        graph,
        node_id,
        depth
    )

    return path
