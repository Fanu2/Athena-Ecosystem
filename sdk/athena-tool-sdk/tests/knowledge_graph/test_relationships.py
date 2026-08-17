from athena_sdk.knowledge_graph import (
    akp_to_node,
    link_sources,
)


def test_cross_source_link():

    chat = akp_to_node(
        {
            "title":
                "ChatGPT Discussion",
            "source":
                {
                    "type":
                        "conversation"
                }
        }
    )


    git = akp_to_node(
        {
            "title":
                "Athena Repository",
            "source":
                {
                    "type":
                        "repository"
                }
        }
    )


    edge = link_sources(
        chat,
        git,
        "references"
    )


    assert (
        edge.relation
        ==
        "references"
    )

    assert (
        edge.source
        ==
        chat.id
    )
