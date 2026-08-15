# Handoff: C2PA/AI-Watermark Audit of Repo + Production Images
**Date:** 2026-08-15
**Machine:** desktop (E:\)
**Status:** Complete
---
## What We Accomplished This Session

- User asked about a support.claude.com article claiming Claude marks AI-generated
  content with watermarks/C2PA metadata. Fetched and confirmed the article's actual
  claims: Claude text gets an imperceptible embedded watermark (no opt-out, no
  detection tool yet); supported files (.svg/.png/.jpg) get C2PA-standard signed
  provenance metadata. Scope: API, Claude.ai, Claude Code, Cowork, Claude Tag.
- Scanned 780 image files (20 in this skills repo + 760 on E:\) for C2PA-style byte
  signatures. 66 files showed a correlated signature cluster (real manifests); 3
  showed only a single isolated signature (false positives — confirmed via
  attribution-field extraction, no real manifest present).
- Extracted the actual `claim_generator`/`softwareAgent` field from the 66 real hits.
  **Zero were attributed to Anthropic/Claude.** All were either Google (Flow/Imagen +
  SynthID watermark) or Canva AI.
- 3 of those files are checked into this skills repo (not just E:\ production output):
  `btq-production\website\btq-episodio-social.png`, `Podcast_cover_art_logo...jpeg`,
  `mrputridsden-production\website\bar-bg.png` — see
  `memory/project_repo_assets_carry_ai_disclosure_metadata.md`. Andrés chose to leave
  them as-is for now.
- Ran `/retrospective`: added a new dated instance to `CLAUDE.md` §"Instrumentos que
  mienten en silencio" (short byte-signature searches over binary data give false
  positives — corroborate with a full signature cluster + attribution field before
  reporting).
- Ran skill-kit audit (`skill-management`): 28 skills, 0 real trigger collisions, no
  oversized `SKILL.md`, no stray loose `.md` files. Clean, no fixes applied.

## Where We Paused

**Last action:** Skill-kit audit completed clean; writing this handoff.
**Next action:** Continuity sync (Step 4 of `/session-close`), then memory/skill-count
check (Step 5).
**Blockers:** None.

## Files to Read First

- `memory/project_repo_assets_carry_ai_disclosure_metadata.md` — the 3 flagged files,
  not yet acted on
- `CLAUDE.md` §"Instrumentos que mienten en silencio" — new 2026-08-15 instance at the
  end of the bulleted list, before "Y el reverso..."

## Notes / Gotchas

- Text watermarking (per the article) is statistical/imperceptible — there is no way
  to grep or verify its presence in `.md`/text files. This remains unverifiable with
  current tooling; don't claim a clean bill of health for text output.
- C2PA is an open standard used by many vendors — a manifest hit does NOT mean
  "Claude did this." Always extract `claim_generator`/`softwareAgent` before
  attributing.

## Questions to Answer

- If the BTQ/MPD website assets get touched again (redesign, episode-launch run,
  artwork regen), ask Andrés whether to strip C2PA/EXIF metadata from the 3 flagged
  files, regenerate them without Canva/Google AI tools, or continue leaving them as-is.
  Not yet decided as a standing pipeline rule.
