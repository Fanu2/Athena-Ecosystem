from athena_sdk.workspace import (
    Workspace
)


def test_workspace():

    ws = Workspace(
        "Athena Project"
    )

    ws.add_knowledge(
        "repository.akp.json"
    )

    assert (
        len(ws.knowledge)
        == 1
    )

    assert (
        ws.name
        == "Athena Project"
    )
