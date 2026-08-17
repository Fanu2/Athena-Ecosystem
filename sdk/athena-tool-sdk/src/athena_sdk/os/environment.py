from dataclasses import dataclass, field


@dataclass
class EnvironmentInfo:

    name: str

    version: str

    components: list[str] = field(
        default_factory=list
    )



class EnvironmentManager:


    def __init__(self):

        self.environments = []


    def register(
        self,
        environment: EnvironmentInfo
    ):

        self.environments.append(
            environment
        )


    def find(
        self,
        name: str
    ):

        for environment in self.environments:

            if environment.name == name:

                return environment


        return None


    def list(self):

        return self.environments
