# Autonomous Deep Research Multi-Agent System

A Python research platform that turns a question into a structured, source-backed report. It brings together LLM assistants, conversation memory, reusable tools, document retrieval, agent planning, MCP, and multi-agent orchestration.

The project follows the practical path in [AI Agent Engineering: Build Production-Ready AI Agents](https://www.udemy.com/course/ai-agent-engineering/) by Pankaj Shukla and applies the course’s core techniques to a research workflow.


## What the platform does

The system takes a research question through a repeatable workflow:

- Breaks the question into focused research tasks.
- Uses specialized agents and tools to gather relevant information.
- Retrieves supporting passages from an ingested document collection.
- Keeps research state and notes available across steps.
- Checks findings against their sources and turns them into a structured report.

The same workflow supports both open-ended research and questions grounded in a supplied document set.

