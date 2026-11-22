# Autonomous Deep Research Multi-Agent System

A Python platform that turns a research question into a structured, source-backed report. It combines web research, document retrieval, specialized agents, evidence verification, persistent research notes, and a live report dashboard.

The system plans multi-step investigations, gathers evidence through tools and MCP integrations, checks findings against their sources, and presents the results in a clear report.

## Capabilities

- Breaks a broad research question into focused, trackable tasks.
- Combines public web research with retrieval from a local document collection.
- Coordinates specialist agents and preserves useful context across the investigation.
- Verifies findings against collected evidence before generating the report.
- Streams run progress and presents the finished report in a browser dashboard.

## Architecture

```mermaid
flowchart TD
    U["Research question"] --> W["Web dashboard"]
    W --> API["FastAPI service"]
    API --> P["Stateful planner"]
    P --> O["Agent orchestrator"]
    O --> R["Research and analysis agents"]
    O --> K["Document retrieval"]
    R --> M["MCP tools and web sources"]
    M --> E["Evidence and research notes"]
    K --> E
    E --> V["Evidence reviewer"]
    V --> G["Report generator"]
    G --> S["Stream results to dashboard"]
```

The planner decomposes the request, the orchestrator assigns work, and the reviewer checks evidence before the report is returned.

