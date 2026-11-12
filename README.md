# Incident Investigator Agent

Select time-bounded evidence for the impacted service.

## Quick start

Run `python3 agent.py example.json` with Python 3.10 or newer. Compare the result with `expected.json`. The JSON keys in the example define the supported input shape.

This offline prototype reads synthetic input and returns a recommendation or diagnostic. It uses no credentials, external APIs, or infrastructure mutations. Results require operator review.

## Local verification

Run `make verify` with Make and Python 3 installed. The sample runs through the CLI and its JSON is compared with `expected.json`.

## Business problem

Incident evidence is easier to review when responders can isolate the affected service and time window from a larger event export.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
