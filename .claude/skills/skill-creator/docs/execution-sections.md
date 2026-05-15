# EXECUTION Sections — Making Skills Actually Work

For your skill to actually *execute* (not just display documentation), SKILL.md must include an `## EXECUTION` section with explicit instructions.

**Without EXECUTION:** Skill shows documentation but doesn't trigger action  
**With EXECUTION:** Skill actually performs the process when invoked

---

## Template

```markdown
## EXECUTION

You have invoked `/your-skill`. Now perform the process:

### Step 1: [First action]
[What to do, what to look for]

### Step 2: [Second action]
[What to do, what to look for]

[Continue for all steps...]

---

**Process complete!** [Summary of what was accomplished]
```

---

## Example (from real skill: retrospective)

```markdown
## EXECUTION

You have invoked `/retrospective`. Now perform the analysis:

### Step 1: Extract Signals
Scan conversation for: corrections, redone work, missing steps, what worked well

### Step 2: Map to Skills
Identify which skills need updating

### Step 3: Propose Changes
Show specific diffs

### Step 4: Ask Confirmation
Wait for user approval

### Step 5: Apply Changes
Update files if approved

---

**Retrospective complete!**
```

---

## Key Principles

- **Explicit instructions** — Each step tells the AI exactly what to do
- **Clear outcomes** — Step describes both action and expected result
- **No assumptions** — Don't assume the AI understands context from docs
- **Complete flow** — Cover all steps from start to finish
- **Summary at end** — Confirm completion with a final message

---

## Critical: Imperative vs. Informative

**WRONG (Informative — describes what should happen):**
```markdown
## EXECUTION

Step 5 Google Drive Sync should attempt to sync if configured.
Step 6 Context should be compressed for next session.
```

**CORRECT (Imperative — tells the AI what to actually do):**
```markdown
## EXECUTION

### Step 5: Google Drive Sync
**ACTION:** Attempt to sync handoff to Google Drive if MCP is configured
- If available: sync the document
- If not available: report "Google Drive MCP not installed - sync skipped"
- **Result:** Continue to Step 6 immediately.

### Step 6: Compact Context
**ACTION:** Execute compact command
```
/compact
```
**MUST EXECUTE:** This is not optional.
- Report: "Context compressed."
- **Continue to Step 7 immediately**
```

**Why:** Multi-step workflows need later steps to execute *in the moment* to validate that earlier changes didn't break the process. Use ACTION directives and MUST EXECUTE markers to signal mandatory execution.

---

## Multi-Step Workflow Pattern

For orchestrated workflows (like session-close), follow this structure:

1. **User-confirmation steps** (1-N) — Can be skipped/rerun, wait for user approval
2. **Sequential execution steps** (N+1 to end) — MUST execute in sequence, no waiting
3. **Final confirmation step** (if needed) — Ask before last action (e.g., clear screen)

Mark later steps with **ACTION:** directives and **MUST EXECUTE:** where needed.

---

## When to Use ACTION Directives

| Step Type | Use ACTION? | Example |
|-----------|-----------|---------|
| User-confirmation (waits for approval) | No | `/retrospective` — wait for user approval |
| Immediate execution (no waiting) | Yes | `/compact` — execute immediately |
| Mandatory step (can't be skipped) | Yes with MUST EXECUTE | `clear` command after user confirms |
| Optional fallback | Yes | "If MCP available: sync; if not: report skipped" |

**Rule:** Use ACTION directives for steps that execute immediately or must happen regardless of user interaction.

---

## Real-World Example: session-close Workflow

```markdown
## EXECUTION

### Step 1: Retrospective (User-confirmation, no ACTION)
/retrospective
- Wait for user approval
- If YES: apply changes; If NO: continue to Step 2

### Step 4: Handoff (Immediate execution, no ACTION for main step)
/handoff
- Generates document and commits to GitHub
- Proceed to Step 5 immediately

### Step 5: Google Drive Sync (Immediate execution, USE ACTION)
**ACTION:** Attempt to sync handoff to Google Drive if MCP is configured
- If available: sync the document
- If not available: report "sync skipped"
- Continue to Step 6 immediately

### Step 6: Compact Context (Immediate execution, USE ACTION + MUST EXECUTE)
**ACTION:** Execute compact command
/compact
**MUST EXECUTE:** This is not optional.
- Report: "Context compressed."
- Continue to Step 7 immediately

### Step 7: Clear Screen (Final confirmation, USE ACTION for fallback)
**ACTION:** Ask user for confirmation
Have you pasted the handoff summary in your next session? [yes/no]
- **If YES:** Execute `clear` command
- **If NO:** Report completion message
```

**Pattern:** User-confirmation steps don't need ACTION. Immediate/mandatory steps do.

---

**Include EXECUTION sections in every skill you generate.** Use ACTION directives for immediate and mandatory steps only.
