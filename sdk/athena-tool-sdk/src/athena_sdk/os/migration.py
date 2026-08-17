from dataclasses import dataclass, field


@dataclass
class MigrationManifest:

    workspace: str

    version: str

    components: list[str] = field(
        default_factory=list
    )



class WorkspaceMigration:


    def __init__(self):

        self.manifests = []


    def create(
        self,
        manifest: MigrationManifest
    ):

        self.manifests.append(
            manifest
        )

        return manifest


    def validate(
        self,
        workspace: str
    ):

        for manifest in self.manifests:

            if manifest.workspace == workspace:

                return {
                    "status": "ready",
                    "manifest": manifest
                }


        return {
            "status": "missing"
        }


    def list(self):

        return self.manifests
