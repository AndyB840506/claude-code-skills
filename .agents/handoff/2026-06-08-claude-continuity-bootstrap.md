# Handoff: Claude Continuity System — Bootstrap + Handoff + Auto-Resume
**Date:** 2026-06-08
**Status:** Complete — all components built and pushed to GitHub

---

## What We Accomplished This Session

- Built **`claude-bootstrap`** (private repo): stores global `~/.claude/` config + memory, cross-platform install/sync scripts — survives OS reformats
- Built **`claude-continuity`** (public template repo): generic version for anyone — GitHub Template, "Use this template" button active
- Redesigned **`/handoff` skill**: replaced clipboard/WinForms flow with file-based `git commit + push` to `.agents/handoff/YYYY-MM-DD-<topic>.md`
- Fixed **session-close** contradictions: removed "Step 4 creates NO files" constraint, updated all 3 files (SKILL.md, INSTRUCTIONS.md, workflows/execute.md), added Step 6 (bootstrap sync)
- Added **auto-resume routine** to `CLAUDE.md`: on startup, `git pull` → check `.agents/handoff/` → summarize latest + ask to continue
- Integrated **`sync.ps1`** into session-close ritual as Step 6 — pushes config+memory to bootstrap repo automatically
- All changes committed and pushed to `claude-code-skills` (the canonical repo)

## Where We Paused
**Last action:** Successfully pushed all commits to `claude-code-skills`; running first live `/handoff` test to verify the full file+git flow works
**Next action:** Verify this handoff file was committed and pushed; then open a fresh session to confirm CLAUDE.md auto-resume picks it up and asks "¿continuamos?"
**Blockers:** None

## Files to Read First
- `CLAUDE.md` — has the new "Antes de responder nada" auto-resume block at the top of "Comportamiento al iniciar"
- `C:\Users\andre\.claude\skills\handoff\SKILL.md` — redesigned handoff skill (file+git instead of clipboard)
- `C:\Users\andre\.claude\skills\session-close\SKILL.md` — updated to 6 steps including bootstrap sync
- `E:\Claude Project\claude-bootstrap\install.ps1` — bootstrap installer for new/reformatted Windows machine
- `E:\Claude Project\claude-bootstrap\sync.ps1` — bootstrap sync (runs at session-close Step 6)

## Notes / Gotchas

- **Two repos, same remote**: `~/.claude/skills/` AND `kit-skill-creator/` both point to `claude-code-skills.git`. Push from either, pull before pushing to avoid rejection.
- **Memory slug**: `install.ps1` computes it from the base dir path. If memory doesn't load after restore, check `~/.claude/projects/` for actual slug and copy manually — one-time fix per machine.
- **Bootstrap sync path hardcoded in session-close SKILL.md**: `E:\Claude Project\claude-bootstrap`. If bootstrap moves, update that path.
- **`claude-bootstrap` is private** — contains personal config and project memory. `claude-continuity` is the public version (generic, no personal data).
- **Skills were deleted from remote in a prior commit** (`682bfe0`) — the rebase on push recreated them. Skills repo working tree was reset to HEAD after the messy stash pop.

## Questions to Answer
- Test the laptop: clone `claude-code-skills` (NOT `claude-projects`) as the kit-skill-creator workspace, then run `install.ps1` from `claude-bootstrap` — confirm skills load and memory is correct
- Should `install.ps1` also save `.config/local-settings.json` with the base dir for future `sync.ps1` runs? (It does — Step 2 already does this)
- The skills in `claude-bootstrap/install.ps1` are cloned from `claude-code-skills` to `~/.claude/skills/`. Do we also need a separate clone for the project workspace, or should both be the same folder? (Currently separate — this is intentional)
