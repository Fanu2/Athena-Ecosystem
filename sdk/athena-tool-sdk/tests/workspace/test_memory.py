from athena_sdk.workspace import (
    Workspace,
    mark_accessed,
    mark_important,
)


def test_memory():

    ws = Workspace(
        "Athena"
    )

    ws.add_knowledge(
        "Project Architecture"
    )

    item = ws.memories[0]

    mark_accessed(
        item
    )

    mark_important(
        item
    )

    assert (
        item.access_count
        == 1
    )

    assert (
        item.important
        is True
    )
