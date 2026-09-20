# Architecture

This repository intentionally separates project concerns.

```text
                    ┌───────────────────┐
                    │   User / Source   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Validation / I/O  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Transform / Prep  │
                    └─────────┬─────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        ┌──────────────┐            ┌──────────────┐
        │ Deterministic│            │ ML / AI      │
        │ logic        │            │ component    │
        └──────┬───────┘            └──────┬───────┘
               │                           │
               └─────────────┬─────────────┘
                             ▼
                    ┌───────────────────┐
                    │ Evaluation        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ API / Batch / UI  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Monitoring / Logs │
                    └───────────────────┘
```

Every project may simplify this architecture. Complexity should be justified by requirements.

## Definition of done

A project is not complete when a notebook runs.

It is complete when:
- requirements are documented;
- inputs are understood;
- implementation is reproducible;
- tests protect important behavior;
- evaluation is explained;
- limitations are documented;
- the project can be handed to another developer.
