from athena_sdk.assistant import (
    execute_request
)


def test_assistant_pipeline():

    response = execute_request(
        "Analyze my Git repository"
    )

    assert (
        len(response["results"])
        == 1
    )

    assert (
        response["results"][0]["tool"]
        ==
        "athena-git-repository-importer"
    )
