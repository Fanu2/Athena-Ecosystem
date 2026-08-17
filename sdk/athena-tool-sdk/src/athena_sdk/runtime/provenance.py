from datetime import datetime, timezone


def create_execution_record(
    tool,
    result
):

    return {
        "tool": tool.name,

        "status": result.status,

        "timestamp":
            datetime.now(
                timezone.utc
            ).isoformat()
    }
