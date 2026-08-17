from athena_sdk.runtime import (
    execute_capability
)


def test_capability_execution():

    result = execute_capability(
        "repository_analysis"
    )

    assert (
        result["result"].status
        == "success"
    )

    assert (
        result["provenance"]["tool"]
        == "athena-git-repository-importer"
    )
