# Pipeline State — CASE FILE No. 001 (Eight Is Great)

**Episode closed for now (2026-07-04).** Everything below is in a stable paused state —
quote-card images and Stage C are the only open items, both waiting on Andy (image
generation, then social/RSS setup). Next session picks up **Case File No. 002**: Andy will
share the missing info (case selection, recording, etc.) to kick that off fresh — don't
assume EP001's open items need chasing unless he brings them back up.

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
  - Script: complete (`episodio-001-eight-is-great.md`, styled artifact published). **Word
    count correction (2026-07-04):** the script's own footer claimed ~6,700 words, but that
    was never actually verified — a direct recount of the spoken dialogue (excluding stage
    directions, headers, sources) gives only ~2,955-3,116 words. Don't trust a script's
    self-reported word count; verify programmatically before locking a "complete" script.
  - Show-level identity: complete (`spotify-show-identity.md`, `artwork-general.md`)
  - Score requisition: complete (`score-requisition.md`) — briefs only, not rendered audio
  - Episode-specific artwork: prompts complete (`artwork-ep001.md`, 3 formats). **Images
    generated (2026-07-04)** at `E:\Podcast\True Crime\Case File 1\Case 001 Artwork\` — 9:16
    (1536×2752), 1:1 (2048×2048), 16:9 (2752×1536). Reviewed against the brief: text exact
    on all three, case-file tab reads "No. 001", 16:9 correctly does the strict left/right
    split, real rendered shading (not flat silhouette). Two fixes still needed before
    upload: (1) the 1:1 is under Spotify's 3000×3000 minimum — regenerate at higher res or
    upscale; (2) the 1:1's "EIGHT IS GREAT" title renders filled crimson instead of the
    aged-parchment fill + crimson drop-shadow the brief specifies (9:16 and 16:9 got this
    right) — regenerate for brand consistency since it's the primary Spotify cover. All
    three are also still >500KB and need the squoosh.app compression pass already documented
    in `artwork-general.md` before upload.
- `stage_b: in_progress`
  - Recording: complete — audio delivered at `E:\Podcast\True Crime\Case File 1\Corporate File Confidential Case 001.mp3`
  - Transcription: complete — `E:\Transcriptor\transcripciones\Corporate File Confidential Case 001.srt`
    (WhisperX large-v2, `--language en`, diarized, run on desktop 2026-07-04; first English
    run, auto-downloaded the English wav2vec2 aligner into `TORCH_HOME`)
  - **Runtime finding (2026-07-04, corrected):** the actual recording is ~23 min (1362s via
    ffprobe), not the ~45 min the script targeted. Investigated: the audio file itself is
    clean (44.1kHz/128kbps CBR, no sped-up export) and the delivered pace, ~137 wpm, is
    completely natural (matches BTQ's own 143 wpm calibration). Initial theory was
    "condensed/paraphrased delivery" — **wrong, corrected by Andy**, who confirmed he read
    the script word-for-word. Recounting the script's actual spoken dialogue (excluding
    stage directions/headers/sources) gives only ~2,955-3,116 words — matching the ~3,104
    words the transcript captured almost exactly. **Root cause: the script itself was
    under-written relative to its stated ~6,700-word/45-min target**, not a delivery
    problem. Fix for future CCC/BTQ scripts: verify the real word count of a finished draft
    before calling it complete, and size scripts to ~140 wpm × target minutes of *actual
    spoken dialogue* (excluding cues) — for a 45-min target that's ~6,300 words of spoken
    content, roughly double what this script had.
  - Assets/metadata: complete — `shownotes-ep001.md` (Spotify/Apple descriptions, SEO tags,
    timestamps) and `youtube-ep001.md` (title, description, tags, thumbnail text, chapters),
    both built for the real ~23-min episode with timestamps extracted from the transcript.
    Quote cards: prompts ready — `quotecards-ep001.md`, 6 cards, all lines verified
    against the actual transcript (not just the unrecorded full script). Paused for
    image generation (no generation API) — same structural pause as cover art.
- `spotify_url: https://open.spotify.com/episode/3slIwuP6C38iuRCBuGThu4` — published 2026-07-04
- `stage_c: explicitly skipped (2026-07-04)` — **not an oversight.** Andy is setting up
  CCC's social media accounts and establishing RSS distribution with Spotify himself
  before the marketing/social plan makes sense to generate. Don't auto-resume this step —
  wait for Andy to say the accounts/RSS are in place.

## Resume instructions

If picked up in a new session: **Stage A and Stage B's recording/transcription/assets/
publish steps are closed.** `[spotify_link]` placeholders in `shownotes-ep001.md` and
`youtube-ep001.md` have been filled in with the real URL. Remaining before Stage B fully
closes: quote-card images (prompts are ready in `quotecards-ep001.md`, paused for
generation). **Stage C (marketing/social plan) is explicitly paused, not blocked on
anything technical** — Andy is handling social account setup + Spotify RSS distribution
manually first. Don't generate Stage C content until he confirms that's done.

**Transcription note (2026-07-04):** `transcriptor` explicitly supports English
(`--language en`), confirmed in `transcriptor/SKILL.md` and `docs/environment.md`. Confirmed
working end-to-end on the desktop (`E:\Transcriptor\` venv/model cache/HF token) for this
episode.
