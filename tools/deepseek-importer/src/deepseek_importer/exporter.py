from pathlib import Path
import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import (
    validate,
    serialize,
    AKPValidationError,
)

from athena_sdk.akp import (
    KnowledgePackage,
)


def export_akp(
    package: KnowledgePackage,
    output_dir: str,
    filename: str
) -> bool:
    """
    Validate and export AKP package.
    """

    validate(package)

    path = Path(output_dir)

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = path / filename

    serialize(
        package,
        str(output_file)
    )

    return True
