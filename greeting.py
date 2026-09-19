"""Greeting script for the PR review walkthrough demo."""

import sys

DEFAULT_NAME = "world"


def build_greeting(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to the PR review walkthrough."


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_NAME
    print(build_greeting(name))


if __name__ == "__main__":
    main()
