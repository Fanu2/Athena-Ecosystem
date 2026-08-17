from athena_sdk.workspace import (
    search_workspace,
)


def build_workspace_context(
    workspace,
    request: str
):

    results = search_workspace(
        workspace,
        request
    )

    return [
        result.item
        for result in results
    ]
