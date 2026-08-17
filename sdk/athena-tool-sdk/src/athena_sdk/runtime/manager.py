import subprocess

from .models import (
    ExecutionResult
)


class PluginRuntime:
    """
    Athena Plugin Runtime Manager.
    """

    def execute(
        self,
        command: list[str],
        tool_name: str
    ) -> ExecutionResult:

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )

            return ExecutionResult(
                tool=tool_name,
                status="success",
                output=result.stdout
            )


        except subprocess.CalledProcessError as error:

            return ExecutionResult(
                tool=tool_name,
                status="failed",
                output=error.stderr
            )
