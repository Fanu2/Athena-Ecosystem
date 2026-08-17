from dataclasses import dataclass


@dataclass
class ScheduledTask:

    name: str

    workflow: str

    schedule: str



class WorkflowScheduler:


    def __init__(self):

        self.tasks = []


    def add(
        self,
        task: ScheduledTask
    ):

        self.tasks.append(
            task
        )


    def list(self):

        return self.tasks


    def find(
        self,
        name: str
    ):

        for task in self.tasks:

            if task.name == name:

                return task

        return None
