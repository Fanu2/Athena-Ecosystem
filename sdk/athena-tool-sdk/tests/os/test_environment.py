from athena_sdk.os import (
    EnvironmentManager,
    EnvironmentInfo,
)


def test_environment_manager():

    manager = EnvironmentManager()


    manager.register(
        EnvironmentInfo(
            name="Athena Portable",
            version="1.0",
            components=[
                "sdk",
                "plugins"
            ]
        )
    )


    result = manager.find(
        "Athena Portable"
    )


    assert (
        result.version
        ==
        "1.0"
    )


    assert len(
        manager.list()
    ) == 1
