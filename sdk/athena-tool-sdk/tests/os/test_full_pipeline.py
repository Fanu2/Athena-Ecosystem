from athena_sdk.os import (
    EnvironmentManager,
    EnvironmentInfo,
    PackageBuilder,
    RuntimePackage,
    BackupManager,
    BackupManifest,
    WorkspaceMigration,
    MigrationManifest,
)


def test_athena_os_pipeline():

    # Environment

    environment = EnvironmentManager()

    environment.register(
        EnvironmentInfo(
            name="Athena Portable",
            version="1.0",
            components=[
                "sdk",
                "plugins"
            ]
        )
    )


    assert (
        environment.find(
            "Athena Portable"
        ).version
        ==
        "1.0"
    )


    # Packaging

    builder = PackageBuilder()

    builder.create(
        RuntimePackage(
            name="Athena Runtime",
            version="1.0",
            components=[
                "models"
            ]
        )
    )


    assert len(
        builder.list()
    ) == 1


    # Backup

    backup = BackupManager()

    backup.create(
        BackupManifest(
            name="athena",
            version="1.0",
            components=[
                "workspace"
            ]
        )
    )


    assert (
        backup.restore_check(
            "athena"
        )["status"]
        ==
        "available"
    )


    # Migration

    migration = WorkspaceMigration()

    migration.create(
        MigrationManifest(
            workspace="Athena",
            version="1.0",
            components=[
                "knowledge"
            ]
        )
    )


    assert (
        migration.validate(
            "Athena"
        )["status"]
        ==
        "ready"
    )
