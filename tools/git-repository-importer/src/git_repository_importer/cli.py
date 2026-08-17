import argparse

from .importer import import_repository


def main():

    parser = argparse.ArgumentParser(
        description="Athena Git Repository Importer"
    )

    sub = parser.add_subparsers(
        dest="command"
    )

    cmd = sub.add_parser(
        "import",
        help="Import Git repository"
    )

    cmd.add_argument(
        "--repo",
        required=True
    )

    cmd.add_argument(
        "--output",
        required=True
    )

    args = parser.parse_args()

    if args.command == "import":

        result = import_repository(
            args.repo,
            args.output
        )

        print(
            "Athena Git Import Complete"
        )

        print(
            f"Repository: {result['repository']}"
        )

        print(
            f"Status: {result['status']}"
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
