# Incident Investigator Agent

Incident evidence is easier to review when responders can isolate the affected service and time window from a larger event export.

## What I built

I built a local incident evidence filter. It validates the time range, keeps events for the affected service within the inclusive window, and returns event IDs ordered by timestamp and ID.

## How it works

```mermaid
flowchart LR
    A["Service, time bounds, and event records"]
    B["Validate time range and filter by service"]
    C{"Within incident time range?"}
    D["Sort and return matching event IDs"]
    E["Exclude unrelated evidence"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [agent.py](agent.py) implements the CLI and decision rules. Uses `argparse` to parse command-line options, `json` to read or write structured records, `pathlib` to read local files. |
| Make | Runs the documented example and local checks. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 agent.py example.json
```

The bundled fixture returns event e1. Events outside the window or from another service are excluded. [Full expected output](examples/Bundled%20scenario.stdout.txt)

### Additional replay cases

- **Regression scenario** · `python3 agent.py examples/regression.json` · [Expected output](examples/Regression%20scenario.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The tool works from supplied events and neither queries live telemetry nor determines root cause.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
