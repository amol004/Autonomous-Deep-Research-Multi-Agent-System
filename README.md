# Autonomous Deep Research Multi-Agent System

A research platform that turns a complex question into a structured, evidence-backed report. It combines web research, document retrieval, specialized agents, persistent memory, and a browser dashboard with live progress updates.

## Project overview

Research work often means switching between search, documents, notes, and review. This system brings those steps into one traceable workflow. It breaks a request into tasks, gathers evidence from public sources and local documents, coordinates agents to analyze and review the material, and produces a report with the supporting evidence.

Each run maintains its task state and research notes. The final response is built from retrieved evidence, while unsupported claims, conflicting sources, and open questions remain visible for review.

## Product capabilities

- **Research planning:** turns a broad question into smaller tasks and tracks each task through execution.
- **Web research:** searches for sources and reads relevant webpages through controlled tools.
- **Document question answering:** retrieves relevant passages from a collection of PDFs, Word files, and text documents.
- **Agent collaboration:** assigns research, analysis, and review work to specialized agents, sequentially or in parallel.
- **Persistent context:** keeps conversation history, extracted facts, and research notes available across steps.
- **Evidence review:** checks whether report claims are supported by retrieved sources and flags gaps.
- **Report delivery:** generates a structured report and streams progress to a browser dashboard.
- **Service deployment:** exposes the research workflow through a validated API and a container-ready application design.

