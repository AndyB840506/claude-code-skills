# ToS-risk alternatives: free access where Apify's fee buys ToS-risk absorption

**When:** the target platform explicitly forbids scraping (Instagram,
LinkedIn, Facebook, X/Twitter, XiaoHongShu) and the user wants to avoid
Apify's per-result cost anyway, on that specific platform. TikTok isn't
covered here — no free mechanism exists for it, Apify remains the only
option.

This is not a compliant-free option — see
`workflows/self-hosted-alternative.md` first for platforms where a real
free-and-compliant path exists (YouTube, RSS, Reddit, generic pages). For
these platforms, Apify Actors cost money specifically because they've
absorbed the anti-bot/ToS enforcement risk into their fee. Going free here
means the user absorbs that risk personally instead — account suspension,
not just a failed request.

## Gate — required every time, not just once per project

1. **Never default to this tier.** Only use it when the user explicitly
   names the platform and says they accept the risk for it. A general
   "avoid Apify costs" request does NOT cover this tier — confirm per
   platform.
2. **Confirm a dedicated/burner account will be used**, not the user's
   primary account. State this explicitly before proceeding; don't assume.
3. **State the mechanism is cookie/session-based**, i.e. it acts as a
   logged-in user of that platform, not an anonymous request — that's what
   triggers ban risk on detection.

## Mechanism

The underlying technique across these platforms is the same: export a
logged-in session's cookies from a browser, then make requests carrying
those cookies (or drive a browser that already has the session, for
Facebook/Instagram). `agent-reach` (github.com/Panniantong/agent-reach) is
an open-source implementation of this pattern across all these platforms
plus a config/credential manager. Use it as the mechanism rather than
writing per-platform cookie-scraping code from scratch — but **pin to a
fixed commit, not `main`**, since the maintainers' own install docs pull the
live branch on every install with no version tag or hash check:

```bash
pipx install "https://github.com/Panniantong/agent-reach/archive/1221ecd0c3e0502ee37406f03543bedf7503f2c7.zip"
agent-reach install --env=auto
```

(SHA verified against `main` via the GitHub API on 2026-08-09 — re-verify
before reusing this pin after significant time has passed, since it's a
point-in-time snapshot, not a maintained release.)

Per-platform setup (all cookie-export based unless noted):

| Platform | Command | Notes |
|---|---|---|
| X/Twitter | `agent-reach configure twitter-cookies` | Export via browser or Cookie-Editor |
| XiaoHongShu | `agent-reach configure xhs-cookies` | Same pattern |
| Facebook/Instagram | handled via existing Chrome session (OpenCLI) | Uses the browser's live login, not an exported cookie file — higher blast radius since it's the real logged-in browser |
| LinkedIn | `mcporter config add linkedin --command uvx --arg mcp-server-linkedin@latest` then `uvx mcp-server-linkedin@latest --login` | MCP-based, separate login flow |

Credentials land in `~/.agent-reach/config.yaml` (600 permissions, local
only per the project's own docs — not independently verified by us).

## After running

Report results the same way as an Apify run (count, format, file location).
Additionally flag to the user: this run used the platform's ToS-risk tier on
[account] — if results look throttled or empty, that's more likely an
account-level soft-block than a bug.
