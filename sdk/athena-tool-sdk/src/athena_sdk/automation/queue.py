from dataclasses import dataclass


@dataclass
class AutomationTask:

    name: str

    workflow: str

    status: str = "pending"



class TaskQueue:


    def __init__(self):

        self.tasks = []


    def add(
        self,
        task: AutomationTask
    ):

        self.tasks.append(
            task
        )


    def next(
        self
    ):

        for task in self.tasks:

            if task.status == "pending":

                return task

        return None


    def complete(
        self,
        task: AutomationTask
    ):

        task.status = "completed"
