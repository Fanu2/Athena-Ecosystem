import argparse

from .importer import import_deepseek


def main():

    parser = argparse.ArgumentParser(
        description="Athena DeepSeek Importer"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    import_parser = subparsers.add_parser(
        "import",
        help="Import DeepSeek conversations"
    )

    import_parser.add_argument(
        "--input",
        required=True
    )

    import_parser.add_argument(
        "--output",
        required=True
    )

    args = parser.parse_args()

    if args.command == "import":

        result = import_deepseek(
            args.input,
            args.output
        )

        print(
            "Athena DeepSeek Import Complete"
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

        print()

        print(
            result["report"].display()
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
