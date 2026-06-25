# Handoff: Continuity backup fix + /insight skill

**Date:** 2026-06-25
**Status:** Complete — all changes committed & pushed; 75 memories now backed up to GitHub

---

## What We Accomplished This Session

(This was a meta/tooling session — second close of the day, after `kumatalent-warmden-cv-capture`.)

- **Built a new skill `/insight`** (global, repo root): a cross-session friction-finder that reads `MEMORY.md` + recent handoffs, clusters recurring friction (requires ≥2 occurrences per pattern), and proposes durable rules. Router `SKILL.md` (41 lines) + `workflows/surface-patterns.md`. Distinct from `/retrospective` (single session) and `/session-close` (ritual). Pushed to `claude-code-skills` (`a0327ba`).
- **Ran `/insight` live** — it surfaced one new actionable pattern: **destructive DNS/domain/cert actions on a live site**. Created memory `feedback_live_dns_danger.md` consolidating the 3 traps (Vercel domain churn resets cert · Porkbun "update nameservers" · moving NS orphans CNAME+MX), and tightened `feedback_validate_before_theorizing.md`.
- **Found & fixed a CRITICAL silent backup failure:** `claude-continuity` (the `~/.claude/` backup system) had been backing up **ZERO memory since 2026-06-09**. Root cause: `sync.ps1`/`sync.sh` recomputed Claude Code's project slug, but the derivation didn't match the real folder names (case + dash mismatch), so `Test-Path` failed silently. Also the active workspace `~/.claude/skills` wasn't even in `projects.json`.
  - **Fixed** `sync.ps1`, `sync.sh`, `install.ps1`, `install.sh`: stop guessing the slug — enumerate every `~/.claude/projects/*/memory` that has files and copy/restore verbatim by real folder name (symmetric sync↔restore).
  - **Fixed** `SKILLS_REPO_URL` placeholder → real repo `claude-code-skills` in both installers.
  - **Fixed** `sync.sh` pushing to `main` when the repo uses `master`.
  - **Ran the corrected sync:** backed up **75 memory files** (48 kit-skill-creator + 27 claude-skills) + `CLAUDE.md` + `settings.json`. Pushed to `claude-continuity` master (`9cad3b5`). Verified counts on disk + clean tree.
- **Automated the backup:** added **Step 4 (Continuity Sync)** to `/session-close` (SKILL.md + INSTRUCTIONS.md), so every close now runs `sync.ps1` and pushes `~/.claude/` memory to GitHub. SKILL.md trimmed to 45 lines. Pushed (`e1f9007`).
- **New memory** `feedback_always_backup_github.md` — always commit+push after work (two PCs); notes that memory is NOT in the skills repo (synced via claude-continuity).
- This session's own close: Step 1 retrospective extended `feedback_validate_before_theorizing.md` (the "verify the backup destination, don't assume" principle).

## Where We Paused

**Last action:** Step 1–2 of this `/session-close` done; writing this handoff (Step 3). Step 4 (continuity sync) runs next.
**Next action:** Finish Step 3 push, then run Step 4 `sync.ps1` to back up today's memory edits.
**Blockers:** None.

## Files to Read First

- `C:\Users\andre\repos\claude-continuity\sync.ps1` / `install.ps1` (+ `.sh`) — the fixed backup scripts (comments explain why slug-guessing was removed).
- `.claude/skills/session-close/SKILL.md` + `INSTRUCTIONS.md` — now a 4-step ritual.
- `.claude/skills/insight/SKILL.md` — the new friction-finder.

## Notes / Gotchas

- **Continuity sync is still MANUAL unless `/session-close` runs it.** Step 4 now does, but a bare `git push` of a project repo does NOT back up `~/.claude/` memory.
- The repo `claude-continuity` uses branch **`master`**; the skills repo `claude-code-skills` uses **`main`**. Don't cross them.
- Slug lesson: never recompute Claude Code's project slug — enumerate real folders instead.
- Verify backups by checking the destination (file counts / `git ls-files`), not by trusting the script ran.

## Questions to Answer

- None open. (If switching to Mac: `git clone claude-continuity && bash install.sh` restores skills + 75 memories + config.)
