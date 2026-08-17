from pathlib import Path
import yaml

from .models import ToolRegistryEntry


def scan_tools(
    tools_directory: str
):

    tools = []

    root = Path(
        tools_directory
    )

    for manifest in root.rglob(
        "tool_manifest.yaml"
    ):

        with manifest.open(
            "r",
            encoding="utf-8"
        ) as f:

            data = yaml.safe_load(f)

        tools.append(
            ToolRegistryEntry(

                name=data.get(
                    "name",
                    ""
                ),

                version=str(
                    data.get(
                        "version",
                        ""
                    )
                ),

                description=data.get(
                    "description",
                    ""
                ),

                path=str(
                    manifest.parent
                ),

                akp_versions=data.get(
                    "akp_versions",
                    []
                ),

                permissions=data.get(
                    "permissions",
                    {}
                ),

                capabilities=data.get(
                    "capabilities",
                    []
                ),

                inputs=data.get(
                    "inputs",
                    []
                ),

                outputs=data.get(
                    "outputs",
                    []
                ),

                command=data.get(
                    "command",
                    []
                )
            )
        )

    return tools
