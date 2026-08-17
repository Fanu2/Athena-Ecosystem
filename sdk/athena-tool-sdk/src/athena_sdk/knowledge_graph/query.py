def find_nodes_by_type(
    graph,
    node_type: str
):

    return [
        node
        for node in graph.nodes
        if node.node_type == node_type
    ]



def find_node_by_id(
    graph,
    node_id: str
):

    for node in graph.nodes:

        if node.id == node_id:

            return node

    return None



def search_nodes(
    graph,
    text: str
):

    text = text.lower()

    return [
        node
        for node in graph.nodes
        if text in node.title.lower()
    ]



def related_nodes(
    graph,
    node_id: str
):

    results = []

    for edge in graph.edges:

        if edge.source == node_id:

            results.append(
                edge.target
            )

        elif edge.target == node_id:

            results.append(
                edge.source
            )

    return results
