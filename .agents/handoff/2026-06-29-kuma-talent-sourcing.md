# Handoff: Kuma Talent sourcing benchmark + skill adoption + security fix
**Date:** 2026-06-29
**Status:** Complete — all active threads either finished or explicitly parked
---
## What We Accomplished This Session

**Global rules and process:**
- Added rules 14-17 ("Método de productividad en código") to global CLAUDE.md, reviewed via `/prompt-reviewer-en`, revised per findings.
- Ran `/retrospective`, persisted the learning that new/edited CLAUDE.md rules need a prompt-reviewer pass before finalizing.

**megamind repositioned as fallback-only:**
- `megamind/SKILL.md` description rewritten — fallback orchestrator for tasks with no dedicated skill, NOT a mandatory front door.
- `megamind/workflows/orchestrate.md` — added Step 0 (check for dedicated skill first) and a `Generated:` staleness check (>14 days → warn) on `project-map.md`.
- Refreshed `~/.claude/project-map.md` (29 repos) as a real end-to-end test of the fixed pipeline.
- Cleaned up duplicate repos found during that refresh (`kit-skill-creator`, `claude-skills` — deleted after verifying ancestor commits were safe).

**Security incident found and fixed:**
- hiresignal's `.git` was publicly exposed in production, leaking a (likely already-expired) DigitalOcean GitHub App token. Fixed at the build-context level (`.dockerignore`) and Apache level (`.htaccess` dotfile block). Verified fixed live (403 on `/.git/HEAD` before/after).
- Full credential audit across all repos came back clean.
- Found and removed a stray `.vercel/` directory (with a `.env.preview.local`) sitting in `~/.claude/skills/` itself — never committed to git, but didn't belong there per the "no production artifacts in ~/.claude/" rule.

**New skills adopted:**
- `deploy-to-vercel` (adapted from vercel-labs/agent-skills) — not yet wired into BTQ/MPD deploy workflows or `web-page-kit`; that integration was discussed but never executed (see Questions below).
- `apify-scraper` (adapted from apify/agent-skills) — built out with 5 playbooks, reviewed via `/prompt-reviewer-en`. Used extensively this session for a real Kuma Talent sourcing project (see below). Added `workflows/self-hosted-alternative.md` this session (the robots.txt → rendering → anti-bot checklist for deciding when to self-host instead of paying Apify) and a Windows/PowerShell-specific gotcha in `docs/gotchas.md` (use `-f <file>` not inline `-i '<json>'`; `-o`/`--json` are mutually exclusive).

**Kuma Talent / HireSignal:**
- Upgraded both the live interview chat AND the post-interview report to `claude-opus-4-8` in `hiresignal/config.php` (committed `651a75c`, pushed).
- New repo **`kuma-talent-sourcing`** (GitHub, Lucca-Tech org) — self-hosted (non-Apify) Argentina recruiting benchmark tooling:
  - `computrabajo_scraper.py` + `benchmark_report.py` + `executive_report.py` — working pipeline, $0 cost. Benchmarked 5 roles (Asistente Virtual is the only one where remote work is normal in the AR market — 59% vs 0-2% for the other four).
  - `jobbank_canada_scraper.py` / `canada_demand_benchmark.py` — parked (Job Bank Canada measures domestic Canadian hiring, not outsourcing intent — wrong signal).
  - Facebook Groups scraping via Apify — parked (works, but signal is mostly noise mixed with a few real candidate CV posts via OCR).
  - Checked and ruled out for self-hosting: Bumeran/Laborum/ZonaJobs (Cloudflare-blocked SPA, same platform family), elempleo.com (explicit scraping ban in robots.txt), Indeed (blocks AI crawlers specifically on job pages).

## Where We Paused
**Last action:** Ran `/session-close` — retrospective applied (5 skill/memory updates), skill-management audit clean (after removing the stray `.vercel/`), now writing this handoff.
**Next action:** Whatever Andrés picks up next — no single thread is mid-flight. See Questions below for things that were discussed but not actioned.
**Blockers:** None active.

## Files to Read First
- `apify-scraper/workflows/self-hosted-alternative.md` — the decision checklist built this session; read before evaluating any new scrape target.
- `kuma-talent-sourcing` repo (separate GitHub repo, Lucca-Tech org) — `computrabajo_scraper.py`, `benchmark_report.py`, `executive_report.py` are the active tools.
- Memory: `project_kuma_talent_sourcing.md`, `feedback_scraping_ethics_check_first.md`, `feedback_verify_background_tasks_promptly.md` — new this session.

## Notes / Gotchas
- `kuma-talent-sourcing` is a **separate git repo**, not part of this skills repo — its commits are already pushed independently, nothing pending there.
- fpdf2's `multi_cell(w=0, ...)` does not reset the cursor to the left margin afterward in the installed version (2.8.7) — every call after the first one fails with a confusing "not enough horizontal space" error unless `new_x="LMARGIN", new_y="NEXT"` is passed explicitly. Already fixed in `executive_report.py`'s code; worth knowing if fpdf2 is used elsewhere.
- A parallel session has uncommitted changes to `btq-production/pipeline-state-ep019.md` in this same repo — left untouched on purpose (not part of this session's work, per the parallel-sessions handling rule).

## Questions to Answer
- **Vercel deploy integration never executed.** A 3-part plan was discussed (mid-session, before this handoff) to: (1) add an `ignoreCommand` check to `deploy-to-vercel`'s Step 0, (2) fix a real bug in `episode-pipeline/workflows/05-deploy-verify.md` where MPD's deploy step uses plain `vercel --prod` despite MPD's `vercel.json` still needing the prebuilt-deploy flow, (3) update `web-page-kit/05-deployment.md`'s Vercel section. Never approved or executed — pick this up if/when an MPD or BTQ deploy is next, since the MPD bug is a real "will produce an empty/404 deployment" risk if run as currently written.
- **`podcast-creator-kit`'s hardcoded `KumaAdmin2026` default password** — explicitly deferred by Andrés (demo use, controlled access, low risk for now). Revisit if that repo's usage changes.
- **2FA org-wide + GitHub Advanced Security for Lucca-Tech** — flagged as optional/paid during the security audit, never actioned. Low priority unless Andrés wants to revisit.
