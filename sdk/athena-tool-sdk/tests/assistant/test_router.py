from athena_sdk.assistant import (
    route_request
)


def test_messenger_route():

    intent = route_request(
        "Import my Messenger archive"
    )

    assert (
        intent.capability
        == "conversation_import"
    )


def test_git_route():

    intent = route_request(
        "Analyze my Git repository"
    )

    assert (
        intent.capability
        == "repository_analysis"
    )
