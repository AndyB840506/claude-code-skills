# Execution

```
User task
    ↓
Decompose into subtasks (independent units)
    ↓
Spawn N agents in parallel (one per subtask)
    ↓
Collect all results
    ↓
Synthesize into final output
```

When `/parallel-workflow` is invoked:

## Step 1 — Understand the task
Ask: *What do you want to parallelize?* If not clear from context, ask for:
- The task description
- The list of items to process (files, repos, episodes, etc.)
- The expected output format

## Step 2 — Decompose
Break the task into independent subtasks. Each subtask must be:
- Self-contained (no dependency on other subtasks)
- Clearly scoped (specific input → specific output)
- Describable in one sentence

Show the decomposition plan and ask for confirmation before spawning agents.

## Step 3 — Spawn agents in parallel
Launch all subtask agents in a **single message** with multiple Agent tool calls.
Pass `run_in_background: true` to each Agent call — without this, agents run sequentially
instead of in parallel. Each agent receives:
- Its specific subtask description
- The input it needs to process
- The expected output format
- Instruction to return a concise result

## Step 4 — Synthesize
Collect all agent results and combine into the final output.
Present as a unified response — not a list of raw agent outputs.

## Step 5 — Summary
Report: how many agents ran, what was processed, what was produced.

---

## Rules

- Never run agents sequentially when they can run in parallel
- Max recommended parallel agents: 10 (beyond that, split into batches)
- If subtasks have dependencies, run dependent ones after the parallel batch
- Always confirm the decomposition plan before spawning
