from athena_sdk.automation import (
    WorkflowScheduler,
    ScheduledTask,
)


def test_scheduler():

    scheduler = WorkflowScheduler()


    scheduler.add(
        ScheduledTask(
            name="daily_review",
            workflow="Athena Review",
            schedule="daily"
        )
    )


    task = scheduler.find(
        "daily_review"
    )


    assert task.workflow == "Athena Review"

    assert len(
        scheduler.list()
    ) == 1
