from dataclasses import dataclass, field


@dataclass
class ModelInfo:

    name: str

    provider: str

    model_type: str

    capabilities: list[str] = field(
        default_factory=list
    )



class ModelRegistry:


    def __init__(self):

        self.models = []


    def add(
        self,
        model: ModelInfo
    ):

        self.models.append(
            model
        )


    def find(
        self,
        capability: str
    ):

        return [
            model
            for model in self.models
            if capability
            in model.capabilities
        ]


    def all(self):

        return self.models
