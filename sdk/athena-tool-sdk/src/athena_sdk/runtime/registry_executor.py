from athena_sdk.runtime import (
    PluginRuntime
)


def execute_tool(
    tool
):

    runtime = PluginRuntime()

    return runtime.execute(
        tool.command,
        tool.name
    )
