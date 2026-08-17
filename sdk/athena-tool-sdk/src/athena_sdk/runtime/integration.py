from athena_sdk.registry import (
    scan_tools,
    find_by_capability,
)

from .executor import (
    run_plugin
)


def execute_capability(
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
            f"No plugin found: {capability}"
        )

    tool = matches[0]

    return run_plugin(
        tool
    )
