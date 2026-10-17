# PizzaPilot Agent Lab

A progressive, hands-on Python project that teaches AI agent engineering through a pizza-ordering assistant: tool calling, workflows, agent harnesses, multi-agent systems, reliability, evaluation, and production architecture.

> **Learning project.** Every line of application code is written by the repo owner. Business logic starts as deterministic Python with mock data. An LLM is introduced only after the deterministic core is tested.
>
> ## Status legend
>
> Implemented = done and tested. In progress = being built. Planned = not started. Update the table below in every PR that finishes a feature.
>
> | Capability | Status |
> |---|---|
> | Menu lookup and availability | Planned |
> | Price and bill calculation | Planned |
> | Order creation and validation | Planned |
> | LangChain tool wrappers | Planned |
> | LangGraph order workflow | Planned |
> | Human approval and resumable runs | Planned |
> | Agent harness controls | Planned |
> | Multi-agent delegation | Planned |
> | Memory and RAG | Planned |
> | Evaluation and observability | Planned |
> | MCP server/client (A2A optional) | Planned |
> | FastAPI service and deployment | Planned |
>
> ## Learning objectives
>
> Python engineering, LLM/LangChain, LangGraph, agent harness engineering, multi-agent systems, memory and retrieval, interoperability (MCP, A2A, Deep Agents, Semantic Kernel), evaluation, and production architecture. Full concept list: docs/CONCEPTS.md.
>
> ## Technology stack
>
> Core: Python, pytest, ruff, mypy, pydantic. Planned: langchain, langgraph, FastAPI, SQLite then Postgres, MCP SDK. A local/free model or a fake model is used first; paid APIs are never required for milestones M0 to M5. Alternative frameworks (Deep Agents, Semantic Kernel) live in experiments/ and never in core.
>
> Versions seen on PyPI on 2026-10-17: langgraph 1.2.16, langchain 1.4.6, mcp 2.3.0. Pin whatever resolves together in a clean virtualenv and record it in pyproject.toml. Verify APIs against the official docs before using them.
>
> ## Setup
>
> These commands work after Issue 1 creates pyproject.toml.
>
> ```bash
> git clone https://github.com/tikhandesanket/pizzapilot-agent-lab
> cd pizzapilot-agent-lab
> python -m venv .venv
> source .venv/bin/activate
> pip install -e ".[dev]"
> pytest && ruff check . && mypy src
> ```
>
> ## Architecture (planned)
>
> See docs/ARCHITECTURE.md. Layers: deterministic services, then tool layer, then workflow graph, then agent harness, then API. Each layer is testable without the layer above it.
>
> ## Milestones
>
> M0 Setup, M1 Deterministic core, M2 LangChain tools, M3 LangGraph, M4 Persistence and approval, M5 Harness and security, M6 Multi-agent, M7 Memory and RAG, M8 Evaluation and observability, M9 MCP and A2A, M10 Framework comparisons, M11 API and production. Details: docs/ROADMAP.md. Backlog: docs/GITHUB_ISSUES.md.
>
> ## Testing
>
> The default test run needs no network and no API keys. Live-model tests are marked live and excluded by default. See docs/TESTING.md.
>
> ## Contributing
>
> Branch feat/ISSUE-slug, Conventional Commits, PR template, CI must pass. See CONTRIBUTING.md.
> 
