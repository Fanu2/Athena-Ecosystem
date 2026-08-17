from athena_sdk.assistant import (
    route_request,
    create_plan,
)


def test_git_plan():

    intent = route_request(
        "Analyze my Git repository"
    )

    plan = create_plan(
        intent
    )

    assert len(
        plan.steps
    ) == 1

    assert (
        plan.steps[0].capability
        == "repository_analysis"
    )
