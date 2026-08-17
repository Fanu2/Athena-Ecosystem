from dataclasses import dataclass, field


@dataclass
class WorkflowStep:

    name: str

    action: str



@dataclass
class Workflow:

    name: str

    steps: list[WorkflowStep] = field(
        default_factory=list
    )


    def add_step(
        self,
        step: WorkflowStep
    ):

        self.steps.append(
            step
        )
