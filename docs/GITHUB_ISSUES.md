# GitHub Issue Backlog

The full text of every issue (description and motivation, concepts, prerequisites, implementation requirements, acceptance-criteria checkboxes, test requirements, out-of-scope items, definition of done, effort, labels, milestone) lives in the GitHub Issues tab of this repository. This file is the ordered index. Work strictly in dependency order. Issues #1 to #47 were created on 2026-10-17.

Priorities are also GitHub labels p0, p1, p2. Effort: S 1-2 h, M 3-5 h, L 6-10 h. P2 issues and milestones M10-M11 are stretch.

Ordering note: issue 30 (supervisor) should be done before issue 29 (the ADR that compares single and multi-agent), because the ADR needs the supervisor numbers.

| Issue | Milestone | Title | Priority | Effort |
|---|---|---|---|---|
| 1 | M0 | Scaffold the project, tooling, and CI | P0 | M |
| 2 | M0 | Prove CI blocks a broken change | P0 | S |
| 3 | M1 | Domain models with validation | P0 | M |
| 4 | M1 | Typed domain errors | P0 | S |
| 5 | M1 | Menu service: lookup and availability | P0 | M |
| 6 | M1 | Pricing and bill calculation | P0 | M |
| 7 | M1 | Order service with injected repository | P0 | L |
| 8 | M1 | Swap in a JSON-file repository | P1 | S |
| 9 | M2 | Spike: verify current LangChain, LangGraph, and MCP docs and versions | P0 | S |
| 10 | M2 | Tool layer over services with typed schemas | P0 | M |
| 11 | M2 | Scripted fake-model tool loop | P0 | M |
| 12 | M2 | Real model via LangChain behind a factory | P0 | L |
| 13 | M2 | Handle invalid arguments and tool failures | P0 | M |
| 14 | M2 | Sequential and parallel tool calls | P1 | M |
| 15 | M3 | Deterministic order graph | P0 | L |
| 16 | M3 | Conditional routing and bounded substitution loop | P0 | M |
| 17 | M3 | Fan-out and join for availability checks | P1 | M |
| 18 | M3 | Agent node for ambiguous requests vs deterministic routing | P1 | L |
| 19 | M4 | Checkpointing and resume after restart | P0 | M |
| 20 | M4 | Human approval interrupt before placing an order | P0 | M |
| 21 | M4 | Idempotent order creation | P0 | M |
| 22 | M5 | Build the custom agent harness | P0 | L |
| 23 | M5 | Retry, timeout, and fallback policies | P1 | M |
| 24 | M5 | Authorization guardrails for tools | P0 | M |
| 25 | M5 | Context management and token budget | P1 | M |
| 26 | M5 | Prompt-injection defense and trust boundaries | P0 | M |
| 27 | M5 | Audit trail for tool calls and approvals | P1 | S |
| 28 | M6 | Single-agent baseline with a minimal eval | P0 | M |
| 29 | M6 | ADR: single agent vs multi-agent (do after issue 30) | P0 | S |
| 30 | M6 | Supervisor with specialist agents | P1 | L |
| 31 | M7 | Preference store and memory vs checkpoint boundary | P1 | M |
| 32 | M7 | RAG over menu and FAQ with measured retrieval | P1 | L |
| 33 | M7 | ADR: relational vs vector storage | P1 | S |
| 34 | M8 | Evaluation dataset and runner | P0 | L |
| 35 | M8 | Tracing and structured logs | P1 | M |
| 36 | M8 | Token, latency, and cost tracking | P1 | M |
| 37 | M8 | CI regression gate for offline evals | P1 | M |
| 38 | M9 | MCP server exposing menu and order tools | P1 | L |
| 39 | M9 | MCP client under the harness allowlist | P1 | M |
| 40 | M9 | Optional: A2A boundary experiment | P2 | M |
| 41 | M10 | Deep Agents comparison experiment | P2 | M |
| 42 | M10 | Semantic Kernel comparison experiment | P2 | M |
| 43 | M11 | FastAPI service: chat, approve, status | P0 | L |
| 44 | M11 | Authentication, secrets, and rate limits | P1 | M |
| 45 | M11 | Containerize and add CI/CD | P1 | M |
| 46 | M11 | Load test and benchmarks | P2 | M |
| 47 | M11 | Monitoring, alerts, and runbook | P2 | M |

## Known gaps to fix as you go

The feature IDs in docs/FEATURES.md are not yet linked to issue numbers. Add the link in each issue's PR. Optional later issues not yet created: parallel specialist agents (F-27), background queue (F-43). Create them when you reach them.
