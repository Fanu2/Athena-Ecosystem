from dataclasses import dataclass, field


@dataclass
class MemoryRecord:

    category: str

    key: str

    value: str



class AssistantMemory:


    def __init__(self):

        self.records = []


    def remember(
        self,
        category: str,
        key: str,
        value: str
    ):

        self.records.append(
            MemoryRecord(
                category=category,
                key=key,
                value=value
            )
        )


    def recall(
        self,
        category: str
    ):

        return [
            record
            for record in self.records
            if record.category == category
        ]
