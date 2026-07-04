# Handoff: Corporate Crime Confidential — Pilot Setup
**Date:** 2026-07-04
**Status:** In progress — Stage A (pre-production) complete, blocked on recording

---

## What We Accomplished This Session

- Explored expanding BTQ to the English market; pulled real Spotify analytics and found
  the actual retention issue is the final-quarter drop-off, not the 60-min runtime
- Pivoted to a new, separate show idea: corporate true-crime podcast, villain
  first-person POV, real documented cases only (not fictionalized)
- Named and set up the new show: **Corporate Crime Confidential** — noir 1940s
  detective-comic identity
- Ran the full `podcast-creator` setup (`00-setup.md`): profile, tagline, intro/outro
  templates, tone rules, palette, episode numbering ("Case File No. NNN")
- Locked the pilot case: Wells Fargo fake-accounts scandal, dual POV (composite
  frontline banker + named executive Carrie Tolstedt)
- Researched and verified real facts/sources for the pilot (OCC/SEC filings, Stumpf's
  Senate testimony, documented whistleblower retaliation pattern)
- Wrote the full pilot script (~6,700 words) — `episodio-001-eight-is-great.md`
- Built and published a styled HTML artifact for the script (noir case-dossier design,
  reusable as the show's visual template)
- Created show-level Spotify identity doc + general show artwork prompts (3 formats)
- Created episode-specific artwork prompts for Case File No. 001 (3 formats)
- Wrote `score-requisition.md` — Suno/Udio prompts + stock-library search terms for
  intro/outro/stinger/tension beds (no audio-generation tool connected, so these are
  briefs, not rendered files)
- Caught and corrected a real location mistake: moved production files from
  `C:\Users\andre\repos\corporate-crime-confidential` into
  `c:\Users\andre\.claude\skills\corporate-crime-confidential-production` to match the
  established BTQ/MPD sibling-folder pattern
- Created `pipeline-state-ep001.md` mirroring BTQ/MPD's `episode-pipeline` structure,
  adapted (no website yet, so no grid-rotation/deploy stages)
- Ran retrospective + skill audit: encoded 5 fixes into the `podcast-creator` skill
  (production-folder location convention, mandatory name-collision web search, MPD-only
  artwork boundary note, audio-fallback-prompt pattern, MPD/BTQ-specific-section
  boundary note in `01-episodio.md`)

## Where We Paused

**Last action:** Committed the skill-audit fix to `01-episodio.md`; now writing this handoff.

**Next action:** User records the pilot episode audio using
`episodio-001-eight-is-great.md`, then brings the audio file back to continue Stage B
(transcription → assets/metadata → Spotify).

**Blockers:**
- Structural pause by design: Stage B cannot start until real recorded audio exists —
  mirrors BTQ/MPD's own pipeline rule, do not generate transcription/show-notes/YouTube
  metadata ahead of real audio
- Transcription machine decision pending: WhisperX setup lives on the desktop
  (`E:\Transcriptor\`), not this laptop — needs either switching machines or a fresh
  laptop install (weaker GPU, RTX 3060 6GB vs. desktop's 3080 Ti)
- ~~Transcription language defaults to Spanish~~ — **resolved 2026-07-04**: a parallel
  session updated `transcriptor` to explicitly support English (`--language en`,
  confirmed in `transcriptor/SKILL.md` and `docs/environment.md`). Pass it explicitly
  when invoking (standalone asks; pipeline mode takes it as an optional second argument).
- No audio-generation tool connected — intro/outro/stinger/tension beds are still just
  written briefs; user needs to run them through Suno/Udio or pull stock tracks
- Three `[VERIFICAR]` fact-check flags remain in the script — must be resolved before
  recording (see Questions to Answer)

## Files to Read First

- `corporate-crime-confidential-production\pipeline-state-ep001.md` — current
  stage/status and resume instructions
- `corporate-crime-confidential-production\episodio-001-eight-is-great.md` — the pilot
  script; has 3 `[VERIFICAR]` tags needing a fact-check pass before recording
- `corporate-crime-confidential-production\podcast-profile.json` — full show
  identity/config
- `corporate-crime-confidential-production\score-requisition.md` — audio briefs, none
  rendered yet

## Notes / Gotchas

- This show's production folder lives as a sibling inside `~/.claude/skills` (like
  `btq-production`/`mrputridsden-production`), NOT under `C:\Users\andre\repos\` —
  contradicts the global CLAUDE.md rule but matches established practice. See memory
  `project_podcast_production_in_skills_repo`.
- The show's sourcing discipline is strict: named real individuals (Carrie Tolstedt)
  get dramatized narration grounded strictly in documented public record; unnamed/
  unconfirmed individuals (the frontline banker) must stay an anonymized composite —
  never a named real person with invented internal thoughts.
- `episode-pipeline` skill is hardcoded to BTQ/MPD specifically (website, deploy,
  grid-rotation) — doesn't cleanly generalize to a brand-new show without a website yet.
  Used `podcast-creator`'s own workflows directly instead, with a reduced structure
  tracked in `pipeline-state-ep001.md`.
- The podcast name went through two rounds of real collision-checking before landing:
  "Off the Books" and "Off the Record" both collided with existing real podcasts;
  "Corporate Crime Confidential" cleared.

## Questions to Answer

- Which machine will be used for WhisperX transcription (desktop vs. laptop setup)?
  (Language is no longer a question — English is confirmed supported.)
- Resolve the 3 `[VERIFICAR]` flags in the script before recording: exact "King of
  Cross-Sell" report coining, exact fake-email address format reported, current status
  of the $2.6B class action
- Should the show's public Spotify description also carry a short version of the
  "dramatized narration" disclaimer (currently only in the internal script)? This was
  raised but left open — user hadn't confirmed before we moved on to artwork/audio.
