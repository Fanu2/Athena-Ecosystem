import argparse

from .importer import import_messenger


def main():

    parser = argparse.ArgumentParser(
        description="Athena Facebook Messenger Importer"
    )

    sub = parser.add_subparsers(
        dest="command"
    )

    cmd = sub.add_parser(
        "import",
        help="Import Messenger conversations"
    )

    cmd.add_argument(
        "--input",
        required=True
    )

    cmd.add_argument(
        "--output",
        required=True
    )

    args = parser.parse_args()

    if args.command == "import":

        result = import_messenger(
            args.input,
            args.output
        )

        print(
            "Athena Messenger Import Complete"
        )

        print(
            f"Conversations: {result['input']}"
        )

        print(
            f"AKP Created: {result['exported']}"
        )

        print(
            f"Status: {result['status']}"
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
