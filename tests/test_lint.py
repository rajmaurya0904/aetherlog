import subprocess


def test_lint_passes():
    result = subprocess.run(
        ["ruff", "check", "."],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
