from dataclasses import dataclass


@dataclass
class AssistantIntent:

    action: str

    capability: str

    input_type: str | None = None
