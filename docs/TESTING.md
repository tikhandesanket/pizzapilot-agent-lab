# Testing Strategy

Principles: tests come before an issue is marked done; the default test run needs no network and no API keys; live-model tests carry the pytest marker live and are excluded by default; every bug found gets a regression test; the model is replaced by a scripted fake wherever possible.

## Test types

| Type | What it proves | Tools and approach | Introduced |
|---|---|---|---|
| Pure Python unit tests | Services, pricing, validation behave correctly | pytest, parametrize, table tests, no I/O | M1 |
| Mocked tool tests | Tool wrappers pass arguments to services and shape results and errors; schema is stable | Fake services, schema snapshot tests | M2 |
| Scripted fake-model loop tests | The loop handles call, result, error, and termination | A fake model that returns a fixed sequence of messages | M2 |
| Graph routing tests | Each edge and branch is taken for the right state; loops are bounded | Build the graph with fake nodes; assert path taken | M3 |
| State and persistence tests | Checkpoints survive restart; reducers merge correctly | Temporary database file per test | M3-M4 |
| Human-approval tests | Side effects never happen before approval; reject and timeout paths; replay after approval makes one order | Interrupt, resume with approve, reject, nothing | M4 |
| Multi-agent tests | Supervisor routing, tool isolation per specialist, aggregation, no state leakage | Fake models per agent; assert allowed tools | M6 |
| Security tests | Authorization matrix; allowlist enforcement; prompt-injection corpus cannot trigger tools; secrets never logged | Table of hostile inputs with expected refusal | M5 |
| Failure-injection tests | Timeouts, transient and permanent tool errors, malformed model output, duplicate requests | Fault-injecting wrappers; assert retries and final state | M2, M5 |
| LLM evaluation datasets | Tool-selection accuracy and task completion on labeled cases | evals/dataset.jsonl, runner, report; offline with fake model, optional live run | M8 |
| Regression tests | Past bugs and quality do not return | Bug-linked tests; eval threshold gate in CI | M8 |
| Performance and cost benchmarks | Latency percentiles, tokens, cost per order, throughput | Benchmark script; load test against the API | M8, M11 |

## Evaluation dataset format (to design in M8)

Each case: id, user message, expected tool sequence, expected final state or answer properties, tags (happy path, ambiguity, injection, failure). Minimum 30 cases for the first baseline. Metrics: tool-selection accuracy, argument correctness, task-completion rate, steps used, tokens, latency, cost.

## CI plan

On every pull request run: pytest (default marker set, with coverage report), ruff check and ruff format check, mypy on src. Nightly or manual: live tests and the full evaluation run. From M8: the offline evaluation must stay above its recorded threshold.

## Coverage and quality expectations

Domain and services: at least 90 percent line coverage. Graph and harness: every branch and policy has a test. Coverage is a floor, not a goal; a test that cannot fail is not counted.

## Rules for writing tests

Name tests by behavior. Arrange, act, assert. One reason to fail per test. No sleeping on real time; inject a clock. No hidden network access. Fixtures create their own data. Tests must fail when the feature is broken: show this once by breaking the code on purpose.
