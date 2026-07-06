---
name: session-close
description: "Automated 5-step session close: retrospective + skill management audit + handoff (writes .agents/handoff/*.md, commits, pushes to GitHub) + continuity sync (backs up ~/.claude memory to GitHub) + memory-audit auto-trigger when memory has grown. Triggers: session close, end session, closing session, session wrap-up, wrap up, end-of-session, cierre de sesión, cerrar sesión, finalizar sesión, terminar sesión, fin de sesión, cerrar proyecto, guardar y cerrar."
---

# Session Close — Automated Complete Workflow

Automated workflow. Each step shows results and waits for your confirmation before continuing (steps 3–5 run without asking first — see below).

**Execution sequence:** Retrospective → Skill Management Audit → Handoff → Continuity Sync → Memory Audit check

---

## What It Does

1. **Retrospective** — Extract learnings from the session, propose skill updates
2. **Skill Management Audit** — Audit the skill kit against `skill-management/SKILL.md`'s checklist (structure, redundancies, oversized files)
3. **Handoff** — Write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub
4. **Continuity Sync** — Run the `claude-continuity` sync so `~/.claude/` memory + config are backed up to GitHub (memory lives OUTSIDE the skills repo, so the handoff push alone does NOT cover it)
5. **Memory + Skill-Kit Audit check** — Count memory files AND `SKILL.md` files vs `memory/.audit-baseline.json`; if memory grew ≥15 OR the skill count changed, auto-invoke `Skill("memory-audit")` right here (no confirmation needed to trigger it — `memory-audit` itself still gates applying any change on your approval, and now also scans the skill kit for corruption, not just memory)

The handoff commit backs up the project repo. The continuity sync (Step 4) backs up `~/.claude/` memory + config — the two together mean a fresh machine (or Mac) can be fully restored. See [[feedback_always_backup_github]].

---

## When to Use

- End of major sessions — after creating/modifying skills or fixing bugs
- End of day — batch daily changes into one session close
- Before handing off — ensure everything is documented and backed up

---

## EXECUTION

When `/session-close` is invoked, run all 5 steps in order:

1. Invoke `/retrospective` → show learnings → ask user to confirm changes → apply if approved
2. Audit the skill kit directly against the checklist in `skill-management/SKILL.md` (trigger overlaps, duplicate content, structure violations, files >50 lines) → show results → ask user to confirm fixes → apply if approved
3. Invoke `/handoff` via `Skill("handoff")` → write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub (no confirmation needed — handoff is always safe to write)
4. Run the continuity sync (no confirmation needed — always safe):
   - Windows: `cd "C:\Users\andre\repos\claude-continuity"; .\sync.ps1`
   - Mac/Linux: `cd ~/<path>/claude-continuity && bash sync.sh`
   - This copies `~/.claude/` memory + config into the `claude-continuity` repo and pushes to `origin master`. Report what it synced.
5. Memory + skill-kit audit check (no confirmation needed to run the check itself):
   - Count `.md` files in `C:\Users\andre\.claude\projects\<workspace>\memory\` (excluding `MEMORY.md`), and count `SKILL.md` files via `Glob "**/SKILL.md"` in `c:\Users\andre\.claude\skills`
   - Compare both against `lastAuditFileCount` / `lastSkillCount` in `memory/.audit-baseline.json`
   - If memory growth ≥15 OR the skill count differs from `lastSkillCount`: invoke `Skill("memory-audit")` directly — do not just print a suggestion, actually run it. It will show its own findings (memory AND skill-kit corruption) and ask for approval before applying anything.
   - Otherwise: report the current counts, no action needed

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.
