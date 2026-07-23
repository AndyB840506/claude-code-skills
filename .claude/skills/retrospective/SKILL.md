---
name: retrospective
description: "Analyze the current session to extract reusable learnings and propose updates to relevant skills. Covers ONE session — for patterns across many sessions use /insight, and for the full closing ritual use /session-close. Triggers: retrospective, retrospectiva, que aprendimos hoy, what did we learn, extraer aprendizajes, post-mortem de sesion, actualizar skills con lo aprendido, learnings de esta sesion, reproceso de hoy."
---

# Retrospective

Analyze the current session and extract learnings that should flow back into skills.

## When to Use

- After completing a multi-step workflow (e.g., deploy-preflight, episode-pipeline, web-page-kit)
- When the user says "retrospective", "what did we learn", "update skills"
- Agent should SUGGEST running this after any session where:
  - Work was redone more than once
  - User corrected the approach ("this is not great", "don't do that")
  - Steps were improvised that aren't in the skill

## Quick Start

```
/retrospective                    # Analyze current session
/retrospective video              # Focus on video skill learnings
/retrospective launch             # Focus on launch skill learnings
```

## Workflow

Follow `workflows/extract-and-apply.md` — extract signals, map to skills, propose
diffs, apply after approval.

## Auto-Suggest Convention

After completing any multi-step workflow, suggest `/retrospective` if: 2+ user
corrections happened, an artifact was regenerated 3+ times, or steps were improvised
that aren't in the skill. This is NOT automatic — the user decides whether to run it.

## Reference

- `docs/solution-quality.md` — what to/not encode + "Think Like Mario" first-principles
  checklist for proposed fixes
