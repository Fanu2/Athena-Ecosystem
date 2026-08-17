from athena_sdk.os import (
    BackupManager,
    BackupManifest,
)


def test_backup_restore():

    manager = BackupManager()


    manager.create(
        BackupManifest(
            name="athena_backup",
            version="1.0",
            components=[
                "workspace",
                "plugins"
            ]
        )
    )


    result = manager.restore_check(
        "athena_backup"
    )


    assert (
        result["status"]
        ==
        "available"
    )


    assert len(
        manager.list()
    ) == 1
