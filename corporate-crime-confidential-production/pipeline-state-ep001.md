# Pipeline State — CASE FILE No. 001 (Eight Is Great)

Mirrors the BTQ/MPD episode-pipeline structure, adapted: this show has no website yet, so
Stage C's grid-rotation and deploy steps don't apply until one exists. Engine for
generation is `podcast-creator` (same as MPD's routing), not `episode-launch` (BTQ-specific).

```
A — Pre-production:  roadmap ✓ → script ✓ → episode artwork ✓ → ⏸ go record
B — Post-recording:   intake → transcription → assets/metadata → ⏸ Spotify URL
C — Launch:           marketing/social plan + quote cards → (no site → no grid/deploy)
```

## Status

- `stage_a: complete`
  - Podcast profile: complete (`podcast-profile.json`)
  - Pilot case locked: Wells Fargo fake-accounts scandal, dual POV (composite banker + Carrie Tolstedt)
  - Script: complete (`episodio-001-eight-is-great.md`, ~6,700 words, styled artifact published)
  - Show-level identity: complete (`spotify-show-identity.md`, `artwork-general.md`)
  - Score requisition: complete (`score-requisition.md`) — briefs only, not rendered audio
  - Episode-specific artwork: complete (`artwork-ep001.md`, 3 formats — prompts only, not rendered images)
- `stage_b: pending` — **blocked on recording.** Nothing in Stage B can start until Andy
  has recorded the episode audio using `episodio-001-eight-is-great.md` and the cues in
  `score-requisition.md`.
- `spotify_url: pending`
- `stage_c: pending`

## Resume instructions

If picked up in a new session: **Stage A is closed.** The pause point is "go record" —
per the BTQ/MPD pipeline's own rules, this is a structural pause, not something to work
around. Do not generate Stage B content (transcription, show notes, YouTube metadata)
until real recorded audio exists. When it does, resume at `00-intake.md`-equivalent:
gather the audio + confirm nothing changed since this checkpoint, then move to
transcription (via the `transcriptor` skill) and assets/metadata.

**Transcription note (2026-07-04):** `transcriptor` now explicitly supports English
(`--language en`), confirmed in `transcriptor/SKILL.md` and `docs/environment.md` — pass
it as the language when invoked (standalone mode asks; pipeline mode takes it as an
optional second argument, e.g. `/transcriptor <path> en`). The still-open item is which
machine to run it on: the WhisperX venv/model cache/HF token live on the desktop's
`E:\Transcriptor\`, not this laptop.
