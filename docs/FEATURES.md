# Feature Inventory

Effort: S = 1-2 h, M = 3-5 h, L = 6-10 h. Priority: P0 essential, P1 important, P2 optional/advanced. Every feature is expanded into issues in docs/GITHUB_ISSUES.md. Status of every feature: Planned.

## Fundamentals

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-01 | Project scaffold and tooling | Reproducible dev loop | Git, packaging, CI | none | P0 | M | Fresh clone runs pytest, ruff, mypy with one command; CI green | Smoke test |
| F-02 | Domain models | Typed menu and order objects | Type hints, validation | F-01 | P0 | M | Invalid data rejected with clear errors | Valid and invalid construction |
| F-03 | Menu service | Lookup and availability | Pure functions, exceptions | F-02 | P0 | M | Unknown item raises a domain error; case and whitespace handled | Parametrized lookups |
| F-04 | Pricing and billing | Totals, tax, discounts | Determinism, money handling | F-02, F-03 | P0 | M | No float rounding bugs; discount rules documented | Table tests, edge cases |
| F-05 | Order service | Create and validate orders | Separation of concerns, dependency injection | F-03, F-04 | P0 | L | Stock and quantity rules enforced; repository injected | Fake-repository tests |
| F-06 | Typed domain errors | Structured failures | Exception taxonomy | F-02 | P0 | S | Every error has a machine-readable code | Error-code tests |

## Agent workflows

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-07 | Tool layer | Expose services as tools | Tool schemas, descriptions | F-05 | P0 | M | Each tool has a typed schema; no business logic in tools | Schema and mocked-service tests |
| F-08 | Fake-model tool loop | Understand the loop without an LLM | Observe-act cycle | F-07 | P0 | M | A scripted model drives tools to completion | Scripted-trace tests |
| F-09 | Real LLM via LangChain | Model integration, tool binding | Messages, providers, tokens | F-07, F-08 | P0 | L | Provider swappable by config; free or local option works | Fake-model unit tests; optional live test |
| F-10 | Invalid-argument and tool-failure handling | Recover from model mistakes | Error feedback to model | F-09 | P0 | M | Bad arguments produce an error the model can act on | Failure-injection tests |
| F-11 | Sequential and parallel tool calls | Understand ordering | Tool call batching | F-09 | P1 | M | Results matched to the right calls | Multi-call tests |
| F-12 | Deterministic LangGraph order workflow | Explicit state machine | StateGraph, nodes, edges, START/END, reducers | F-05 | P0 | L | Happy path and failure branches run | One routing test per branch |
| F-13 | Conditional routing and bounded loops | Branching and retry | Conditional edges, termination | F-12 | P0 | M | Out-of-stock routes to substitution; loops are bounded | Branch and loop-bound tests |
| F-14 | Agent node inside the graph | Mix deterministic and agentic steps | Workflow vs agent | F-09, F-12 | P1 | L | LLM handles only the ambiguous step | Fake-model graph test |
| F-15 | Fan-out and join | Parallel steps with merge | Reducers, joins | F-12 | P1 | M | Parallel availability checks merge correctly | Order-independence test |
| F-16 | Checkpointing and thread resume | Durable state | Threads, checkpointers | F-12 | P0 | M | A run resumes after a process restart | Persistence test with temp DB |
| F-17 | Human approval interrupt | Confirm before side effects | Interrupts, resume | F-16 | P0 | M | Payment never runs before approval; reject path works | Approve, reject, timeout tests |

## Agent harness and security

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-18 | Custom agent harness | Own the loop | Max steps, allowlist, termination | F-09 | P0 | L | Enforces step limit, tool allowlist, timeout | Policy-violation tests |
| F-19 | Idempotent side effects | Retries never double-order | Idempotency keys | F-05, F-18 | P0 | M | Same key returns the same order | Duplicate-request tests |
| F-20 | Retry, timeout, fallback policies | Reliability | Backoff, fallbacks | F-18 | P1 | M | Transient errors retried; permanent errors not | Fault-injection tests |
| F-21 | Context management | Stay inside the window | Trimming, summarization | F-09 | P1 | M | Long histories trimmed without losing order state | Token-budget tests |
| F-22 | Guardrails and authorization | Controlled side effects | Input/output validation, authz | F-18 | P0 | M | A user cannot read or cancel another user's order | Authorization matrix tests |
| F-23 | Prompt-injection defense | Untrusted data handling | Trust boundaries | F-22 | P0 | M | Injected text in menu or notes cannot trigger tools | Injection corpus tests |
| F-24 | Audit trail | Accountability | Structured logging | F-18 | P1 | S | Every tool call and approval is logged | Log-assertion tests |

## Multi-agent systems

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-25 | Single-agent baseline | Justify any split | Baselines | F-14, F-29 | P0 | M | Baseline metrics recorded | Eval run |
| F-26 | Supervisor and specialists | Menu, pricing, order, support agents | Delegation, handoffs, isolated vs shared state | F-25 | P1 | L | Supervisor routes correctly; specialists have restricted tools | Routing and isolation tests |
| F-27 | Parallel agents with aggregation | Concurrency | Fan-out, aggregation | F-26 | P2 | M | Deterministic merge | Concurrency tests |
| F-28 | Multi vs single ADR | Evidence-based decision | Trade-off analysis | F-26 | P0 | S | ADR cites measured data | Manual review |

## Evaluation and observability

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-29 | Evaluation dataset and runner | Measure behavior | Tool-selection accuracy, task completion | F-09 | P0 | L | 30+ labeled cases; report produced | Runner tests on fake model |
| F-30 | Tracing and structured logs | See what happened | Spans, correlation IDs | F-18 | P1 | M | One trace per request with tool spans | Trace-shape tests |
| F-31 | Token, latency, cost tracking | Operating economics | Usage metrics | F-30 | P1 | M | Per-request cost visible | Counter tests |
| F-32 | Regression gate in CI | Prevent quality drops | Thresholds | F-29 | P1 | M | CI fails if offline eval drops below threshold | Gate test |

## Memory and retrieval

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-33 | Memory vs checkpoint boundary | Short vs long-term state | Memory design | F-16 | P1 | M | Written boundary doc and working preference store | Persistence tests |
| F-34 | RAG over menu and FAQ | Retrieval | Embeddings, vector search, chunking | F-33 | P1 | L | Allergen and FAQ questions answered from retrieved docs | Retrieval-quality tests |
| F-35 | Storage decision ADR | Choose the right store | Relational vs vector | F-34 | P1 | S | Decision backed by an experiment | Manual review |

## Integrations

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-36 | MCP server for menu and order tools | Reusable external tools | MCP servers, tools, resources, prompts | F-07 | P1 | L | An MCP client lists and calls the tools | In-process client tests |
| F-37 | MCP client inside the agent | Consume external tools | MCP clients, trust | F-36, F-18 | P1 | M | MCP tools obey the harness allowlist | Allowlist tests |
| F-38 | A2A boundary experiment | Agent-to-agent concepts | Communication boundaries | F-26 | P2 | M | Two processes exchange a task via a contract | Contract tests |
| F-39 | Deep Agents comparison | Evaluate framework | Planning, delegation | F-29 | P2 | M | Same eval run; written comparison | Eval run |
| F-40 | Semantic Kernel comparison | Evaluate framework | Agent abstractions | F-29 | P2 | M | Same eval run; written comparison | Eval run |

## Production engineering

| ID | Feature | Purpose | Concepts learned | Depends on | Pri | Effort | Acceptance criteria | Required tests |
|---|---|---|---|---|---|---|---|---|
| F-41 | FastAPI service | HTTP interface | Async, request models | F-17 | P0 | L | Chat, approve, status endpoints | API tests with TestClient |
| F-42 | Authentication, secrets, rate limits | Secure access | Authn/authz, config | F-41 | P1 | M | No secrets in repo; per-user limits | Security tests |
| F-43 | Background execution and queue | Long-running tasks | Async workers | F-41 | P2 | L | API returns a job id; worker completes the run | Worker tests |
| F-44 | Containerization and CI/CD | Deployment | Docker, pipelines | F-41 | P1 | M | Image builds; pipeline deploys to staging or dry run | Pipeline run |
| F-45 | Load tests and benchmarks | Performance | Throughput, tail latency | F-41, F-31 | P2 | M | Report with p50, p95, cost per order | Benchmark script |
| F-46 | Monitoring and runbook | Operations | Alerts, SLOs | F-30, F-44 | P2 | M | Runbook and dashboard sketch | Review |
