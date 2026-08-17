def validate_plugin_execution(
    tool
):

    if tool.state not in [
        "verified",
        "enabled",
    ]:

        raise PermissionError(
            "Plugin is not enabled or verified"
        )

    if not tool.command:

        raise ValueError(
            "Plugin command missing"
        )

    return True
