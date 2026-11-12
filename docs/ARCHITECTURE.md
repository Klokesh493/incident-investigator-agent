# Incident Investigator Agent architecture

Select time-bounded evidence for the impacted service.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
