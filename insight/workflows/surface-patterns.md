# Surface Patterns Workflow

Gather → cluster → propose → apply. The goal is to turn repeated friction into a
durable rule before it costs time again.

## 1. Gather

- Read `MEMORY.md` (the index) and skim the `feedback_*` + `reference_*` files it
  points to — these already encode past friction.
- List `.agents/handoff/` and read the **5–8 most recent** handoffs (by date).
  Focus on their "Notes / Gotchas", "Where We Paused / Blockers", and "Questions"
  sections — that's where friction lives.
- Optional focus arg (e.g. `/insight web`, `/insight infra`) — narrow to handoffs
  and memories matching that topic.

## 2. Cluster

Group what you find into a SMALL number of named patterns (aim for 3–6, not 15).
A pattern qualifies only if it has **≥2 real occurrences across sessions/projects**
— cite them. A single occurrence is a retrospective item, not a trend; drop it.

Common pattern families to check for (don't force-fit):
- **External-service state I can't see** — guessing at the state of a Google/Vercel/DO
  resource instead of asking the user to confirm it.
- **Tier/limit found mid-build** — chose a tool, then hit a free-plan wall.
- **Wrong ID / URL pasted** — retyped instead of copied from source.
- **Cross-platform rendering** — emoji/encoding/path that breaks on Windows.
- **Recurring copy/design tell** — same correction across multiple builds.
- **Instrument not validated** — built a theory on an unverified tool/stack reading.

## 3. Propose

Present a compact table the user can act on:

| Pattern | Evidence (sessions) | Root cause | Proposed fix | Where it lands |
|---|---|---|---|---|

- **One fix per pattern** — the smallest durable change (a rule line, a checklist
  item, a memory entry, a tool), not a new framework.
- If a memory/skill **already covers** the pattern, the fix is "fire it earlier" or
  "tighten the existing rule" — not a new file.
- Mark patterns already fully handled as ✅ (no action) so the user sees they're closed.

## 4. Apply (after approval)

- Let the user pick which fixes to apply (they may defer some).
- For each approved fix:
  - **Rule/checklist** → edit the relevant skill file (e.g. a `docs/*.md` or workflow).
  - **Memory** → write/update a `feedback_*` or `reference_*` file + add the one-line
    MEMORY.md pointer. Update an existing file rather than duplicating.
  - **Tool** → if it's a real new command, build it per skill-management (router <50
    lines + workflow); otherwise note it as a backlog idea, don't overbuild.
- Confirm what changed in 2–3 lines. Do NOT commit/push here — that's the user's call
  or the `/session-close` handoff step.
