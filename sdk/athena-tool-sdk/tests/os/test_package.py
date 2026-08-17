from athena_sdk.os import (
    RuntimePackage,
    PackageBuilder,
)


def test_runtime_package():

    builder = PackageBuilder()


    package = builder.create(
        RuntimePackage(
            name="Athena Offline Runtime",
            version="1.0",
            components=[
                "sdk",
                "plugins",
                "models"
            ]
        )
    )


    assert (
        package.name
        ==
        "Athena Offline Runtime"
    )


    assert len(
        builder.list()
    ) == 1
