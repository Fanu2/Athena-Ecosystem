from athena_sdk.personal import (
    Preference,
    PreferenceStore,
    ContextContinuity,
    Workflow,
    WorkflowStep,
    AssistantMemory,
)


def test_personal_intelligence_pipeline():

    # Preference layer
    preferences = PreferenceStore()

    preferences.add(
        Preference(
            key="response_style",
            value="developer",
            category="assistant"
        )
    )

    assert (
        preferences.get(
            "response_style"
        ).value
        ==
        "developer"
    )


    # Context continuity layer
    context = ContextContinuity()

    context.remember(
        "project",
        "Athena"
    )

    assert (
        context.recall(
            "project"
        )[0].value
        ==
        "Athena"
    )


    # Workflow layer
    workflow = Workflow(
        "Athena Review"
    )

    workflow.add_step(
        WorkflowStep(
            name="collect",
            action="workspace_search"
        )
    )

    assert (
        len(workflow.steps)
        ==
        1
    )


    # Assistant memory layer
    memory = AssistantMemory()

    memory.remember(
        "context",
        "active_project",
        "Athena"
    )

    result = memory.recall(
        "context"
    )

    assert (
        result[0].value
        ==
        "Athena"
    )
