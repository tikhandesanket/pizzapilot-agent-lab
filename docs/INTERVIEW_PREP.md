# Interview Prep

Every prompt asks you to justify a trade-off. Answer aloud or in writing in your own words, using evidence from your own code and tests. If you cannot point at a test or a trace from this repository, you do not yet own the answer.

## M0-M1 Engineering fundamentals

Q1. Your order service takes a repository as a parameter. A teammate says a global database object is simpler. Argue both sides and say what you would measure.

Q2. Prices are stored as integers or Decimal. Describe a real bug floats would cause and the test that catches it.

Q3. Where should the rule "maximum 20 pizzas per order" live: model, service, tool, or prompt? Defend your choice and name the failure if it lives in the wrong place.

## M2 Tool calling

Q4. Draw what the model receives and returns in one tool call. Where can a hallucinated argument enter and which layer stops it?

Q5. A tool fails with a validation error. Compare returning the error to the model, retrying silently, and aborting. When is each right?

Q6. You have 5 tools vs 25 tools. How does tool count affect selection accuracy, tokens, and cost, and how would you test it?

## M3 Workflows and LangGraph

Q7. Your graph and a plain function with if statements both implement the order flow. List the exact conditions under which the graph earns its complexity.

Q8. Two parallel nodes write to the same state key. What can go wrong and how does a reducer fix it? Show your test.

Q9. Which steps of the order flow should be agentic and which deterministic? Justify using cost, predictability, and failure impact.

## M4 Persistence and human approval

Q10. A crash happens after the order is placed but before the checkpoint is written. What does resume do? How did you make this safe?

Q11. Distinguish checkpoint, thread, and long-term memory with one PizzaPilot example each.

Q12. The user approves, then the approval is replayed. Design the behavior and the test. What if approval arrives after a long timeout?

## M5 Harness and security

Q13. Why enforce max steps and an allowlist in code instead of the prompt? Describe an attack that succeeds if you rely on the prompt.

Q14. A menu item description contains hidden instructions. Trace how your system treats it at every layer and where it is finally contained.

Q15. Which errors are safe to retry? Give one example where retrying causes harm and how idempotency changes the answer.

Q16. If the model is fully compromised, what is the worst it can do in your system? How would you shrink that blast radius further?

## M6 Multi-agent

Q17. Present your baseline vs multi-agent numbers. Would you ship the multi-agent version? What would change your mind?

Q18. Should specialists share message history with the supervisor? Compare cost, leakage risk, and debuggability.

Q19. Give three signs that a multi-agent design is unnecessary for a given task.

## M7 Memory and retrieval

Q20. For orders, preferences, allergen FAQs, and conversation summaries, choose a store for each and justify it. Where would a vector database be wrong?

Q21. Your retrieval returns the wrong allergen passage. How do you detect, measure, and prevent harm?

Q22. What goes stale in long-term memory, and how do you handle that?

## M8 Evaluation and observability

Q23. Design three metrics for this agent and explain which you would gate CI on and which you would only monitor.

Q24. A prompt change improves accuracy 3 percent but doubles cost. Decide, with your reasoning.

Q25. A user complains an order was wrong. Which logs and traces let you reconstruct what happened?

## M9-M10 Integrations and frameworks

Q26. You expose menu tools through MCP. What did you gain and what new risks appeared? When would direct function calls be better?

Q27. Compare A2A and MCP in one PizzaPilot scenario.

Q28. Your Deep Agents or Semantic Kernel experiment matches core accuracy with less code. Do you adopt it? State your criteria.

## M11 Production

Q29. Where does your system fail first at 100 times traffic? Show evidence from your load test.

Q30. Compare synchronous API, background job with polling, and streaming for a 30-second agent run.

Q31. Describe your rollout, monitoring, and rollback plan for a new model version.

## Portfolio walkthrough

Q32. In five minutes, explain the architecture, the three hardest bugs you hit, and one decision you reversed after an experiment.
