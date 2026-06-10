# Handoff: Vercel deploy fixes (MPD, BTQ, Lucca) + deploy-preflight update

**Date:** 2026-06-10
**Status:** Complete
---

## What We Accomplished This Session

- Identified root cause of MPD build-failure emails and BTQ/Lucca 404s: all 3 Vercel projects (`v0-mr-putrids-den`/MPD, `website`/BTQ, `lucca-tech-web`) had `Root Directory: .` while their actual code lives in subdirectories — Git pushes to `claude-code-skills` triggered Next.js framework-detected builds from repo root that overwrote prebuilt deploys.
- **Root-level fix:** ran `vercel git disconnect --yes` for all 3 projects. Pushes to `claude-code-skills` no longer trigger any auto-deploy for these projects.
- **Lucca:** redeployed prebuilt via `vercel --prod --yes` from `repos/lucca-tech-web` → `www.luccatech.com` returns 200 OK.
- **BTQ:** found `vercel link --project website --yes` (run earlier from the subdirectory) had corrupted root `.vercel/repo.json` with a bogus `"directory": "."` entry for `website`, causing deploys to upload 182 files (whole repo) instead of 9. Fixed by creating `btq-production/website/.vercel/project.json` as a dedicated local link and removing the bad entry from root `repo.json`. Redeploy now correctly uploads 8 files; `behind-thequeue.com` and `www.behind-thequeue.com` both return 200 OK.
- **Kuma Talent:** verified untouched — separate GitHub repo (`AndyB840506/kuma-talent-web`), `Root Directory: .` is correct for it, latest deploy `Ready`/Production. No action needed.
- **MPD anomaly check:** confirmed `Root Directory: .` mismatch exists for MPD too (same pattern as BTQ), but is neutralized by `ignoreCommand: exit 0` in `mrputridsden-production/website/vercel.json` + the Git disconnect. `www.mrputridsden.com` returns 200 OK.
- Deleted a stray, inert root-level `.vercel/project.json` (settings-cache file, no `projectId`) for repo cleanliness.
- Decided and confirmed with user: all 3 projects stay Git-disconnected going forward. Future deploys are manual — Claude runs `vercel --prod --yes` from the project directory on request. User does no manual Vercel dashboard actions.
- Ran `/retrospective` and updated `.claude/skills/deploy-preflight/workflows/checks.md`:
  - Added a pitfall note (Paso 2): never run `vercel link --project X --yes` from a monorepo subdirectory — it can corrupt root `.vercel/repo.json` with a `"directory": "."` entry (this is exactly what happened to BTQ).
  - Reworded Paso 6 to document the Git-disconnect as the established current state for MPD/BTQ/Lucca (not just a recommendation), and to note the pattern any future prebuilt project should follow.
- Committed cleanup from earlier in session (deploy-preflight hook-unlock removal, orphaned `session-close/workflows/execute.md` deletion) — commit `ba844e3`.

## Where We Paused

**Last action:** Committed `ba844e3` (deploy-preflight checklist simplification + orphan removal). The `checks.md` edits made during this session's `/retrospective` are NOT yet committed.
**Next action:** Stage and commit the `checks.md` retrospective edits, then push this handoff.
**Blockers:** None.

## Files to Read First

- `.claude/skills/deploy-preflight/workflows/checks.md` — updated Paso 2 (vercel link pitfall) and Paso 6 (current Git-disconnect state for MPD/BTQ/Lucca). Read this before any future `vercel link` or deploy in this repo.
- `.vercel/repo.json` — should have exactly one entry (`v0-mr-putrids-den` → `mrputridsden-production/website`). If a `website` or other subdirectory-project entry with `directory: "."` reappears, that's the BTQ bug recurring.

## Notes / Gotchas

- `btq-production/website/.vercel/project.json` and `lucca-tech-web/.vercel/project.json` are the reference pattern for dedicated subdirectory project links — both gitignored, not committed.
- All 3 production sites verified 200 OK at end of session: `www.mrputridsden.com`, `behind-thequeue.com`/`www.behind-thequeue.com`, `www.luccatech.com`.
- Vercel dashboard shows a `!` icon on `v0-mr-putrids-den` (vs `✓` on others) — likely flags the disconnected Git or the Root Directory mismatch as an info warning. Not investigated further since the live site is confirmed healthy; CLI doesn't expose the tooltip text.

## Questions to Answer

- None outstanding.
