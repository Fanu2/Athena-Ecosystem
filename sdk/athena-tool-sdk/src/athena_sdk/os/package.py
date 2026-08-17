from dataclasses import dataclass, field


@dataclass
class RuntimePackage:

    name: str

    version: str

    components: list[str] = field(
        default_factory=list
    )


class PackageBuilder:


    def __init__(self):

        self.packages = []


    def create(
        self,
        package: RuntimePackage
    ):

        self.packages.append(
            package
        )

        return package


    def list(self):

        return self.packages
