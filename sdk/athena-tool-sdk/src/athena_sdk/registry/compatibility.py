def supports_akp(
    tool,
    version="1.0"
) -> bool:

    return (
        version
        in tool.akp_versions
    )
