"""MCP server skeleton for Aetherlog.

TODO: register real tools/resources here. This stub exists so the project
has something importable and testable from the first commit -- the build
loop fills in the actual server logic one task at a time.
"""


def main() -> None:
    """Entry point for the aetherlog console script.

    The real server logic will be added in later tasks. For now, this
    implementation provides a minimal CLI that supports ``--help`` and
    exits cleanly.
    """
    import argparse

    parser = argparse.ArgumentParser(
        prog="aetherlog",
        description="Aetherlog server – placeholder implementation.",
    )
    # No real arguments yet; this is just a stub.
    parser.add_argument(
        "--version",
        action="version",
        version="aetherlog 0.1.0",
        help="Show the version number and exit.",
    )
    # Parse arguments; argparse will automatically handle --help.
    parser.parse_args()
    # If we reach here, simply exit successfully.
    return None



if __name__ == "__main__":
    main()
