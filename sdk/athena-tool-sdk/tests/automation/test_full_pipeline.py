from athena_sdk.automation import (
    WorkflowScheduler,
    ScheduledTask,
    TriggerRegistry,
    EventTrigger,
    TaskQueue,
    AutomationTask,
    AutomationPolicy,
    SafeAutomationEngine,
)


def test_automation_pipeline():

    # Scheduler

    scheduler = WorkflowScheduler()

    scheduler.add(
        ScheduledTask(
            name="daily_sync",
            workflow="Workspace Sync",
            schedule="daily"
        )
    )


    assert len(
        scheduler.list()
    ) == 1


    # Trigger

    triggers = TriggerRegistry()

    triggers.add(
        EventTrigger(
            event="document_added",
            workflow="Index Workspace"
        )
    )


    assert len(
        triggers.find(
            "document_added"
        )
    ) == 1


    # Queue

    queue = TaskQueue()

    queue.add(
        AutomationTask(
            name="sync",
            workflow="Workspace Sync"
        )
    )


    task = queue.next()


    assert (
        task.status
        ==
        "pending"
    )


    # Safety

    engine = SafeAutomationEngine(
        AutomationPolicy(
            allowed=True
        )
    )


    result = engine.validate(
        task
    )


    assert (
        result["status"]
        ==
        "approved"
    )
