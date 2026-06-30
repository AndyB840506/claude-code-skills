# Execution

```
/megamind
    ↓
Load project-map (workspace context)
    ↓
Analyze task complexity
    ↓
Simple task → handle directly
Large task  → /parallel-workflow (multi-agent)
```

## Execution modes

| Task Type | Mode | Example |
|-----------|------|---------|
| Single file / single answer | Direct | "Fix this bug in auth.js" |
| Multiple independent items | Parallel | "Audit all 10 repos for security issues" |
| Sequential steps | Pipeline | "Generate → Review → Deploy" |
| Mixed | Hybrid | "Audit 5 repos, then summarize findings" |

## Steps

When `/megamind` is invoked:

### Step 0 — Check for a dedicated skill first
Before loading context or assessing complexity: does a named skill already cover this
task (episode-launch, freelance-gig, web-page-kit, episode-pipeline, etc. — check the
available-skills list)? If yes, use that skill directly and stop here — don't run the
rest of this workflow. Megamind only continues past this step for ad-hoc tasks with no
dedicated skill, or tasks that explicitly span 2+ independent repos/projects.

### Step 1 — Load context
Read `~/.claude/project-map.md` if it exists. Check its `Generated:` date — if it's
more than 14 days old, tell the user it may be stale and offer to run `/project-map`
before relying on it for routing decisions. If the file doesn't exist, suggest running
`/project-map` first. Use the map to identify which repos/projects are relevant before
decomposing — this prevents unnecessary agent spawns on unrelated projects.

### Step 2 — Understand the task
Ask what needs to be done if not clear from context.

### Step 3 — Assess complexity
- How many independent items are involved?
- Can subtasks run in parallel?
- Is there a dependency chain?

### Step 4 — Route
- **1 item or sequential steps** → handle directly
- **2+ independent items** → invoke `/parallel-workflow` with decomposed subtasks
- **Unknown scope** → ask a clarifying question before routing

### Step 5 — Execute and synthesize
Run the work. Collect all outputs. Present a unified final result.

---

## Tips

- Run `/project-map` once after setting up to build your workspace index.
- `/megamind` gets smarter the more complete your `project-map.md` is.
- For very large tasks (10+ subtasks), Megamind batches agents automatically.
