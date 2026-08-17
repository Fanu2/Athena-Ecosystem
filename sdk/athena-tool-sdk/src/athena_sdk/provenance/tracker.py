from datetime import datetime, timezone


def create_provenance(
    tool_name: str,
    tool_version: str
) -> dict:
    """
    Create Athena provenance record.
    """

    return {
        "tool": tool_name,
        "version": tool_version,
        "created_at": datetime.now(
            timezone.utc
        ).isoformat()
    }
