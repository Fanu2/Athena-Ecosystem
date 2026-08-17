from dataclasses import dataclass


@dataclass
class AutomationPolicy:

    allowed: bool = False



class SafeAutomationEngine:


    def __init__(
        self,
        policy: AutomationPolicy
    ):

        self.policy = policy


    def can_execute(self):

        return self.policy.allowed


    def validate(
        self,
        task
    ):

        if self.can_execute():

            return {
                "status": "approved",
                "task": task.name
            }


        return {
            "status": "blocked",
            "task": task.name
        }
