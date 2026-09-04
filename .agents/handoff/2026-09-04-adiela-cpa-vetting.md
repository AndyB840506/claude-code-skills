# Handoff: Adiela Gomez CPA Deal — Vetting Prep

**Date:** 2026-09-04
**Machine:** desktop (workspace: kit-skill-creator)
**Status:** Complete — nothing pending in this repo; next action is Andres's, off-repo (a meeting)

---

## What We Accomplished This Session

- Evaluated a LinkedIn CPA/affiliate lead-gen offer from Adiela Gomez: up to $250 USD per qualified lead (married, US-citizen Latino) who attends a commercial presentation for a high-value financial product.
- Confirmed existing tools (`AI Lead Generator`, `apify-scraper`) don't fit — both are B2B lead-gen (companies/decision-makers), this is B2C consumer lead-gen with demographic targeting + event-attendance conversion.
- Talked through funnel options (landing page + WhatsApp/community channel vs. paid Meta ads) and the custom-domain requirement (no bare `*.vercel.app`, same pattern as BTQ).
- Andres flagged the "sounds like a pyramid scheme" risk himself; walked through the real legal distinction (FTC Business Opportunity Rule test: pay-per-verified-attendance = legit CPA; pay-to-join or recruiting-driven income = pyramid flag).
- Built and published an Artifact — **CPA Vetting Dossier** (`https://claude.ai/code/artifact/684c9c0d-736e-4d0b-a10d-cd6a79ebe5ad`) — a live-use checklist for Andres's meeting with Adiela: 3 sidebar "tripwire" questions (payout trigger, pay-to-join fee, licensing) plus 12 full clarification questions across Legitimacy & Compensation / Product & Compliance / Resources, with checkboxes + note fields that persist via localStorage.
- Saved project memory (`project_adiela_gomez_cpa_deal.md`) — this hadn't been captured proactively during the conversation, so it was added at session-close.

## Where We Paused

**Last action:** Published the CPA Vetting Dossier artifact and ran `/session-close`.
**Next action:** Andres meets Adiela and works through the dossier's questions — especially the 3 tripwires (payout trigger, pay-to-join, licensing).
**Blockers:** Everything downstream depends on Andres's answers from that meeting. The parallel scraping task (finding Latino community FB/IG groups to promote in) is explicitly **not started** — it needs platform, geography, and target volume from Andres before `apify-scraper` runs (it costs money per run).

## Files to Read First

- `project_adiela_gomez_cpa_deal.md` (memory) — full deal terms, the 3-question gate, and what's still open.
- The published dossier artifact itself (link above) — treat it as the primary record of the questions; don't re-derive them from this handoff.

## Notes / Gotchas

- No repo files changed this session — this was advisory conversation + one published Artifact. `git status` is clean.
- Don't assume the deal is viable — it's explicitly unvetted. Ask Andres what Adiela answered before proposing any build (landing page, WhatsApp funnel, ad campaign).

## Questions to Answer

- Did Adiela's answers pass the 3 tripwires (attendance-triggered payout, no pay-to-join, licensing accounted for)?
- If yes: platform(s), geography, and target group count for the `apify-scraper` community-group search.
