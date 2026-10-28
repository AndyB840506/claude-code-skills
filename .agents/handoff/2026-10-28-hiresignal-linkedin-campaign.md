# Handoff: HireSignal LinkedIn campaign — strategy + first 3 posts
**Date:** 2026-10-28 (Wednesday)
**Machine:** desktop (E:\)
**Status:** In progress — strategy written, 3 posts with images ready; NOTHING published (Andrés posts "in the upcoming days")
---
## What We Accomplished This Session
- Picked up the "Track paralelo — Campañas en redes sociales" (hiresignal checkpoint, never started since 2026-09-22).
- Decisions (Andrés): LinkedIn only · new HireSignal company page + Andrés and Hugo's personal profiles · success = demos (`/try` + Book a demo) · English only for the pilot · positioning: set HireSignal apart from tools that let the AI decide and that get set up badly.
- Strategy doc (EN, Claude Doc): https://claude.ai/artifact/V1GN8bSgAdgqFNXpNeMFPL — sourced cases (EEOC iTutorGroup, Amazon/Reuters, Mobley v. Workday, EU AI Act, NYC LL144, Ontario), comparison table checked against hiresignal `8773edb`, can/can't-claim table, pillars, who posts, measurement, 2-week calendar, open questions, sources.
- hiresignal checkpoint updated with the answers + doc link: commit `729b1c9` (pushed to master).
- 3 posts with ComfyUI images (Z-Image Turbo, Apache-2.0) + Geist typography composed with PIL, 1200x1200:
  - `E:\AI\outputs\HireSignal\linkedin-pilot\final\HireSignal-LI01-launch-1x1.png` — page, Mon 2026-11-02
  - `...\final\HireSignal-LI02-itutorgroup-1x1.png` — Hugo, Tue 2026-11-03
  - `...\final\HireSignal-LI03-try-1x1.png` — Andrés, Thu 2026-11-05
  - Copy: `...\final\HireSignal-LinkedIn-week1-posts.txt` (687 / 1,083 / 607 characters, ASCII)
  - Scripts + converted fonts: `E:\AI\outputs\HireSignal\linkedin-pilot\scripts\`
- Retrospective applied: `python -I` vs `-P` (kit CLAUDE.md), woff2 fonts + glyph check (`comfyui/docs/artwork-composition.md`), textures with density (`comfyui/docs/prompting.md`), new memory `project_hiresignal_linkedin_campaign`.

## Where We Paused
**Last action:** session-close; ComfyUI stopped (port 8188 closed).
**Next action:** ask Andrés which posts already went out before doing anything (the dates are planned, not confirmed).
**Blockers:** Hugo has to review post 2 (it's written in his voice) and approve the plan; the doc is private until Andrés shares it.

## Files to Read First
- The strategy doc (link above) — may now carry comments from Hugo.
- `E:\AI\outputs\HireSignal\linkedin-pilot\final\HireSignal-LinkedIn-week1-posts.txt` — **machine-bound (desktop E:\)**; on the laptop it doesn't exist unless it was copied.
- `hiresignal/.agents/build-state/integraciones-pool.md` — social media track (~line 411).

## Notes / Gotchas
- The doc has 2 outdated points that weren't changed (Andrés closed before answering): its visual rule says "real product output only, no AI imagery" (the posts use AI-generated images), and the calendar has the `/try` post on 11-10 while the .txt moves it to 11-05.
- Messaging: we sell transparency and control, NOT accuracy (the fit score swings up to 15 pts on identical input; thresholds not validated). Never name competitors or HGS.
- Nothing records where a demo came from: the site has no analytics, and `demo_requests` and the Book a demo Sheet store no source. UTM sprint proposed, not approved.
- The kuma-talent-web clone is on the `redesign-hiresignal` branch (production = master `70fa628`).

## Questions to Answer
- Does Hugo post from his personal profile, and does he approve post 2?
- Company page name: "HireSignal" or "HireSignal by Kuma Group"?
- Publish the "15-point" figure (Andrés's next post in the calendar)?
- Update the doc (visual rule + date of the `/try` post)?
- UTM sprint: before or after the pilot? When to add FR/ES/PT?
- Review of the pilot: Fri 2026-11-13.
