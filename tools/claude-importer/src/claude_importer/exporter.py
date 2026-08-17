from pathlib import Path
import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import (
    validate,
    serialize,
)


def export_akp(
    package,
    output_dir: str,
    filename: str
):

    validate(package)

    path = Path(output_dir)

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    serialize(
        package,
        str(path / filename)
    )
