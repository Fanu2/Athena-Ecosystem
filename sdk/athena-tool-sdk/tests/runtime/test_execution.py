from types import SimpleNamespace

from athena_sdk.runtime import (
    run_plugin
)


def test_plugin_execution():

    tool = SimpleNamespace(
        name="test-plugin",
        state="verified",
        command=[
            "echo",
            "Athena"
        ]
    )

    result = run_plugin(
        tool
    )

    assert (
        result["result"].status
        == "success"
    )

    assert (
        result["provenance"]["tool"]
        == "test-plugin"
    )
