# Handoff: apify-scraper — free-alternative tiers (compliant vs. ToS-risk)

**Date:** 2026-08-09
**Machine:** desktop (E:\)
**Status:** Complete
---
## What We Accomplished This Session

- Evaluated the external repo `Panniantong/agent-reach` (GitHub) at the user's request —
  verified it's real and active via the GitHub API directly (69,406 stars, MIT, Python,
  pushed 2026-08-06), not just from its README claims.
- Flagged real risks before recommending anything: unpinned `main`-branch install (no
  version tag/hash), cookie/session-based scraping of ToS-restricted platforms
  (Twitter/Reddit/FB/IG/XHS), and unusually fast star growth worth independent sanity-check.
- User wanted to use it to cut Apify costs on `apify-scraper`. Read the existing skill
  first (`SKILL.md`, `workflows/self-hosted-alternative.md`, `docs/actor-index.md`,
  `docs/gotchas.md`) — confirmed the skill already has a hard ethics gate ("don't route
  around robots.txt/ToS regardless of feasibility") that agent-reach's core method
  conflicts with for the ToS-restricted platforms.
- Presented the real tradeoff instead of quietly complying: for Instagram/LinkedIn/
  Facebook/X/Twitter/XiaoHongShu there is no free option that's both full-reach AND
  ToS-compliant — free-and-compliant only exists for YouTube/RSS/Reddit(official
  API)/generic pages. Asked the user via `AskUserQuestion` how to resolve this; user
  chose to add an explicit **opt-in ToS-risk tier** rather than keep the hard gate as-is.
- Implemented a two-tier model in `apify-scraper`:
  - **Compliant-free** (`workflows/self-hosted-alternative.md`): added Jina Reader,
    `yt-dlp`, `feedparser`, official Reddit API as free options before reaching for a
    paid Actor.
  - **ToS-risk opt-in** (new `workflows/tos-risk-alternatives.md`): documents using
    agent-reach as the mechanism, **pinned to commit `1221ecd0c3e0502ee37406f03543bedf7503f2c7`**
    (verified against `main` via two independent GitHub API calls, not installed as a
    live dependency), gated on explicit per-platform user confirmation + dedicated/burner
    account, never a default.
  - Cross-referenced both tiers from `SKILL.md` and `docs/actor-index.md` (per-platform
    headers for Instagram/Facebook/X-Twitter/LinkedIn). Confirmed via the repo's actual
    `agent_reach/channels/` file listing (19 files) that **TikTok has no coverage** —
    explicitly noted as Apify-only, no free path.
- Session-close ran: retrospective found one learning (see below, applied), skill audit
  found `apify-scraper/SKILL.md` had grown to 67 lines from these edits (over the skill
  kit's own 50-line router cap) — condensed to 49 lines, no content lost.

## Where We Paused

**Last action:** Skill audit fix applied (SKILL.md trimmed to 49 lines), trigger-overlap
audit re-run clean (0 real collisions).
**Next action:** Continue session-close — Step 4 (continuity sync) and Step 5
(memory/skill-count audit check) still to run.
**Blockers:** None.

## Files to Read First

- `apify-scraper/SKILL.md` — ethics gate now has the two-tier pointer
- `apify-scraper/workflows/tos-risk-alternatives.md` — new file, the opt-in mechanism
- `apify-scraper/workflows/self-hosted-alternative.md` — compliant-free additions
- `apify-scraper/docs/actor-index.md` — per-platform cross-references

## Notes / Gotchas

- The agent-reach commit pin (`1221ecd0...`) is a point-in-time snapshot, not a
  maintained release — re-verify via the GitHub API before reusing it if much time has
  passed.
- `CLAUDE.md` got a new bullet under "Instrumentos que mienten en silencio": WebFetch
  summarizes with a small model and can silently omit list items — don't write a
  NEGATIVE claim about a third-party tool ("X doesn't support Y") into a durable file
  based on one WebFetch summary; verify against the primary structured source (this
  session initially almost shipped "TikTok not covered" on that basis alone, caught and
  fixed before declaring done by checking the actual file listing).
- The `mrputridsden` generic-trigger warning from the trigger audit (`D` category) is
  pre-existing, unrelated to this session — not touched.

## Questions to Answer

None open.
