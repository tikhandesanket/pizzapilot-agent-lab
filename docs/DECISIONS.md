# Architecture Decisions to Investigate

Status values: Open (needs thinking), Experiment (needs a measured experiment before deciding), Decided (record the outcome as an ADR in docs/adr/). Nothing here is pre-decided. For each decision, write an ADR with context, options, evidence, decision, consequences, and what would change your mind.

| ID | Question | What to investigate | Status | Milestone |
|---|---|---|---|---|
| D-01 | Why LangGraph rather than a custom workflow engine? | Build the same order flow both ways; compare code size, resume support, testability, debugging, and dependency risk | Experiment | M3-M5 |
| D-02 | When should a workflow use an agent? | Compare a fully deterministic route with an agent node on ambiguous input: accuracy, cost, predictability | Experiment | M3 |
| D-03 | When is a multi-agent architecture justified? | Measure a single-agent baseline against supervisor plus specialists on the eval set | Experiment | M6 |
| D-04 | When is MCP useful? | Expose tools directly and via MCP; compare coupling, latency, security surface, reuse | Experiment | M9 |
| D-05 | What belongs in state versus memory? | Classify each piece of data by lifetime, owner, and size; test resume and cross-thread behavior | Open | M4, M7 |
| D-06 | How should retries avoid duplicate side effects? | Compare idempotency keys, at-most-once checks, and transactional outbox; test crash points | Experiment | M4-M5 |
| D-07 | Which data belongs in a relational database versus a vector database? | Run retrieval experiments on menu and FAQ; test whether exact lookup plus keyword search is enough | Experiment | M7 |
| D-08 | How should evaluation and observability influence architecture? | Identify which seams you need to measure; check that every decision is traceable and replayable | Open | M8 |
| D-09 | Where is the trust boundary for model output, tool output, and retrieved text? | Threat-model each hop; test with an injection corpus | Open | M5 |
| D-10 | How should human approval behave on timeout, rejection, and replay? | Specify behavior per case and test after process restarts | Experiment | M4 |
| D-11 | Which model provider strategy fits the project? | Local free model vs hosted; abstraction cost; reproducibility of evals | Open | M2 |
| D-12 | Sync, async, or queue-based execution? | Load test both models; measure p95 and failure behavior | Experiment | M11 |
| D-13 | Should an alternative framework (Deep Agents, Semantic Kernel) enter core? | Re-implement in experiments/ and compare on the same evals and dependency weight | Experiment | M10 |
| D-14 | How is the context window managed? | Compare trimming, summarization, and state-only context against order-correctness evals | Experiment | M5 |
