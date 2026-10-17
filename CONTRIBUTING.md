# Contributing and Workflow

This is a solo learning repository. The rules below exist to build professional habits.

## Mentoring rules

You write all application code. A mentor gives tasks, explains concepts, provides pseudocode or function contracts, and reviews your code and tests. Hints are graduated: concept first, then a small hint, then a minimal snippet only if you ask. An issue is never complete because code exists; it is complete when tests pass and you can explain your design in your own words.

## Branch and commit conventions

| Item | Convention |
|---|---|
| Branch name | feat/ISSUE-short-slug, fix/ISSUE-short-slug, docs/ISSUE-short-slug, test/ISSUE-short-slug |
| Commit format | Conventional Commits: type(scope): summary, for example feat(menu): add availability check |
| Types | feat, fix, test, docs, refactor, chore, ci |
| Commit size | One logical change; tests in the same PR as the code |
| Pull request | One issue per PR, uses the PR template, links the issue with Closes # |
| Merge | Squash merge after CI is green; delete the branch |

## Labels

learning, python, langchain, langgraph, agent-harness, multi-agent, security, testing, observability, mcp, architecture, documentation, good-first-task, plus priority labels p0, p1, p2.

## Milestones

M0 Setup, M1 Deterministic core, M2 LangChain tools, M3 LangGraph workflows, M4 Persistence and approval, M5 Harness and security, M6 Multi-agent, M7 Memory and RAG, M8 Evaluation and observability, M9 MCP and A2A, M10 Framework comparisons, M11 API and production.

## CI plan (you build this in the first issue)

On every pull request and push to main: install with pip install -e ".[dev]", run ruff check, ruff format --check, mypy on src, and pytest. The default pytest run must not need network access or API keys; live-model tests use the live marker and run only on demand. From M8, add an offline evaluation gate.

## Definition of done (every issue)

- [ ] Acceptance criteria in the issue are all checked
- [ ] Tests were written first or alongside, and fail when the feature is broken
- [ ] pytest, ruff, and mypy pass locally and in CI
- [ ] No network or API key needed for the default test run
- [ ] Docs and the README status table are updated
- [ ] No secrets or personal data committed
- [ ] The PR description explains design choices in your own words
- [ ] You can answer the issue's review questions without looking at the code
