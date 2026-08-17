VALID_STATES = [
    "discovered",
    "verified",
    "enabled",
    "disabled",
]


def set_state(
    tool,
    state: str
):

    if state not in VALID_STATES:

        raise ValueError(
            f"Invalid state: {state}"
        )

    tool.state = state

    return tool


def is_enabled(
    tool
):

    return (
        tool.state == "enabled"
    )
