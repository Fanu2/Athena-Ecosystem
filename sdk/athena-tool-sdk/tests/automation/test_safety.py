from athena_sdk.automation import (
    AutomationTask,
    AutomationPolicy,
    SafeAutomationEngine,
)


def test_safe_automation():

    task = AutomationTask(
        name="backup_workspace",
        workflow="Backup"
    )


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
