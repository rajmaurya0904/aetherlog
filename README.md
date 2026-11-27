# Aetherlog

**A Model Context Protocol server that enables AI coding assistants to securely query and aggregate distributed microservice logs.**

When debugging microservices across distributed containers, AI coding assistants are flying blind without unified log context. Pasting gigabytes of raw logs into chat windows blows context limits, leaks secrets, and breaks workflows. Aetherlog bridges this gap by exposing a secure MCP interface for live log queries and aggregation directly inside your development environment.

## Example

Run the Aetherlog MCP server:

```bash
$ python3 -m aetherlog.server --help
usage: aetherlog [-h] [--version]

Aetherlog server – placeholder implementation.

options:
  -h, --help  show this help message and exit
  --version   Show the version number and exit.
```

## Install

```bash
pip install -e .
```

## Usage

- Start the Aetherlog server:
  ```bash
  python3 -m aetherlog.server
  ```

## How it works

- Inspects incoming MCP tool calls from AI assistants.
- Validates query scopes and permissions against configured security policies.
- Fetches logs from OpenTelemetry-compatible storage backends.
- Sanitizes and redacts sensitive data (API keys, tokens, PII) before emission.
- Returns structured JSON payloads optimized for LLM token efficiency.

## Limitations

- Currently a prototype implementation; persistent storage backends and advanced query filters are under active development.
- Test coverage currently covers basic CLI functionality and scaffolding.
