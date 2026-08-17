from athena_sdk.automation import (
    AutomationTask,
    TaskQueue,
)


def test_task_queue():

    queue = TaskQueue()


    queue.add(
        AutomationTask(
            name="index_docs",
            workflow="Document Index"
        )
    )


    task = queue.next()


    assert (
        task.name
        ==
        "index_docs"
    )


    queue.complete(
        task
    )


    assert (
        task.status
        ==
        "completed"
    )
