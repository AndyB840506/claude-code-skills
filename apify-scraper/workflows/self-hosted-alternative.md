# Self-hosted alternative: when NOT to use Apify

**When:** User wants to avoid Apify's per-result cost for a specific target site
and asks whether scraping it themselves (free, local) is viable.

Apify Actors are worth paying for specifically because they've already solved
anti-bot detection and JS rendering. Before defaulting to Apify, check whether
the target site actually needs that — many don't.

## Checklist (run in this order, stop at the first blocker)

1. **Fetch `robots.txt` first.** Look for:
   - A blanket prohibition on scraping for commercial/AI use (some sites state
     this explicitly in a comment, not just `Disallow` rules — e.g. elempleo.com).
     If present, stop. This is a policy decision, not a technical one — don't
     route around it regardless of feasibility.
   - AI-crawler-specific exclusions (`GPTBot`, `ClaudeBot`, `anthropic-ai`,
     `DeepSeekBot`, etc.) that block paths general browsers/Googlebot can still
     access (seen on Indeed). Don't spoof a generic browser User-Agent to get
     around a distinction the site owner made on purpose — treat this the same
     as an explicit prohibition and stop.
2. **Fetch one sample page with a plain HTTP request** (real browser User-Agent,
   no JS execution). Check if the data you need is in the raw HTML.
   - Present → server-rendered, self-hosted scraping with `requests`+`BeautifulSoup`
     works and is free.
   - Absent / tiny HTML shell → likely a JS-rendered SPA, go to step 3.
3. **If it's an SPA, check for anti-bot protection before reaching for Playwright.**
   A headless browser only helps if the site isn't actively blocking automation.
   Quick probe: load the page with Playwright and check the response status —
   a 403 with a Cloudflare/WAF error page means stealth techniques would be
   needed to get further, which isn't worth building (same risk/cost tradeoff
   as paying for the Apify Actor that already handles this).
4. **Decision:** server-rendered + permissive robots.txt → self-host for free.
   SPA blocked by anti-bot → pay for the Apify Actor instead (it's already
   solved the problem you'd otherwise be building from scratch). SPA with no
   anti-bot wall → Playwright self-hosted still works, just slower than HTTP.

## Worked example (Argentina job boards, 2026-06)

Checked 7 sites for a recruiting benchmark: Computrabajo (server-rendered,
open robots.txt → self-hosted, free), Bumeran/Laborum/ZonaJobs (same platform
family, SPA + Cloudflare 403 on headless → not worth self-hosting), elempleo.com
(explicit commercial/AI scraping ban in robots.txt → excluded on policy, not
difficulty), Indeed (AI-crawler-specific block on `/jobs` while Googlebot is
allowed → excluded, didn't spoof UA to bypass), Job Bank Canada (fully open,
server-rendered → self-hosted, but turned out to measure the wrong thing —
domestic hiring, not outsourcing intent, so an open site doesn't guarantee
useful data).
