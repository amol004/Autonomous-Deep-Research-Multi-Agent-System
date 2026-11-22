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

## Technical architecture

| Category | Technologies and engineering concepts |
| --- | --- |
| Programming | Python 3.13, JavaScript, `asyncio`, and virtual environments |
| LLM integration | Ollama, OpenAI-compatible LLM APIs, tool calling, and prompt engineering |
| Data storage and memory | SQLite, conversation history, persistent memory, and semantic memory |
| Retrieval-augmented generation | Document chunking, metadata, embeddings, keyword and semantic search, hybrid retrieval, re-ranking, and cosine similarity |
| Vector databases | FAISS and ChromaDB |
| Agent architecture | Agent state, planning, task decomposition, execution loops, and tool management |
| Protocols and integrations | MCP clients and servers, tool registries, remote HTTP transport, resources, prompts, authentication, and authorization |
| Multi-agent orchestration | Manager-worker systems, specialist roles, parallel execution, fan-out/fan-in, and iterative review cycles with bounded termination |
| Agent frameworks | LangChain, LangChain Expression Language (LCEL), LangGraph, and CrewAI |
| Backend | FastAPI, Pydantic, request and tool validation, error handling, and health checks |
| Deployment | Docker, Docker Compose, and application lifecycle management |
| Reliability and security | Retries, backoff, timeouts, rate limiting, permissions, safe file access, and prompt-injection protection |
| Observability and evaluation | Structured logging, automated retrieval and answer evaluation, and LLM-as-a-Judge |
| Frontend | HTML, CSS, JavaScript, research dashboards, and real-time progress streaming |

## Local setup

Use Python 3.13 or later. Create a virtual environment and install the packages needed by the local assistant and document utilities:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install openai python-dotenv pypdf
```

Install `python-docx` to extract text from Word documents:

```bash
python -m pip install python-docx
```

Create a `.env` file in the repository root and configure the model endpoint and names available in your local runtime:

```dotenv
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=your-chat-model
EMBEDDING_MODEL=embeddinggemma-2:740m
```

## Local utilities

Generate embeddings for a supported document:

```bash
python embedding.py "path/to/document.pdf"
```

On an Apple Silicon Mac, start the included MLX-LM chat server with:

```bash
python start_mlx_server.py
```

The MLX-LM helper serves the configured chat model on port 8080. Ollama remains the default endpoint for embedding generation.

