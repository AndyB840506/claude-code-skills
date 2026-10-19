# Handoff: BF6 Meta Ops, Season 5 refresh (+ continuity start.ps1 fix)
**Date:** 2026-10-19 (Monday)
**Machine:** desktop (E:\)
**Status:** Complete. Refresh PUBLISHED to luccatech.com/bf6/ (lucca-tech-web `2764a24`, deploy `lucca-tech-n8hd2jdqd`, live == local).
---
## What We Accomplished This Session
- **claude-continuity `start.ps1` fixed (`7ed79a9`, pushed):** `Resolve-Path -Relative` resolved from
  the caller's cwd, git got `..\..\repos\...`, exited 128, commit date = MinValue, so the local
  memory always "won". On the desktop it kept 3 stale memories (`feedback_design_references`,
  `hub_freelance`, `project_d2_build_tool`); copied from the repo by hand, byte-identical.
  Tested: a staged stale copy gave `actualizados: 1`, exit 0 (before: conservados 3, exit 128).
- **BF6 data refresh** (`E:\Claude Output\bf6\data\weapons.json`, backup of the Oct 15 data in
  `weapons.json.2026-10-15.bak`). Patch still 2.1.1.0; the only patch since is the Oct 15 hotfix
  (audio only). Added: Mk 24 Underslung Mount disabled (our 6H64 Vertical build is unaffected),
  REDSEC Rapid Royale airstrikes disabled. Pick rates refreshed to Battlefinity Oct 16 and
  meta rankings to wzstats Oct 19.
- **Rank decisions by Andres:** Mk 24 #1 AR in both modes (usage); Z84M #1 MP LMG and RSPR #2 MP
  SMG (int.gg match performance + MP TTK). Also: MP M16A4 above KORD; REDSEC RSPR down to #4;
  REDSEC carbine #3 M4A1 replaced by QBZ-192 (MP builds reused, stated in its reason).
- **Season 5 builds:** Z84M moved from a pattern pick to 3 sourced builds (close / versatile /
  long); Mk 24 got a Versatile build; ELR-40 reasons carry the Single Shot vs standard sweet spot
  (one player's test, unconfirmed).
- App rebuilt to `E:\Claude Output\bf6\bf6-meta-app.html` and
  `C:\Users\andre\repos\lucca-tech-web\bf6\index.html` (identical). `verify-all.ps1`:
  PASS 9 of 9 (after fixing a 421 px overflow from a long TTK chip).
- Patch script used for every data change (re-runnable, starts from the .bak, aborts if any
  target is not found exactly once):
  `C:\Users\andre\AppData\Local\Temp\claude\c--Users-andre--claude-skills\10bc76c5-cc3e-4de8-8e5b-3262cf087f09\scratchpad\bf6_update.py`
  (scratchpad: may be gone in a new session).
- Skill updates: `bf6-meta-configurator/workflows/run-report.md` (3 source families + split
  menu rule, incremental refresh still needs Pass 2 for season weapons, REDSEC TTK trap),
  `html-spec.md` (short stat chips), kit `CLAUDE.md` (start.ps1 root cause).

## Where We Paused
**Last action:** published on Andres's OK: `node build.js` (sitemap lastmod), commit
`2764a24` pushed, deploy-preflight passed (domain served by `lucca-tech-web`, no secrets,
baseline 200), `vercel build --prod` output cmp'd against the repo, `deploy --prebuilt --prod`.
Live check: `vercel inspect` shows the new deploy (17:41), `/bf6/` 200 and identical to local,
sitemap lastmod 2026-10-19, home and `/es/` 200. Memory `project_bf6_meta_ops` updated.
**Next action:** nothing pending on BF6 unless Andres asks; next refresh should run the vehicle pass.
**Blockers:** none. The data still lives only on `E:\` (desktop).

## Files to Read First
- `E:\Claude Output\bf6\data\weapons.json` (desktop only): current data.
- `bf6-meta-configurator/workflows/run-report.md` Step 1-2: the new rules from today.

## Notes / Gotchas
- Battlefinity per-weapon TTK is REDSEC (armor): Z84M 417 ms there vs 167 ms MP (Timesaver).
- Timesaver's LMG ranking puts the DRS-IAR at C tier; wzstats #1 and Battlefinity S disagree.
  Kept DRS-IAR #2 MP LMG.
- `vehicles.json` was not touched and the vehicle pass was NOT run this session.
- Other open handoffs: `2026-10-18-black-armory-s8-ui.md` (desktop black-armory still 1
  commit behind, not pulled) and `2026-10-18-lucca-tune-tdr-cputemp.md`.

## Questions to Answer
- Mk 24 Versatile / Z84M per-playstyle builds: never seen on screen (the verify suite does not
  switch playstyle). Set the app to Aggressive: the Z84M should show Iron Sights.
- Has EA re-enabled the Mk 24 Underslung Mount? (newest source: Oct 16)
- Vehicle pass: run it on the next refresh.
