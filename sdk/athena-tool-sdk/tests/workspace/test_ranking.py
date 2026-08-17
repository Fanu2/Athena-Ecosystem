from athena_sdk.workspace import (
    Workspace,
    mark_accessed,
    mark_important,
    rank_memory,
)


def test_memory_ranking():

    ws = Workspace(
        "Athena"
    )

    ws.add_knowledge(
        "Normal Document"
    )

    ws.add_knowledge(
        "Important Architecture"
    )

    important = ws.memories[1]

    mark_important(
        important
    )

    normal = ws.memories[0]

    mark_accessed(
        normal
    )


    ranked = rank_memory(
        ws.memories
    )


    assert (
        ranked[0].content
        ==
        "Important Architecture"
    )
