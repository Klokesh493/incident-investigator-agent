# Skills and verification

## What this repository demonstrates

A local incident evidence filter. It validates the time range, keeps events for the affected service within the inclusive window, and returns event IDs ordered by timestamp and ID.

## Reproduce the result

The bundled fixture returns event e1. Events outside the window or from another service are excluded. Reproduce the primary fixture with `python3 agent.py example.json`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The tool works from supplied events and neither queries live telemetry nor determines root cause.

Align the incident time window and service identity with the source export. Follow returned event IDs back to the evidence.

[agent.py](../agent.py) · [examples/Bundled scenario.stdout.txt](../examples/Bundled%20scenario.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
