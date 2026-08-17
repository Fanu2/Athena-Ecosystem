from pathlib import Path
import json


def import_akp_workspace(
    workspace,
    akp_directory: str
):

    path = Path(
        akp_directory
    )

    imported = 0

    for file in path.glob(
        "*.akp.json"
    ):

        try:

            data = json.loads(
                file.read_text(
                    encoding="utf-8"
                )
            )

            title = data.get(
                "title",
                file.name
            )

            workspace.add_knowledge(
                title
            )

            imported += 1

        except Exception:

            continue

    return {
        "status": "success",
        "imported": imported
    }
