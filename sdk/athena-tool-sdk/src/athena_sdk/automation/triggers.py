from dataclasses import dataclass


@dataclass
class EventTrigger:

    event: str

    workflow: str



class TriggerRegistry:


    def __init__(self):

        self.triggers = []


    def add(
        self,
        trigger: EventTrigger
    ):

        self.triggers.append(
            trigger
        )


    def find(
        self,
        event: str
    ):

        return [
            trigger
            for trigger in self.triggers
            if trigger.event == event
        ]
