---
name: session-close
description: "Automated 6-step session close: retrospective + skill management audit + handoff (writes .agents/handoff/*.md, commits, pushes to GitHub) + skills repo sync (commits/pushes ~/.claude/skills) + continuity sync (backs up ~/.claude memory to GitHub) + memory-audit auto-trigger when memory has grown. Triggers: session close, end session, closing session, session wrap-up, wrap up, end-of-session, cierre de sesión, cerrar sesión, finalizar sesión, terminar sesión, fin de sesión, cerrar proyecto, guardar y cerrar."
---

# Session Close — Automated Complete Workflow

Automated workflow — steps 3–6 run without asking first. **Sequence:** Retrospective → Skill Management Audit → Handoff → Skills Repo Sync → Continuity Sync → Memory Audit check

---

## What It Does

1. **Retrospective** — Extract learnings from the session, propose skill updates
2. **Skill Management Audit** — Audit the skill kit against `skill-management/SKILL.md`'s checklist (structure, redundancies, oversized files)
3. **Handoff** — Write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub
4. **Skills Repo Sync** — commit + push any skill edited in `~/.claude/skills` this session — Step 3's handoff commit is scoped to the handoff file only, so it never covers skill edits, even though `~/.claude/skills` and this project repo are two clones of the same remote (see INSTRUCTIONS.md)
5. **Continuity Sync** — Run the `claude-continuity` sync so `~/.claude/` memory + config are backed up to GitHub
6. **Memory + Skill-Kit Audit check** — Count memory files AND `SKILL.md` files vs `memory/.audit-baseline.json`; if memory grew ≥15 OR the skill count changed, auto-invoke `Skill("memory-audit")` right here (no confirmation needed to trigger it — `memory-audit` itself still gates applying any change on your approval, and now also scans the skill kit for corruption, not just memory)

Two remotes, three concerns covered: the shared skills/project remote (via Steps 3-4) and `claude-continuity`'s memory+config (Step 5) — together they mean a fresh machine can be fully restored. See [[feedback_always_backup_github]].

---

## When to Use

- End of major sessions — after creating/modifying skills or fixing bugs
- End of day — batch daily changes into one session close
- Before handing off — ensure everything is documented and backed up
- When a past session ended WITHOUT its close (e.g. a missing handoff) — run the full
  close now, don't just patch the handoff: the skipped close also skipped the continuity
  sync (memory unbacked since then) and the retrospective (unrecoverable once context clears)
- **Parallel sessions:** close each one (each retrospective is session-local) but
  SEQUENTIALLY — handoff + continuity sync push to shared repos and concurrent closes race.

---

## EXECUTION

When `/session-close` is invoked, run all 6 steps in order:

1. Invoke `/retrospective` → show learnings → ask user to confirm changes → apply if approved. Si el usuario pegó reglas o prompts durante la sesión, **reconciliarlos antes de seguir** — ver INSTRUCTIONS.md Step 1.
2. Audit the skill kit directly against the checklist in `skill-management/SKILL.md` (trigger overlaps, duplicate content, structure violations, files >50 lines) → show results → ask user to confirm fixes → apply if approved
3. Invoke `/handoff` via `Skill("handoff")` → write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub (no confirmation needed — handoff is always safe to write)
4. Skills repo sync (no confirmation needed — always safe): `cd "$env:USERPROFILE\.claude\skills"; git status --short`. If dirty, `git add -A; git commit -m "session-close: skill updates <date>"; git push origin main`. Report which skills changed, or "sin cambios" if clean.
5. Run the continuity sync (no confirmation needed — always safe): `cd "C:\Users\andre\repos\claude-continuity"; .\sync.ps1` (Mac/Linux: `bash sync.sh`). It copies `~/.claude/` memory + config into the repo and pushes to `origin master`. Report what it synced.
6. Memory + skill-kit audit check (no confirmation needed): compare the memory `.md` count and the `SKILL.md` count against `memory/.audit-baseline.json`. If memory grew ≥15 OR the skill count changed, invoke `Skill("memory-audit")` directly — actually run it, don't just suggest it (it gates applying changes on approval). Otherwise report the counts. Exact counting commands in INSTRUCTIONS.md Step 6.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.
