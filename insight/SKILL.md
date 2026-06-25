---
name: insight
description: "Surface cross-session friction patterns and turn them into rules before they bite again. Reads MEMORY.md + recent handoffs, clusters recurring loops/corrections/rework across sessions, and proposes new rules, tools, or memory entries. Distinct from /retrospective (single session) and /session-close (closing ritual). Triggers: insight, what keeps biting us, recurring patterns, cross-session learnings, what slows us down, minimize loops, friction audit."
---

# Insight — Cross-Session Friction Finder

Look across many sessions (not just this one) to find the friction that keeps
recurring, and convert it into rules/tools BEFORE it costs time again.

## What It Does

- Reads `MEMORY.md` + the memory files it indexes, and the recent files in
  `.agents/handoff/`.
- Clusters recurring friction into a few named patterns (e.g. "external-service
  state I can't see", "free-tier limit found mid-build", "wrong ID/URL pasted").
- For each pattern: shows the evidence (which sessions/projects), names the
  root cause, and proposes ONE concrete fix — a new rule, a checklist item, a
  memory entry, or a tool.
- Applies approved fixes (writes/updates `feedback_*` memories, edits the right
  skill, adds MEMORY.md pointer).

## How It Differs

- `/retrospective` — extracts learnings from **one** session.
- `/session-close` — the end-of-session ritual (retrospective → audit → handoff).
- `/insight` — looks **across** sessions for what repeats. Run it occasionally,
  not every session.

## Workflow

Follow `workflows/surface-patterns.md` — gather → cluster → propose → apply.

## Rules

- **Evidence before proposal** — every pattern must cite ≥2 real occurrences. No
  speculative patterns from a single event (that's a retrospective, not a trend).
- **One fix per pattern** — propose the smallest durable change, not a framework.
- **No duplicate memories** — update an existing `feedback_*`/`reference_*` file if
  it already covers the pattern; only create new when none fits.
- **Apply only after approval** — show the full list first, let the user pick.
