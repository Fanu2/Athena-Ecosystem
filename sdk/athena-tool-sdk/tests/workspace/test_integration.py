from athena_sdk.workspace import (
    Workspace,
    search_workspace,
    mark_important,
    rank_memory,
)

from athena_sdk.assistant import (
    build_memory_context,
)


def test_workspace_full_flow():

    ws = Workspace(
        "Athena Workspace"
    )


    ws.add_knowledge(
        "Git Repository Intelligence"
    )

    ws.add_knowledge(
        "ChatGPT Conversation Archive"
    )


    mark_important(
        ws.memories[0]
    )


    search = search_workspace(
        ws,
        "Git"
    )


    assert len(search) == 1


    ranked = rank_memory(
        ws.memories
    )


    assert (
        ranked[0].content
        ==
        "Git Repository Intelligence"
    )


    context = build_memory_context(
        ws
    )


    assert (
        "Git Repository Intelligence"
        in context
    )
