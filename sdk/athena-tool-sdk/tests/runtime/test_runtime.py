from athena_sdk.runtime import (
    PluginRuntime,
    validate_command,
)


def test_runtime():

    validate_command(
        ["echo", "Athena"]
    )

    runtime = PluginRuntime()

    result = runtime.execute(
        [
            "echo",
            "Athena Runtime"
        ],
        "test-plugin"
    )

    assert result.status == "success"
    assert "Athena Runtime" in result.output
