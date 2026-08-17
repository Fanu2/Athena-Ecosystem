from athena_sdk.workspace import (
    Workspace,
    search_workspace,
)


def test_workspace_search():

    ws = Workspace(
        "Athena"
    )

    ws.add_knowledge(
        "Git Repository Analysis"
    )

    ws.add_knowledge(
        "ChatGPT Conversation Archive"
    )


    results = search_workspace(
        ws,
        "Git"
    )


    assert len(results) == 1

    assert (
        results[0].item
        ==
        "Git Repository Analysis"
    )

    assert (
        results[0].score
        == 1.0
    )
