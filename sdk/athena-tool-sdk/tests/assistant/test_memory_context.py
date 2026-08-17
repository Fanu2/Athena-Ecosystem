from athena_sdk.workspace import (
    Workspace,
    mark_important,
)

from athena_sdk.assistant import (
    build_memory_context,
)


def test_memory_context():

    ws = Workspace(
        "Athena"
    )

    ws.add_knowledge(
        "Project Architecture"
    )

    ws.add_knowledge(
        "Random Note"
    )

    mark_important(
        ws.memories[0]
    )

    context = build_memory_context(
        ws
    )


    assert (
        "Project Architecture"
        in context
    )
