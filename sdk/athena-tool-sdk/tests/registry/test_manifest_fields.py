import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.registry import (
    scan_tools
)


def test_manifest_fields():

    tools = scan_tools(
        "tools"
    )

    for tool in tools:

        assert tool.name
        assert tool.version
        assert tool.path

        assert (
            "1.0"
            in tool.akp_versions
        )
