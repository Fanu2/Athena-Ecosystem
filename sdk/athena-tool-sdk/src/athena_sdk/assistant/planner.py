from dataclasses import dataclass, field


@dataclass
class PlanStep:

    action: str

    capability: str


@dataclass
class ExecutionPlan:

    steps: list[PlanStep] = field(
        default_factory=list
    )


def create_plan(
    intent
):

    return ExecutionPlan(
        steps=[
            PlanStep(
                action="execute_plugin",
                capability=intent.capability
            )
        ]
    )
