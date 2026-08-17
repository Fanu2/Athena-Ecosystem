import json

from .models import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeEdge,
)


def save_graph(
    graph,
    path: str
):

    data = {

        "nodes": [
            {
                "id": node.id,
                "type": node.node_type,
                "title": node.title,
                "metadata": node.metadata,
            }

            for node in graph.nodes
        ],

        "edges": [
            {
                "source": edge.source,
                "target": edge.target,
                "relation": edge.relation,
            }

            for edge in graph.edges
        ],
    }


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=2
        )



def load_graph(
    path: str
):

    graph = KnowledgeGraph()


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(
            file
        )


    for node in data["nodes"]:

        graph.add_node(
            KnowledgeNode(
                id=node["id"],
                node_type=node["type"],
                title=node["title"],
                metadata=node["metadata"],
            )
        )


    for edge in data["edges"]:

        graph.add_edge(
            KnowledgeEdge(
                source=edge["source"],
                target=edge["target"],
                relation=edge["relation"],
            )
        )


    return graph
