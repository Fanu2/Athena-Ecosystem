import argparse

from athena_sdk.registry import (
    scan_tools,
    find_by_capability,
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

    find = sub.add_parser(
        "find"
    )

    find.add_argument(
        "--capability",
        required=True
    )

    args = parser.parse_args()

    tools = scan_tools(
        "tools"
    )

    if args.command == "find":

        results = find_by_capability(
            tools,
            args.capability
        )

        print(
            "Matching Tools"
        )

        print(
            "=============="
        )

        for tool in results:

            print()
            print(
                tool.name
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


    elif args.command == "capabilities":

        for tool in tools:

            print()
            print(
                tool.name
            )

            print(
                tool.capabilities
            )


    else:

        parser.print_help()


if __name__ == "__main__":
    main()
