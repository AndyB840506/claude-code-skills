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

**Include EXECUTION sections in every skill you generate.** This is what makes skills actually work.
