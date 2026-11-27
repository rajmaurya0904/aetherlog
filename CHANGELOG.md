# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-15

### Added

- Initial release of the Aetherlog MCP server package.
- `aetherlog.server` entry point exposing a placeholder MCP server with
  `--help` and `--version` CLI options.
- Package metadata in `pyproject.toml` with an editable install path.
- Test suite covering CLI behavior, linting, and smoke tests.
- CI workflow for running the test suite on pull requests.