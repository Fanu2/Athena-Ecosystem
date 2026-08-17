from athena_sdk.assistant import (
    execute_request,
    compose_response,
)


def test_response_composer():

    result = execute_request(
        "Analyze my Git repository"
    )

    response = compose_response(
        result
    )

    assert (
        response.status
        == "success"
    )

    assert (
        "git"
        in response.tool
    )
