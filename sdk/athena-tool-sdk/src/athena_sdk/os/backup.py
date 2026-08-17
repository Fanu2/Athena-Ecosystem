from dataclasses import dataclass, field


@dataclass
class BackupManifest:

    name: str

    version: str

    components: list[str] = field(
        default_factory=list
    )



class BackupManager:


    def __init__(self):

        self.backups = []


    def create(
        self,
        manifest: BackupManifest
    ):

        self.backups.append(
            manifest
        )

        return manifest


    def restore_check(
        self,
        name: str
    ):

        for backup in self.backups:

            if backup.name == name:

                return {
                    "status": "available",
                    "backup": backup
                }


        return {
            "status": "missing"
        }


    def list(self):

        return self.backups
