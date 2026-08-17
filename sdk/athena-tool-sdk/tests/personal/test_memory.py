from athena_sdk.personal import (
    AssistantMemory,
)


def test_assistant_memory():

    memory = AssistantMemory()


    memory.remember(
        "preference",
        "style",
        "developer"
    )


    memory.remember(
        "context",
        "project",
        "Athena"
    )


    result = memory.recall(
        "preference"
    )


    assert len(result) == 1


    assert (
        result[0].value
        ==
        "developer"
    )
