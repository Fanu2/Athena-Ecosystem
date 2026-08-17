from dataclasses import dataclass


@dataclass
class Preference:

    key: str

    value: str

    category: str = "general"
