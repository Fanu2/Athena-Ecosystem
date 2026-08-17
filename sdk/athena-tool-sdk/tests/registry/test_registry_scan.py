from pathlib import Path
import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.registry import (
    scan_tools
)


def test_registry_scan():

    tools = scan_tools(
        "tools"
    )

    names = [
        tool.name
        for tool in tools
    ]

    assert (
        "athena-git-repository-importer"
        in names
    )

    assert len(tools) >= 5
