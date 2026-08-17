from athena_sdk.personal import (
    Workflow,
    WorkflowStep,
)


def test_workflow():

    workflow = Workflow(
        "Weekly Athena Review"
    )


    workflow.add_step(
        WorkflowStep(
            name="collect",
            action="workspace_search"
        )
    )


    workflow.add_step(
        WorkflowStep(
            name="summarize",
            action="assistant_response"
        )
    )


    assert len(
        workflow.steps
    ) == 2


    assert (
        workflow.steps[0].action
        ==
        "workspace_search"
    )
