# Handoff — the-freelancer samples + language-neutral prompts

**Date:** 2026-07-03
**Repos touched:** `C:\Users\andre\repos\the-freelancer` (master), `C:\Users\andre\.claude\skills` (main), `~/.claude/` memory

---

## What was done (all committed/pushed/live)

### 1. Fixed the mixed-language deliverable bug — "recipe vs render"
`the-freelancer` deliverable engine was emitting Frankenstein output (e.g. English body under Spanish headers) because the prompt files hardcoded output-facing Spanish labels. Fixed centrally:
- `freelancer/deliverable.js` `BASE_RULES` — added **Output-language** rule (render 100% in order language; content native, not translated), **unified markers** `[TODO]`/`[IMAGE]` (was 6 different vocabularies), **shared score bands + gauge** for audits, and fixed the **brand color** teal `#0d9488` → `#0e1113` + `#ff3d00` (the real live-site palette). Removed the bilingual `"Preguntas pendientes / Pending questions"` example.
- All 7 `freelancer/prompts/*.md` — Spanish output labels → English canonical reference labels; markers migrated to the unified convention; business_audit got a non-SMB note.
- Commit `2cf5a97` on `master`, pushed, **DO deploy confirmed green** by user.
- Principle captured in memory: [[feedback_recipe_vs_render]].

### 2. Skill kit audit (language)
- `smart-recruiter/templates/report-template.md` — added directive to render headings in the report's language (was hardcoded English while interviews can run Spanish).
- `web-page-kit` — normalized recipe-facing `Paso N` → `Step N` (cosmetic; 9 files).
- **Left intentionally untouched:** `mrputridsden`, `crear-skill`, `deploy-preflight` (Spanish is the product/workspace voice), `podcast-creator`, `episode-launch` (Spanish-first products, pending product-intent decision).
- Commit `330aeb5` on skills repo `main`, pushed.

### 3. 7 real sample deliverables — LIVE at andyfreelancer.com/samples
Replaced screenshot mockups with clickable, complete, watermarked samples covering all 7 services (`one-pager/samples/*.html`):
- `business-audit-nvidia`, `seo-audit-tesla` (public data; Tesla flags fetch-block limitations)
- `social-to-web-btq` — **built from the REAL Instagram feed** of @behindthequeue84 via Apify (12 posts scraped, images downloaded to `one-pager/samples/assets/btq-ig/`, hosted locally)
- `web-page-bakery` (concept brand), `lead-generation-austin-roasters` (real public businesses, public channels only, decision-makers `[TODO: verify]`), `meta-ads-audit-btq` (honest pre-launch — Ad Library not queryable), `copywriting-kit-ledgerly` (concept brand, `[TODO: confirm]` on claims)
- `samples.html`: "Read a complete report" section links all 7 (trilingual EN/ES/PT) + restyled to homepage typography (Cabinet Grotesk / Supreme / Martian Mono, Fontshare).
- Commit `edb2f67` on `master`, pushed, **verified 200 live** (page + 7 reports + 12 images).
- Method captured in memory: [[reference_instagram_apify_scraping]].

### 4. LinkedIn campaign (drafted in chat, NOT saved)
Anchor post + 3 highlights (Social→Web, audits, honesty/lead-gen), EN + ES as separate posts, Andy's voice, link-in-first-comment mechanic. Delivered in chat only.

---

## Next Steps (pending markers + open items)

- **[NEEDS USER INPUT] BTQ Spotify/Apple links** — `social-to-web-btq.html` uses `#` placeholders for Spotify/Apple Podcasts; the profile pic is a "BTQ" monogram, not the real IG avatar. **Andy must provide the real streaming URLs** (and confirm if he wants the real avatar downloaded) → then update.
- **[USER ACTION] Rotate `APIFY_TOKEN`** — Andy pasted it in chat. It was used inline only, never written to disk or repo (verified: `grep apify_api_` in repo = clean). Rotate in Apify for safety.
- **[OPTIONAL] Save LinkedIn posts** — the campaign is only in chat. Offer to save as `.md` in the repo if Andy wants it retained.
- **[OPTIONAL] 4th LinkedIn highlight** — Copywriting or Meta Ads angle, if extending the series.
- **[INFO, no action] `/samples` 301-redirects to `/samples/`** — benign side effect of adding the real `samples/` directory; report files serve fine. Only revisit if Andy wants the redirect gone (reorder middleware in `server.js`).
- **[DECISION PENDING] podcast-creator / episode-launch language** — deferred: are these Spanish-only products or should they become language-flexible? Not touched this session.

## Verify on resume
Ask Andy: "¿Alguno de estos next steps ya lo hiciste?" — especially whether the BTQ links/avatar were provided and whether the APIFY_TOKEN was rotated. Handoff reflects state at write time.
