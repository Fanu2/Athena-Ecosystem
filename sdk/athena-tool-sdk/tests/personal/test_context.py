from athena_sdk.personal import (
    ContextContinuity,
)


def test_context_continuity():

    context = ContextContinuity()


    context.remember(
        "project",
        "Athena"
    )


    result = context.recall(
        "project"
    )


    assert len(result) == 1

    assert (
        result[0].value
        ==
        "Athena"
    )
