import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.akp import KnowledgePackage
from athena_sdk.provenance import create_provenance


def repository_to_akp(
    repository: dict
) -> KnowledgePackage:
    """
    Convert repository metadata into AKP.
    """

    content = f"""
Repository:
{repository['name']}

Files:
{chr(10).join(repository['files'])}

Latest Commit:
{repository['latest_commit']}

Documentation:
{repository['readme']}
"""

    return KnowledgePackage(
        title=repository["name"],

        content=content,

        source={
            "name": "Git Repository",
            "type": "software project"
        },

        confidence={
            "level": "high",
            "reason": "Extracted from local repository"
        },

        evidence={
            "source_type": "repository files"
        },

        provenance=create_provenance(
            "athena-git-repository-importer",
            "0.1"
        ),

        metadata={
            "file_count": len(repository["files"])
        }
    )
