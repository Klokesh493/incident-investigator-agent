# Incident Investigator Agent walkthrough

## Business problem

Select time-bounded evidence for the impacted service.

## Reproduce the workflow

Run `python3 agent.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
[
  "e1"
]
```

The sample supplies these fields. `service`, `start`, `end`, `events`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Regression scenario

Include an event on the end boundary and exclude events for a different service.

`make verify` runs this scenario and compares the result with the checked-in expected JSON.
