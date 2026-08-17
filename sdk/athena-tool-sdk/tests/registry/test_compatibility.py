import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.registry import (
    scan_tools,
    supports_akp
)


def test_akp_support():

    tools = scan_tools(
        "tools"
    )

    for tool in tools:

        assert supports_akp(
            tool,
            "1.0"
        )
