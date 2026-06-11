---
name: session-close
description: "Automated 3-step session close: retrospective + skill management audit + handoff (writes .agents/handoff/*.md, commits, pushes to GitHub). Triggers: session close, end session, closing session, session wrap-up, wrap up, end-of-session, cierre de sesión, cerrar sesión, finalizar sesión, terminar sesión, fin de sesión, cerrar proyecto, guardar y cerrar."
---

# Session Close — Automated Complete Workflow

Automated 3-step workflow. Each step shows results and waits for your confirmation before continuing.

**Execution sequence:** Retrospective → Skill Management Audit → Handoff

---

## What It Does

1. **Retrospective** — Extract learnings from the session, propose skill updates
2. **Skill Management Audit** — Audit the skill kit against `skill-management/SKILL.md`'s checklist (structure, redundancies, oversized files)
3. **Handoff** — Write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub

Everything is backed up to GitHub via the handoff commit. A `claude-bootstrap` sync (separate, manual) keeps `~/.claude/` config in sync across machines if you ever start fresh — see that repo for setup.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)
✓ Audit findings reviewed and fixes applied (approved by you)
✓ Handoff document written, committed, and pushed to GitHub

---

## When to Use

- End of major sessions — after creating/modifying skills or fixing bugs
- End of day — batch daily changes into one session close
- Before handing off — ensure everything is documented and backed up

---

## EXECUTION

When `/session-close` is invoked, run all 3 steps in order:

1. Invoke `/retrospective` → show learnings → ask user to confirm changes → apply if approved
2. Audit the skill kit directly against the checklist in `skill-management/SKILL.md` (trigger overlaps, duplicate content, structure violations, files >50 lines) → show results → ask user to confirm fixes → apply if approved
3. Invoke `/handoff` via `Skill("handoff")` → write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub (no confirmation needed — handoff is always safe to write)

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.
