from athena_sdk.workspace import (
    rank_memory,
)


def build_memory_context(
    workspace,
    limit: int = 5
):

    ranked = rank_memory(
        workspace.memories
    )

    return [
        item.content
        for item in ranked[:limit]
    ]
