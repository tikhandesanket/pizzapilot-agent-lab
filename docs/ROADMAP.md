# Roadmap

Target: about 8 weeks at 2 h/day (about 112 h) for P0 and P1 work; P2 items and M10-M11 are stretch. The timeline is an estimate, not a deadline. Do not skip a milestone's proof exercise. Rule: you write all code; the mentor gives tasks, hints, and reviews.

## M0 Setup (days 1-2, about 4 h)

| Field | Content |
|---|---|
| Learning objective | A working development loop: branch, test, lint, type-check, PR, CI |
| Understand first | Git branching, virtualenvs, pyproject.toml, pytest basics, what CI does |
| Coding assignment | Scaffold the repo, tooling config, one smoke test, CI workflow |
| Files | pyproject.toml, src/pizzapilot/__init__.py, tests/test_smoke.py, .github/workflows/ci.yml |
| Required tests | Smoke test passes locally and in CI |
| Definition of done | PR merged with green CI; commands in README work on a fresh clone |
| Interview questions | Why isolate environments? Why run CI on every PR? What should block a merge? |
| Practical exercise | Break a test on purpose; show CI blocking the PR |
| Prerequisite for M1 | One merged PR with green CI |

## M1 Deterministic core (weeks 1-2, about 20 h)

| Field | Content |
|---|---|
| Learning objective | A correct, well-layered business core with no AI |
| Understand first | Type hints, dataclasses vs pydantic, exceptions, TDD, dependency injection, money as integers or Decimal |
| Coding assignment | Models, menu service, pricing, order service, domain errors, in-memory repository |
| Files | src/pizzapilot/domain/models.py, domain/errors.py, services/menu.py, services/pricing.py, services/orders.py, data/menu.json, matching tests |
| Required tests | Unit and table-driven tests; at least 90% coverage of domain and services; no I/O in services |
| Definition of done | All F-01 to F-06 acceptance criteria met; you can explain the layering aloud |
| Interview questions | Where does validation belong? How do you test the order service without a database? Why not floats for money? |
| Practical exercise | Swap the in-memory repository for a JSON-file repository without editing the service |
| Prerequisite for M2 | Services fully tested and import nothing from tools, graph, or LLM code |

## M2 LangChain tools and tool loop (week 3, about 14 h)

| Field | Content |
|---|---|
| Learning objective | Understand the full tool-calling lifecycle |
| Understand first | Messages, tokens, context window, JSON schema, tool-call and tool-result message pairing, who executes the tool |
| Coding assignment | Tool layer; hand-written loop with a scripted fake model; then a real model via LangChain (local or free) |
| Files | src/pizzapilot/tools/, llm/factory.py, loop/simple_loop.py, tests/tools, tests/loop |
| Required tests | Schema tests, scripted traces, invalid-argument injection, optional live test marked live |
| Definition of done | The model orders a pizza end to end; wrong arguments are recovered from |
| Interview questions | What does the model actually receive about a tool? Who runs it? What if the model invents a tool name? |
| Practical exercise | Draw one request on paper, then match it against a real trace |
| Prerequisite for M3 | Your fake-model loop works; do not start LangGraph before this |

## M3 LangGraph workflows (week 4, about 14 h)

| Field | Content |
|---|---|
| Learning objective | Explicit state and control flow |
| Understand first | State machines, state schema, reducers, conditional edges, workflow vs agent |
| Coding assignment | Deterministic order graph; substitution routing; fan-out and join; one agent node |
| Files | src/pizzapilot/graph/state.py, nodes.py, routing.py, builder.py, tests/graph |
| Required tests | One test per edge and branch; bounded-loop test; merge-order test |
| Definition of done | Every route covered by a test; graph always terminates |
| Interview questions | Why not plain if/else? When is a graph overkill? What does a reducer do when two nodes write one key? |
| Practical exercise | Render the graph from code and hand-trace a failure path |
| Prerequisite for M4 | Green routing test suite |

## M4 Persistence and human approval (weeks 4-5, about 12 h)

| Field | Content |
|---|---|
| Learning objective | Durable, resumable, safe workflows |
| Understand first | Checkpoints, threads, interrupts, idempotency keys, at-least-once execution |
| Coding assignment | Checkpointer; approval interrupt before payment; idempotent order creation |
| Files | graph/persistence.py, graph/approval.py, services/idempotency.py, tests/persistence |
| Required tests | Restart-resume; approve, reject, timeout; duplicate resume creates one order |
| Definition of done | Payment is unreachable without approval, even on replay |
| Interview questions | What if the process crashes after the side effect but before the checkpoint? Which nodes re-run on resume? |
| Practical exercise | Kill the process mid-run and resume it |
| Prerequisite for M5 | Idempotency tests pass |

## M5 Agent harness and security (weeks 5-6, about 14 h)

| Field | Content |
|---|---|
| Learning objective | Build the controls around the loop |
| Understand first | Allowlists, step budgets, trust boundaries, prompt injection, least privilege, OWASP LLM risks (read it) |
| Coding assignment | Custom harness; retry and timeout policy; context trimming; authorization; injection corpus; audit log |
| Files | harness/loop.py, policy.py, context.py, guardrails.py, security/authz.py, tests/security |
| Required tests | Policy violations, fault injection, authorization matrix, injection corpus |
| Definition of done | Every hostile case is blocked and logged |
| Interview questions | What is the blast radius if the model is fully compromised? Which retries are unsafe? |
| Practical exercise | Write 10 attacks; each must fail safely |
| Prerequisite for M6 | Harness enforces policies and tests prove it |

## M6 Multi-agent systems (weeks 6-7, about 12 h)

| Field | Content |
|---|---|
| Learning objective | Know when delegation helps and when it does not |
| Understand first | Supervisor and handoff patterns, shared vs isolated state, cost of coordination |
| Coding assignment | Measure single-agent baseline first; supervisor with specialists; write the ADR |
| Files | agents/supervisor.py, menu_agent.py, order_agent.py, docs/adr/ |
| Required tests | Routing, tool isolation, aggregation |
| Definition of done | ADR compares single vs multi on accuracy, cost, latency |
| Interview questions | Name three signs a multi-agent design is unnecessary |
| Practical exercise | Find one scenario where single wins and one where multi wins |
| Prerequisite for M7 | Baseline numbers recorded |

## M7 Memory and RAG (week 7, about 10 h)

| Field | Content |
|---|---|
| Learning objective | Put the right data in the right store |
| Understand first | Embeddings, similarity search, chunking, retrieval evaluation, checkpoint vs memory |
| Coding assignment | Preference store; RAG over menu and FAQ; storage ADR |
| Files | memory/, rag/, data/faq/ |
| Required tests | Top-k retrieval, memory boundary, stale-memory handling |
| Definition of done | Retrieval quality is measured, not eyeballed |
| Interview questions | Why not put the whole menu in the prompt? When is a relational DB enough? |
| Practical exercise | Find a query where RAG fails and explain why |
| Prerequisite for M8 | Storage ADR written |

## M8 Evaluation and observability (weeks 7-8, about 10 h)

| Field | Content |
|---|---|
| Learning objective | Make quality and cost measurable |
| Understand first | Metrics, labeled datasets, tracing, thresholds |
| Coding assignment | Eval dataset and runner; tracing; cost tracker; CI regression gate |
| Files | evals/dataset.jsonl, evals/runner.py, observability/ |
| Required tests | Runner on fake model; trace shape; gate behavior |
| Definition of done | A deliberate regression fails CI |
| Interview questions | Which metric would you alert on, and why? |
| Practical exercise | Change a prompt and show the metric delta |
| Prerequisite for M9 | Baseline report committed |

## M9 MCP and A2A (week 8, about 8 h)

| Field | Content |
|---|---|
| Learning objective | Integrate across process boundaries |
| Understand first | MCP clients, servers, tools, resources, prompts; trust; A2A concepts. Read the current MCP docs: the SDK is on a new major version |
| Coding assignment | MCP server for menu and order tools; agent client under the allowlist; optional A2A sketch |
| Files | integrations/mcp/server.py, client.py, experiments/a2a/ |
| Required tests | In-process client tests; allowlist enforcement |
| Definition of done | The same tools work directly and via MCP |
| Interview questions | When is MCP overkill? Why treat MCP tools as untrusted? |
| Practical exercise | Connect a third-party MCP client to your server |
| Prerequisite for M10 | Harness treats MCP tools as untrusted |

## M10 Framework comparisons (stretch, about 8 h)

| Field | Content |
|---|---|
| Learning objective | Evaluate frameworks without contaminating core |
| Understand first | Deep Agents planning and delegation; Semantic Kernel agent abstractions |
| Coding assignment | Re-implement one workflow in experiments/deep_agents and experiments/semantic_kernel; run the same evals |
| Required tests | Shared eval dataset |
| Definition of done | Comparison table: code size, accuracy, control, debuggability, dependency weight |
| Interview questions | What would make you adopt a framework? |
| Practical exercise | Write a when-I-would-not-use-it paragraph for each |
| Prerequisite for M11 | Core stays free of experiment dependencies |

## M11 API and production (stretch, about 12+ h)

| Field | Content |
|---|---|
| Learning objective | Ship it |
| Understand first | Async Python, auth, queues, containers, SLOs |
| Coding assignment | FastAPI service, auth, background jobs, Docker, CI/CD, load test, runbook |
| Files | api/, Dockerfile, deploy/, docs/RUNBOOK.md |
| Required tests | API tests, auth tests, load script |
| Definition of done | Staging or dry-run deploy works; p95 reported |
| Interview questions | Where does it break first at 100x load? |
| Practical exercise | A load test that finds the real bottleneck |
| Prerequisite | Portfolio write-up of trade-offs |
