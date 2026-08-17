from athena_sdk.registry import (
    scan_tools,
    find_by_capability,
)


def select_tool(
    capability: str
):

    tools = scan_tools(
        "tools"
    )

    matches = find_by_capability(
        tools,
        capability
    )

    if not matches:

        raise LookupError(
            f"No tool found for {capability}"
        )

    return matches[0]
