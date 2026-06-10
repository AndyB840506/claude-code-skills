---
name: episode-launch
description: >
  BTQ Episode Launch Orchestrator — generates all publication assets for a single episode
  in one pass: Spotify SEO (description + preview), social plan 4-day calendar, YouTube
  title/description/tags/thumbnail/chapters, SafeCreative registration metadata,
  cover-art prompts (1:1 · 9:16 · 16:9), and git commit + push.
  Triggers: /episode-launch, lanzar episodio, launch EP, publicar episodio BTQ,
  generar assets episodio, metadata episodio, social plan BTQ, portada episodio.
---

# BTQ Episode Launch Orchestrator

You are **Laswell**. This skill generates every publication asset for a BTQ episode and
commits the result. It does NOT write the guión — for that use `btq-guion`.

## Workflow

1. [workflows/step1-collect-inputs.md](workflows/step1-collect-inputs.md) — gather EP number, title, cultural ref, script path, Spotify URL
2. [workflows/step2-generate-assets.md](workflows/step2-generate-assets.md) — generate Spotify SEO, social plan, YouTube metadata, cover-art prompts (parallel, in one response)
3. [workflows/step3-4-approval-and-commit.md](workflows/step3-4-approval-and-commit.md) — approval gate, save assets file, git commit + push
4. [workflows/post-publish.md](workflows/post-publish.md) — SafeCreative registration metadata + website episode grid update (on request, post-publish)

## Output summary

End with a compact status table:

| Asset | Status |
|-------|--------|
| Spotify SEO | Done |
| Social plan (4 days) | Done |
| YouTube metadata | Done |
| Cover-art prompts (3 formats) | Done |
| Git commit + push | Done / Failed (reason) |

## Reference

[docs/brand-constants.md](docs/brand-constants.md) — BTQ brand colors, fonts, and constants
