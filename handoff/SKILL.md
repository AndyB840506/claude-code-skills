---
name: handoff
description: >
  Transfer work context between agent sessions without losing progress.
  Use when switching to a new session mid-task, parking work to resume
  later, or creating a persistent handoff committed to GitHub. Triggers:
  transfer context, park session, guardar contexto, transferir sesión,
  next session, continue in new session, retomar sesión, pasar contexto,
  park work, resume later. NOT for end-of-session close — use session-close
  for that.
---

# Handoff Skill

Transfer work context between agent sessions without losing progress.
Handoff files are committed and pushed to GitHub so any machine where
the repo is cloned can resume from exactly this point.

## Workflow Routing

| Command | Mode | Workflow |
|---|---|---|
| `/handoff` | File: write handoff doc, commit, push to GitHub | `workflows/file-handoff.md` |
| `/handoff park` | Park: update session Progress only, no file, no push | `workflows/park.md` |

## Key Rules

Follow these steps in order:
1. **Update docs first** - the vault/project is the source of truth
2. **User's direction > agent's analysis** - if user said what to focus on next, that's the priority. Supplement with agent analysis only if user direction is incomplete
3. **Scan for pending markers before Next Steps** - grep for `USER-COMMENT`, `NEEDS USER INPUT`, `[TODO]`, `FIXME` in active session files. Every marker found must appear explicitly in Next Steps with where it lives, what's being asked, and who must act
4. **Verificar estado real al retomar** — Al iniciar sesión con handoff, preguntar explícitamente: "¿Alguno de los next steps del handoff ya fue completado?" El handoff captura el estado al momento de escribirse. No asumir que los Next Steps siguen pendientes.

## Reference

- `docs/sessionend-hook.md` — configure an automatic SessionEnd reminder
