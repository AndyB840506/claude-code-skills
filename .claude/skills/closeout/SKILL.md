---
name: closeout
description: "Simplified 3-step session close: retrospective → skill-kit-auditor → handoff. Lightweight alternative to /session-close (which also includes prompt review and Google Drive backup). Triggers: closeout, close out. For full session close use /session-close."
---

# Session Closeout (Simplified)

Lightweight 3-step close: retrospective → skill-kit-auditor → handoff.
For the full 5-step close (includes prompt review + Google Drive backup), use /session-close.

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
