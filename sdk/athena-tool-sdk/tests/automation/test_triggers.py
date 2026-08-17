from athena_sdk.automation import (
    EventTrigger,
    TriggerRegistry,
)


def test_event_trigger():

    registry = TriggerRegistry()


    registry.add(
        EventTrigger(
            event="document_imported",
            workflow="Index Workspace"
        )
    )


    result = registry.find(
        "document_imported"
    )


    assert len(result) == 1

    assert (
        result[0].workflow
        ==
        "Index Workspace"
    )
