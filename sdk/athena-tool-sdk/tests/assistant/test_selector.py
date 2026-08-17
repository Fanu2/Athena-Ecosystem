from athena_sdk.assistant import (
    select_tool
)


def test_select_git_tool():

    tool = select_tool(
        "repository_analysis"
    )

    assert (
        tool.name
        ==
        "athena-git-repository-importer"
    )


def test_select_conversation_tool():

    tool = select_tool(
        "conversation_import"
    )

    assert (
        "importer"
        in tool.name
    )
