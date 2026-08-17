from athena_sdk.workspace import (
    Workspace,
    import_akp_workspace,
)


def test_akp_import():

    ws = Workspace(
        "Test Workspace"
    )

    result = import_akp_workspace(
        ws,
        "examples/workspace-akp-test"
    )

    assert (
        result["status"]
        == "success"
    )

    assert (
        result["imported"]
        == 1
    )

    assert (
        "Athena Sample Knowledge"
        in ws.knowledge
    )
