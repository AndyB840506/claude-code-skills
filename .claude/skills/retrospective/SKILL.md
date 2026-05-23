---
name: retrospective
description: "Analyze session to extract learnings, propose skill updates, ask for confirmation before applying. Detects corrections, redone work, missing steps, patterns that worked. Proposes specific diffs with user approval required. Triggers: retrospective, what did we learn, update skills, what did we improve, lessons learned, session review."
---

# Retrospective — Learn and Update Skills

Analyzes the current session to extract reusable learnings and proposes updates to skill files.

**Critical:** Always asks for explicit user approval before applying ANY changes to skill files.

---

## Quick Start

```
/retrospective
/retrospective skill-name
```

---

## How It Works

**5-Step Workflow:**

1. [Extract Signals](workflows/extract.md) — Identify learnings from this session
2. Map to Skills — Which skills need updating
3. Propose Diffs — Show specific changes with before/after
4. [Ask Confirmation](workflows/confirm.md) — Wait for explicit approval
5. Apply Changes — Update skills if approved

---

## When to Use

- After completing a multi-step workflow
- When you corrected my approach multiple times
- When something was redone 3+ times
- When you ask "what did we learn"
- After `/session-close` workflow

---

## See Also

- [What to Encode](docs/what-to-encode.md) — Process changes, anti-patterns, tool behavior
- [Auto-Suggest](docs/auto-suggest.md) — When to suggest retrospective vs when to skip

---

## EXECUTION

You have invoked `/retrospective`. Now execute the 5-step workflow:

1. **Extract Signals** — Scan conversation for corrections, redone work, missing steps, what worked well
2. **Map to Skills** — Identify which skills need updating based on learnings
3. **Propose Diffs** — Generate specific changes with reasoning for each skill
4. **Ask Confirmation** — Present all changes and wait for user approval (or confirm "no updates needed")
5. **Apply Changes** — Update skill files if user approved; otherwise proceed to next session step

See [Full Workflow](workflows/extract.md) for detailed step-by-step instructions.

**Result:** Skills updated with session learnings (if approved), or next step ready if no changes proposed.
