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
2. [Map to Skills](workflows/map.md) — Which skills need updating
3. [Propose Diffs](workflows/propose.md) — Show specific changes
4. [Ask Confirmation](workflows/confirm.md) — Wait for explicit approval
5. [Apply Changes](workflows/apply.md) — Update skills if approved

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
