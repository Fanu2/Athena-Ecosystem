from athena_sdk.workspace import (
    Workspace,
)

from athena_sdk.assistant import (
    build_workspace_context,
)


def test_workspace_context():

    ws = Workspace(
        "Athena"
    )

    ws.add_knowledge(
        "Git Repository Analysis"
    )

    ws.add_knowledge(
        "ChatGPT Archive"
    )


    context = build_workspace_context(
        ws,
        "Git"
    )


    assert (
        "Git Repository Analysis"
        in context
    )
