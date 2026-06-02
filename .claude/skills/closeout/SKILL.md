---
name: closeout
description: "End-of-session closeout ritual: runs retrospective, skill-kit-auditor, and handoff in sequence. Triggers: closeout, close out, cerrar sesion, session close, end session, finalizar sesion, wrap up, cierre de sesion."
---

# Session Closeout

Ritual de cierre de sesion. Runs the three-step sequence below in order and produces a clipboard-ready handoff before closing.

1. Run the retrospective workflow and apply learnings.
2. Run skill-kit-auditor and apply approved fixes.
3. Build a clipboard-ready handoff.

## Steps

### 1. Retrospective
Invoke the `retrospective` skill. Wait for it to complete and present proposed learnings. Apply any approved updates to memory or skill files before moving on.

### 2. Skill-kit audit
Invoke the `skill-kit-auditor` skill. Present the prioritized findings. Apply fixes that the user approves before moving on.

### 3. Handoff
Invoke the `handoff` skill to build a clipboard-ready context block summarizing: what was done this session, decisions made, files changed, and clear next steps. Confirm with the user before closing.

## Rules

- Do not skip steps or run them out of order.
- Do not generate the handoff until retrospective learnings and audit fixes are applied (or explicitly skipped by the user).
- If the user says "skip X", skip that step and continue with the next.
