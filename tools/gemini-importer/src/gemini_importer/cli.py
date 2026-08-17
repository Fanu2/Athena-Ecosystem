import argparse

from .importer import import_gemini


def main():

    parser = argparse.ArgumentParser(
        description="Athena Gemini Importer"
    )

    sub = parser.add_subparsers(
        dest="command"
    )

    cmd = sub.add_parser(
        "import"
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

        result = import_gemini(
            args.input,
            args.output
        )

        print(
            "Athena Gemini Import Complete"
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


if __name__ == "__main__":
    main
