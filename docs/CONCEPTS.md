# Concept Index

Columns: what it means and why it exists | where it appears in PizzaPilot and which milestone teaches it | how to test or demonstrate it | common misconception | interview question.

## Python and software engineering

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| Functions, type hints | Small units with declared inputs and outputs; types catch mistakes early | Services (M1) | mypy passes; unit tests | Type hints are enforced at runtime | What does mypy check that pytest cannot? |
| Exceptions | Signal failure without returning magic values | Domain errors (M1) | Test that bad input raises the right error | Catch everything to be safe | When should you catch vs let propagate? |
| Data models and validation | Reject bad data at the boundary | Menu, order models (M1) | Invalid-construction tests | Validation belongs only in the UI | Where do you validate and why there? |
| Dependency injection | Pass collaborators in instead of creating them | Order service gets a repository (M1) | Swap a fake repository in tests | Needs a framework | How does DI make testing easier? |
| Separation of concerns | Each layer has one job | Services vs tools vs graph (M1-M3) | Import-direction check | More layers means better design | What belongs in a tool vs a service? |
| Unit and integration tests, mocking, TDD | Prove behavior at different scopes | All milestones | Test pyramid in docs/TESTING.md | Mocks prove the system works | What should you never mock? |
| Git, PRs, CI | Safe collaboration and automatic checks | M0 onward | Failing CI blocks a PR | CI replaces review | What should block a merge? |

## LLM and LangChain

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| LLMs, prompts, messages | The model maps a message list to the next message | Chat loop (M2) | Inspect real message traces | The model remembers between calls | What is actually sent on every call? |
| Tokens and context window | Cost and input limit are measured in tokens | Context trimming (M5) | Token-budget test | Bigger window means no need to manage context | What happens when the window overflows? |
| Tool definitions and schemas | Name, description, and typed arguments the model sees | Tool layer (M2) | Schema snapshot tests | The model reads your Python code | What does the model know about a tool? |
| Tool selection and execution | The model requests; your code runs | Harness (M2, M5) | Scripted fake-model traces | The model executes tools | Who executes a tool call? |
| Structured output | Constrain the model to a schema | Intent parsing (M2-M3) | Schema validation tests | Valid JSON means correct content | How do you handle schema-valid but wrong output? |
| Provider abstraction | One interface over many model vendors | llm/factory (M2) | Same test with fake and real model | Providers behave identically | What leaks through an abstraction? |
| Tool loops, sequential and parallel calls | Repeat call-observe until done; independent calls can batch | Loop (M2) | Multi-call traces | Parallel is always faster | When must calls be sequential? |
| Invalid arguments and tool failures | Return a clear error so the model can retry | Failure handling (M2) | Failure-injection tests | Errors should crash the run | What should the model see on failure? |

## LangGraph and workflow orchestration

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| StateGraph, nodes, edges, START, END | Workflow as an explicit graph over shared state | Order graph (M3) | Render the graph; route tests | Graphs are only for agents | Why a graph over nested ifs? |
| State schema, updates, reducers | Typed state and rules for merging writes | Graph state (M3) | Two nodes writing one key | Nodes mutate state in place | What does a reducer decide? |
| Conditional routing, loops, termination | Choose the next node from state; bound loops | Substitution (M3) | One test per branch | Loops terminate by themselves | How do you guarantee termination? |
| Fan-out and join | Run steps in parallel then merge | Availability checks (M3) | Order-independence test | Parallel results arrive in order | What if one branch fails? |
| Deterministic workflow vs agent | Fixed paths vs model-chosen paths | Agent node (M3) | Compare accuracy and cost | Agents are always better | When is a fixed workflow enough? |
| Checkpointing, threads, resume | Save state per thread to continue later | Persistence (M4) | Kill and resume | Checkpoint equals memory | What is a thread id for? |
| Interrupts and human approval | Pause before risky steps until a human decides | Pre-payment approval (M4) | Approve, reject, timeout tests | Prompting the user in text is enough | What happens on replay after approval? |

## Agent harness engineering

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| Execution loop, observe-act | Cycle of model call, tool run, observation | Harness (M2, M5) | Trace tests | The loop is the model | Where do you stop the loop? |
| Planning and task decomposition | Split a goal into steps | Multi-item orders (M5-M6) | Plan-quality eval cases | More planning is always better | When does planning add cost without value? |
| Allowlists, max steps, termination | Hard limits the model cannot override | Policy (M5) | Policy-violation tests | A prompt instruction is a control | Why enforce in code, not in the prompt? |
| Context management | Trim or summarize history deliberately | Context (M5) | Order state survives trimming | Truncate the oldest messages | What must never be trimmed? |
| Guardrails and authorization | Validate input and output; check who may do what | Authz (M5) | Authorization matrix | The model can be trusted with identity | Where is user identity taken from? |
| Retries, timeouts, fallbacks | Handle transient failure safely | Reliability (M5) | Fault injection | Retry everything | Which errors are safe to retry? |
| Idempotency | Same request, same effect once | Order creation (M4-M5) | Duplicate-request test | Idempotent means read-only | How do you pick an idempotency key? |

## Multi-agent systems

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| Single vs multi-agent | Split only when it measurably helps | Baseline and ADR (M6) | Eval comparison | More agents means smarter | What evidence justifies a split? |
| Specialists and supervisor | Narrow agents with restricted tools plus a router | Supervisor (M6) | Routing and tool-isolation tests | Specialists share everything | What does the supervisor see? |
| Delegation, handoffs, communication | Pass a task and typed result across agents | M6 | Contract tests | Pass full chat history | What should a handoff contain? |
| Shared vs isolated state | Isolation limits blast radius and token use | M6 | State-leak tests | Shared state is simpler and safer | What can go wrong with shared state? |
| Sequential vs parallel agents | Order vs concurrency trade-off | M6 stretch | Aggregation tests | Parallel always cuts latency | How do you merge conflicting results? |
| When multi-agent is unnecessary | Simple tasks, tight budgets, hard debugging | ADR (M6) | Single agent wins a case | Complex problem needs many agents | Name three signs you do not need it |

## Memory and retrieval

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| Conversation history, short-term state | What this run needs right now | Graph state (M3-M4) | Resume test | History is memory | What lives in state vs storage? |
| Long-term memory, persistent storage | Facts that outlive a run | Preferences (M7) | Cross-thread test | Store everything | What should you not remember? |
| Checkpointing vs memory | Run recovery vs knowledge | M4 and M7 | Boundary doc | They are the same | Why separate stores? |
| Embeddings, vector search, RAG | Retrieve similar text to ground answers | FAQ and allergens (M7) | Top-k quality tests | RAG removes hallucination | How do you measure retrieval quality? |
| Relational vs vector vs app state | Exact and transactional vs fuzzy vs ephemeral | Storage ADR (M7) | Experiment | Vector DB for everything | Where do orders belong? |

## Interoperability and frameworks

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| MCP: clients, servers, tools, resources, prompts | Standard way to expose tools and context across processes | MCP server and client (M9) | In-process client test | MCP makes tools safe | Why treat MCP tools as untrusted? |
| A2A concepts | Agents in different systems exchange tasks across a boundary | Optional experiment (M9) | Contract test | A2A replaces MCP | How does A2A differ from tool calling? |
| LangGraph vs custom harness | Framework features vs full control | Compare in M5 | Same behavior both ways | Frameworks are always better | What do you lose with a framework? |
| Deep Agents | Planning, delegation, long-running tasks packaged | Comparison (M10) | Same eval run | Replaces design work | When would you adopt it? |
| Semantic Kernel | Another agent and orchestration abstraction set | Comparison (M10) | Same eval run | Equivalent to LangChain | What is the migration cost? |
| Evaluating frameworks | Compare on the same evals with a dependency budget | M10 | Comparison table | Pick by popularity | What is your adoption criterion? |

## Evaluation and production architecture

| Concept | Meaning and why | Where (milestone) | Test or demo | Misconception | Interview question |
|---|---|---|---|---|---|
| Unit, integration, regression, end-to-end evals | Different scopes catch different bugs | M1-M8 | docs/TESTING.md | One test type is enough | What does each layer catch? |
| Tool-selection accuracy, task completion | Did it pick the right tool and finish | Evals (M8) | Dataset report | Accuracy equals quality | Which metric would you gate on? |
| Tracing, logging, metrics, observability | Reconstruct what happened | M8 | Trace-shape test | Logs are enough | What goes in a trace span? |
| Tokens, latency, cost, reliability | Operating economics | M8 | Counters and benchmarks | Cheaper model is cheaper overall | How do retries affect cost? |
| Authn, authz, secrets, privacy, injection defense, audit | Protect users and data | M5, M11 | Security tests | Filtering prompts is enough | What is the blast radius of a compromised model? |
| FastAPI, async, queues, databases, deployment, CI/CD, load testing, monitoring | Run it reliably | M11 | API and load tests | Local success means production-ready | Where does it break first? |
| ADRs, trade-off analysis, system design | Record decisions and reasons | docs/DECISIONS.md | ADR reviews | ADRs are paperwork | What would change your decision? |
