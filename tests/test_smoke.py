"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import aetherlog


def test_version_is_set() -> None:
    assert aetherlog.__version__
