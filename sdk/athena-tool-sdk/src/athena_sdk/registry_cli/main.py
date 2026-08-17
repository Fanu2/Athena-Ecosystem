import argparse

from athena_sdk.registry import (
    scan_tools
)


def main():

    parser = argparse.ArgumentParser(
        description="Athena Tool Registry"
    )

    sub = parser.add_subparsers(
        dest="command"
    )

    sub.add_parser("list")
    sub.add_parser("status")
    sub.add_parser("capabilities")

    args = parser.parse_args()

    tools = scan_tools(
        "tools"
    )


    if args.command == "capabilities":

        print(
            "Athena Tool Capabilities"
        )

        print(
            "========================"
        )

        for tool in tools:

            print()
            print(
                tool.name
            )

            print(
                "Capabilities:",
                tool.capabilities
            )

            print(
                "Inputs:",
                tool.inputs
            )

            print(
                "Outputs:",
                tool.outputs
            )


    elif args.command == "list":

        for tool in tools:
            print(
                tool.name,
                tool.version
            )


    elif args.command == "status":

        for tool in tools:
            print(
                tool.name,
                tool.state
            )


    else:

        parser.print_help()


if __name__ == "__main__":
    main()
