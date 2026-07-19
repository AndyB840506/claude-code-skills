# Handoff: MPD — EP.005 live on Spotify, full website overhaul deployed to mrputridsden.com
**Date:** 2026-07-19 (domingo)
**Status:** Complete — site is live on the real domain, all planned fixes shipped
---

## What We Accomplished This Session

**EP.005 published — metadata/roadmap closed out:**
- Real Spotify URL added to `episodios/ep005-metadata.md` (plain + HTML descriptions) and
  `roadmap-mpd.md` (status → "en Spotify", title aligned to the aired title).
- Resolved the two open questions from the 2026-07-17 handoff: roadmap title now matches
  the aired title, and the Juan-departure-mention question is decided — **stays unmentioned**
  everywhere (episode, show notes, social). `ep005-metadata.md`'s stale "pendiente decisión"
  note updated to reflect this.
- Central Spotify link in `podcast-profile.json` (`links.spotify`) now points to the show page
  (`open.spotify.com/show/0M12ujB9eJqr0dWZUwEf6B`) instead of standing in on EP.001's episode link.

**Website: full visual redesign ("Última Ronda") for the solo-host era:**
- `mrputridsden-production/website/index.html` — concert-ticket episode cards rebuilt as vinyl
  sleeve/crate-digging cards ("Lado A" + mini disc icon); "El Residente" rebuilt from a
  two-host grid into a single editorial feature (bigger portrait, pull-quote from Andrés —
  **draft copy, his to personalize**); ambient neon flicker slowed/softened and the WebGL
  shader warmed (ember over red) for a calmer "last call" mood instead of "loud club."
- Two follow-up polish passes, both requested after visual review: **La Carta de la Casa**
  redesigned as an actual paper menu card (was floating transparent text, didn't read as a
  menu); **"Disponible en" platform links** given a solid dark panel background + brighter tag
  color (text was losing contrast against the shader background).
- Stale links fixed: nav/hero CTA + Sintoniza embed now point to EP.005 (was EP.001 and an old
  unrelated episode); Sintoniza's Spotify platform link now points to the show page.

**Production incident, caught and fixed same session:**
- `mrputridsden-production/website/.vercel/project.json` was linked to the WRONG Vercel
  project — a folder-name collision (`website`) meant it was actually BTQ's live project.
  Running `vercel --prod` auto-aliased `behind-thequeue.com` to the MPD build, overwriting
  BTQ's production site. Caught via WebFetch (had to cache-bust with `?cb=`, since the tool's
  own 15-min cache returned stale content and initially masked the fix), restored BTQ's alias
  to its last-good deployment, verified.
- Root-caused and fixed properly: created a new dedicated project `mr-putrids-den-web`,
  relinked this folder to it, removed the orphaned MPD deployment/aliases that had landed on
  BTQ's project. **`mrputridsden.com` and `www.mrputridsden.com` are now aliased to
  `mr-putrids-den-web`** — the old `v0-mr-putrids-den` project is orphaned/stale, do not use it.
- `deploy-preflight/workflows/checks.md` updated with the corrected project mapping, a new
  Paso 1b (verify `.vercel/project.json`'s actual `projectName` against the expected mapping
  before deploying — the check that would have caught this), and a WebFetch cache-busting note.

## Where We Paused

**Last action:** `/session-close` ritual — retrospective applied, skill kit audit found no
issues, this handoff.
**Next action:** Nothing blocking. If a future session touches the MPD website again, verify
`.vercel/project.json`'s `projectName` is still `mr-putrids-den-web` before any `vercel --prod`
(see Paso 1b in deploy-preflight).
**Blockers:** None.

## Files to Read First

- `reference_mpd_vercel_projects.md` (memory) — the Vercel project map/incident, so the mixup
  isn't repeated.
- `project_mpd_juan_departure.md` (memory, newly created this session — the prior handoff
  referenced it by name but it never actually existed) — full state of the solo-format change.
- `mrputridsden-production/website/index.html` — the redesigned site, now live.
- `mrputridsden-production/roadmap-mpd.md` — EP.005 status, open items for EP.008/EP.009.

## Notes / Gotchas

- The "El Residente" pull-quote ("La barra sigue abierta...") is copy I drafted in Andrés'
  voice — flagged to him as a draft, not yet explicitly confirmed word-for-word. Fine to leave
  live, but worth a look next time he's on the site.
- `v0-mr-putrids-den` (the old Vercel project) still exists under the team but is disconnected
  from the domain — harmless to ignore, not scheduled for deletion.
- EP.002's own metadata still has a leftover `[show-url-EP002]` placeholder (predates this
  session) — Andrés explicitly chose not to fix it with the show-level URL, since it needs
  EP.002's own episode-specific link, not the general show page. Still pending whenever that
  real link is available.

## Questions to Answer

None open from this session — both prior open questions (roadmap title, Juan-mention) were
resolved today. Still-open from earlier sessions (unchanged, see `project_mpd_juan_departure.md`):
- Replacement source for the retired Promoción segment / guest booking for EP.008.
- What topic EP.009 covers now that "Spotlight: eventos underground" was retired.
