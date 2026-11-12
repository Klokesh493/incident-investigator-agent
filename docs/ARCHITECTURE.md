# Incident Investigator Agent architecture

Select time-bounded evidence for the impacted service.

```mermaid
flowchart LR
    N0["example.json"]
    N1["agent.py"]
    N2["Filter by impacted service and incident time range, then sort matching event IDs."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
