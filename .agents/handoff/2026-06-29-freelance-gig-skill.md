# Handoff: `freelance-gig` skill — JD/requirement in, pitch and/or deliverable out

**Date:** 2026-06-29
**Status:** Complete
---
## What We Accomplished This Session

- Planned and built a new global skill, `freelance-gig/` (repo root), for freelance
  jobs found outside andyfreelancer.com's own intake bot (Upwork, Fiverr, direct
  outreach). Paste in a JD/requirement → get a pitch and/or a finished deliverable,
  tailored to Andy's real practice rather than a generic template.
- Discovered and reused `C:\Users\andre\repos\the-freelancer` (Andy's live
  production system) instead of re-deriving generic service/pricing/voice rules:
  `services.config.js` (7 services + pricing), `freelancer/bot.js` `SYSTEM_PROMPT`
  (voice playbook), `freelancer/prompts/{service_id}.md` (deliverable methodology),
  `freelancer/deliverable.js` `BASE_RULES`/`resolveServiceId()` (output contract +
  fuzzy matcher pattern). All read live at runtime, never copied — see
  `freelance-gig/docs/reuse-map.md`.
- Built the skill: `SKILL.md` (27-line router) + `workflows/{intake,proposal,build}.md`
  + `templates/gig-brief.json` + `docs/reuse-map.md`.
- Added section **"8 · Propuestas y entregables freelance"** to
  `docs/estandar-de-entregables.md` with a verifiable checklist matching the
  existing 7 sections' style.
- Incorporated explicit user feedback (mid-session): outputs must carry no
  AI-generation giveaways, in visual work (web pages, logos, graphics) AND
  written work (copy, audits, proposals) — framed as a client-risk issue for
  freelance work, not just an aesthetic preference. Encoded into
  `freelance-gig/workflows/build.md` step 3 + the new standards section.
- Ran `/retrospective`: found `build.md`'s AI-tell rules duplicated a thinner
  version of `web-page-kit/docs/design-guide.md` Rule 0 — fixed by pointing
  `build.md` to Rule 0 live for any web/visual build instead of restating it.
  Saved two new memories: `feedback_ai_tells_beyond_web.md` (scope extends past
  web pages) and `reference_the_freelancer_reuse.md` (pointer to the reuse
  source, so future sessions don't have to rediscover it).
- Ran the skill-management audit against the new skill — passes all checklist
  items, no trigger-phrase overlap with existing skills.

## Where We Paused

**Last action:** Skill-management audit completed and reported clean.
**Next action:** This handoff — then continuity sync (Step 4 of `/session-close`).
**Blockers:** None.

## Files to Read First

- `freelance-gig/SKILL.md` — entry point/router
- `freelance-gig/docs/reuse-map.md` — exact pointers into `the-freelancer` repo
- `freelance-gig/workflows/build.md` — has the no-AI-tell self-check (step 3-4)
- `docs/estandar-de-entregables.md` section 8 — quality checklist for this skill's output

## Notes / Gotchas

- A **new Claude Code session is required** for `/freelance-gig` to register as a
  slash command (new skill folders need a fresh session to be detected).
- The skill was never run end-to-end with a real JD — the plan's verification
  section (run once with a matched-service sample JD, once with an unmatched
  custom JD) has NOT been executed yet. Treat the skill as built-but-unverified.
- `the-freelancer` repo paths are hardcoded as absolute Windows paths
  (`C:\Users\andre\repos\the-freelancer\...`) inside the skill's workflow files
  — if that repo ever moves or is renamed, `freelance-gig` breaks until those
  paths are updated.

## Questions to Answer

- None outstanding — plan was approved and fully executed as scoped.
