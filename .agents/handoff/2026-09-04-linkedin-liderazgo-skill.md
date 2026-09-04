# Handoff: LinkedIn Liderazgo Skill
**Date:** 2026-09-04
**Machine:** laptop (D:\)
**Status:** Complete — skill built and tested end-to-end with one published article
---
## What We Accomplished This Session

- Built new global skill `linkedin-liderazgo` (`~/.claude/skills/linkedin-liderazgo/`) — generates LinkedIn leadership articles in the user's real voice, with a 10-point verifiable checklist against generic AI-writing patterns (`docs/anti-patrones-ia.md`). Explicit documented boundary: never attempts to detect/strip Claude's real text watermark (confirmed real via support.claude.com/articles/16266773) — that's a transparency feature, not a style problem.
- Calibrated `perfil-voz.md` from real sources: user's BPO/CX job-interview prep doc (Google Drive, file id `1Ptu45m1WadwfFPeiMoRWQopAbhrPwT9R`) + BTQ podcast context. Captured tone, leadership philosophy, 7 real anecdotes. **Flagged as sensitive** (active job interview — Talent Harbor, CEO Elena) and got explicit confirmation: anecdotes usable but anonymized (no client/employer names, no mention of the interview process).
- Cross-referenced BTQ's production roadmap (`kit-skill-creator/btq-production/roadmap-btq.md`) into `docs/temas-btq.md` as an optional topic bank for when the user has no article idea.
- Generated and published one full test article ("La Proyección Sin Dueño") as a self-designed Artifact (copy-to-clipboard button, checklist evidence table shown, not hidden) — https://claude.ai/code/artifact/f8eb1cdb-ce2a-42d5-8ea3-04205c423d96 — approved after one angle revision (client-blame-shifting framing) and one checklist fix (patrón #10).
- Added ComfyUI cover-image generation to the workflow: abstract/conceptual style only (explicitly avoids the "AI corporate stock photo" cliché of photorealistic local models), Z-Image Turbo, 1200×630, embedded into the artifact as base64 spliced entirely inside a shell command (never through the tool-call context — `docs/estilo-visual.md` has the exact method and why).
- Found and fixed a real infrastructure gap in `session-close`: it never committed/pushed `~/.claude/skills` (a separate git repo, `claude-code-skills`, from both the project repo and the `claude-continuity` memory backup) — added Step 4 "Skills Repo Sync" to `SKILL.md` and `INSTRUCTIONS.md`.
- Retrospective: 3 learnings applied — the session-close gap fix above, tightened `anti-patrones-ia.md` patrón #10 (quoted-dialogue question stacking no longer gets a free pass), and a new feedback memory (`feedback_flag_sensitive_sources_before_publishing.md`).

## Where We Paused

**Last action:** Finished the skill-management audit (Step 2 of `/session-close`) and the handoff (this file, Step 3). About to run Step 4 (skills repo sync — will commit today's `linkedin-liderazgo` + `session-close` changes to `~/.claude/skills`), then Step 5 (continuity sync), then Step 6 (memory/skill-kit audit check).

**Next action:** If resuming mid-close, continue with Steps 4-6 of `/session-close`. If starting a new session, the skill is ready to use as-is — just invoke `/linkedin-liderazgo` (voice profile already calibrated, no re-asking needed).

**Blockers:** None active.

## Files to Read First

- `C:\Users\andre\.claude\skills\linkedin-liderazgo\SKILL.md` — entry point
- `C:\Users\andre\.claude\skills\linkedin-liderazgo\perfil-voz.md` — calibrated voice + anecdote reuse policy (anonymize, no interview mentions)
- `C:\Users\andre\.claude\skills\linkedin-liderazgo\docs\estilo-visual.md` — cover-image procedure (server check/launch, model, embedding method)

## Notes / Gotchas

- ComfyUI's `assets` capability is **NOT available** to this user (verified via the `artifact-capabilities` skill, 2026-09-04 — full available list: artifact, db, downloads, mcp, room, sample, self). Cover images must be embedded as base64 spliced via shell (`head`+`base64 -w0`+`tail`), never passed through a tool-call parameter — a 600 KB PNG is ~800K base64 characters.
- ComfyUI ran on the **laptop** this session (`D:\AI`, RTX 3060 Laptop, 6 GB VRAM) — no `E:` drive present, so it wasn't the desktop. The server does not persist between sessions; it was launched fresh and **stopped again at session close** to free VRAM. Any future session needing a cover image must repeat the check/launch sequence in `docs/estilo-visual.md`.
- `C:\Users\andre\repos\linkedin-articulos\` (where article `.md` + cover `.png` files get saved) is **not yet a git repo** — it's a plain folder, local-disk only, not backed up to GitHub.

## Questions to Answer

- Should `linkedin-articulos` become a tracked git repo (so articles + covers are backed up), or is local-only fine since the real destination is LinkedIn itself?
- No `USER-COMMENT`/`NEEDS USER INPUT`/`[TODO]`/`FIXME` markers found in project files this session (skill files excluded per rule).
