from .manager import PluginRuntime
from .security import (
    validate_plugin_execution
)

from .provenance import (
    create_execution_record
)


def run_plugin(
    tool
):

    validate_plugin_execution(
        tool
    )

    runtime = PluginRuntime()

    result = runtime.execute(
        tool.command,
        tool.name
    )

    record = create_execution_record(
        tool,
        result
    )

    return {
        "result": result,
        "provenance": record
    }
