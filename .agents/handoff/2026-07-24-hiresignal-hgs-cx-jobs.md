# Handoff: HireSignal — HGS Customer Service Rep jobs (EN + FR) added live

**Date:** 2026-07-24
**Machine:** desktop (E:\)
**Status:** Complete

---

## What We Accomplished This Session

- Recovered the prior CX JD (HireSignal `KT-004 "Customer Service Representative — CX (EN/FR)"`) from git history — it had been removed when the catalog restarted at KT-001 (commit `e263e4a`).
- User changed plans: built two new jobs from the real HGS posting instead — https://careers.joinhgs.com/Canada/job/Alberta-Work%40Home-Customer-Service-Representative/3724-en_US/ (Req 3724).
- **Added both live to the HireSignal production Jobs catalog:**
  - `KT-004` — Work@Home Customer Service Representative — HGS (Alberta), **English** (assess_french OFF)
  - `KT-005` — Représentant du service à la clientèle en télétravail — HGS (Alberta), **French FR-CA** (assess_french ON)
  - Both `active`, level `agent`, interview_mode `text`, requires_english ON, 3 custom questions each.
- **Key discovery:** HireSignal serves jobs from **Postgres** (`kv_store`), NOT `data/jobs.json`, since the 2026-06-11 persistence migration (commit `0369cfe`). The repo file is only a first-boot seed + ephemeral fallback. Editing/pushing it does NOT change the live list. Confirmed via `docs/operating-model.md` §Persistence and the live/file `active`-flag mismatch.
- Added the jobs by **curl-driving the admin endpoint** (login → session cookie → POST to `/admin/edit.php`; no CSRF). Verified via public `api/jobs.php` (5 jobs) and the authed `edit.php?code=` pages (description length, flags, question counts all correct).
- Committed + pushed `hiresignal/docs/jd-hgs-csr.md` (copy-paste JD reference, EN+FR) — commit `d776902` on `Lucca-Tech/hiresignal@master`.
- Saved 2 memory files: `reference_hiresignal_jobs_db_backed.md` and `feedback_check_http_layer_before_impossible.md`.

## Where We Paused
**Last action:** Session-close ritual (retrospective applied, this handoff).
**Next action:** Nothing pending — jobs are live and verified.
**Blockers:** None.

## Files to Read First
- `~/.claude/.../memory/reference_hiresignal_jobs_db_backed.md` — how to add HireSignal jobs (DB, not the file)
- `hiresignal/docs/jd-hgs-csr.md` — the two JDs, ready to re-paste if needed
- `hiresignal/docs/operating-model.md` — why prod is DB-backed

## Notes / Gotchas
- `data/jobs.json` in the repo is stale/inert (KT-001/002/003 show `active:false` there but are live/active in the DB). Do NOT "fix" it by pushing to make jobs live — that door is closed since the DB migration.
- The `d776902` push triggers a DO redeploy (`deploy_on_push`), which is safe: live jobs are in Postgres and survive redeploys.
- Admin password is a DO `ADMIN_PASSWORD` secret (not stored in repo or memory) — ask the user if a future session needs to script the admin endpoint again.

## Questions to Answer
- None open. (Optional future: give KT-005 its own non-KT code if HGS jobs should be namespaced separately from the Kuma catalog — not requested.)
