from athena_sdk.os import (
    WorkspaceMigration,
    MigrationManifest,
)


def test_workspace_migration():

    migration = WorkspaceMigration()


    migration.create(
        MigrationManifest(
            workspace="Athena Workspace",
            version="1.0",
            components=[
                "knowledge",
                "plugins",
                "models"
            ]
        )
    )


    result = migration.validate(
        "Athena Workspace"
    )


    assert (
        result["status"]
        ==
        "ready"
    )


    assert len(
        migration.list()
    ) == 1
