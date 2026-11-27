"""CLI test: `aetherlog --help` exits 0 and prints usage."""

import subprocess
import sys


def test_cli_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "aetherlog.server", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "usage" in result.stdout