import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import (
    KnowledgePackage,
    validate,
    serialize,
    deserialize
)

from athena_sdk.provenance import (
    create_provenance
)

from athena_sdk.logging import (
    get_logger
)


def test_sdk_flow():

    logger = get_logger(
        "sdk-test"
    )

    logger.info(
        "Creating AKP"
    )

    package = KnowledgePackage(
        title="SDK Integration Test",
        content="Athena ecosystem test",
        source={
            "name": "test-source"
        },
        confidence={
            "level": "unknown"
        },
        evidence={
            "reference": "test.txt"
        },
        provenance=create_provenance(
            "sdk-test-tool",
            "0.1"
        )
    )

    assert validate(package)

    serialize(
        package,
        "sdk-test.akp.json"
    )

    loaded = deserialize(
        "sdk-test.akp.json"
    )

    assert loaded.title == package.title

    logger.info(
        "SDK integration successful"
    )
