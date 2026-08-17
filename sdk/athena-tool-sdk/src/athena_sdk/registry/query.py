def find_by_capability(
    tools,
    capability: str
):
    return [
        tool
        for tool in tools
        if capability in tool.capabilities
    ]


def find_by_input(
    tools,
    input_type: str
):
    return [
        tool
        for tool in tools
        if input_type in tool.inputs
    ]


def find_by_output(
    tools,
    output_type: str
):
    return [
        tool
        for tool in tools
        if output_type in tool.outputs
    ]
