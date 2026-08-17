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

    sub.add_parser(
        "list"
    )

    sub.add_parser(
        "status"
    )

    args = parser.parse_args()

    tools = scan_tools(
        "tools"
    )

    if args.command == "list":

        print("Athena Tools")
        print("=============")

        for tool in tools:

            print(
                f"{tool.name:45} {tool.version}"
            )


    elif args.command == "status":

        print("Athena Tool Status")
        print("==================")

        for tool in tools:

            print(
                f"{tool.name:45} {tool.state}"
            )


    else:

        parser.print_help()


if __name__ == "__main__":
    main()
