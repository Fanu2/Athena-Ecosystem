def validate_command(
    command
):

    if not command:

        raise ValueError(
            "Empty plugin command"
        )

    return True
