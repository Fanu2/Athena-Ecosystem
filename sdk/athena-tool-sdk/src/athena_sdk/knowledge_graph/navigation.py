def find_related_nodes(
    graph,
    node_id: str
):

    related = []

    for edge in graph.edges:

        if edge.source == node_id:

            related.append(
                edge.target
            )

        elif edge.target == node_id:

            related.append(
                edge.source
            )

    return related



def build_path(
    graph,
    start_id: str,
    depth: int = 1
):

    visited = set()

    frontier = [
        start_id
    ]

    for _ in range(depth + 1):

        next_nodes = []

        for node in frontier:

            if node in visited:
                continue

            visited.add(
                node
            )

            next_nodes.extend(
                find_related_nodes(
                    graph,
                    node
                )
            )

        frontier = next_nodes


    return list(
        visited
    )
