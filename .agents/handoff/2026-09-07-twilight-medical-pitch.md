# Handoff: Twilight Medical Pitch — built, not sent

**Date:** 2026-09-07 (Monday)
**Machine:** desktop (E:\ present)
**Status:** Complete — full outbound package built and verified. **Nothing has been sent to the prospect.**

---

## What We Accomplished This Session

- **Analyzed twilightmed.com end to end** (Twilight Medical Inc., Sacramento CA — after-hours preventive maintenance on diagnostic imaging equipment + OEM parts supply; founder Travis Turner). Everything measured directly, not estimated.
- **Key findings:** Google Ads tag live with **no analytics property at all** (no GA4/GTM/UA, verified case-sensitively after a false positive); **126,957 parts pages** with ~205 words each of which only ~4 are unique; **zero pages targeting any city** despite a coast-to-coast claim; 2.25 MB / 81 requests homepage; a **malformed footer phone link** (`tel:http://(916)%20314-0164`) that does nothing on mobile; **zero of six security headers** on the site of a company selling HIPAA/NIST consulting.
- **Reframed the whole pitch** on one discovery: their `/work-with-us/` page recruits FSEs as *subcontractors* by location and modality, so the business is **supply-constrained (engineer coverage), not demand-constrained**. That produced the three-engine model (FSEs → parts → service accounts) that leads the deck and the email.
- **Confirmed it is a DIY operation:** theme is Re:bytes, a ~$60 ThemeForest "Computer Repair Service" template, plus a child theme. Yoast installed (generates all 127 sitemaps) with **zero meta descriptions set**. Hotjar installed, GA4 never was. No agency fingerprint anywhere.
- **Built and published four artifacts** (see Files below): internal teardown, client proposal, LA demo landing page, signature kit.
- **Gamma deck generated and corrected** — it invented a statistic; caught and removed (see Gotchas).
- **Deployed the LA demo to Vercel** as a new project, public with full noindex protection.
- **Wrote a 2-email outbound sequence** plus recipient verification.
- **Retrospective applied 5 changes** — Gamma + Windows-python entries in `skills/CLAUDE.md`, Vercel SSO section in `deploy-to-vercel`, contact-verification rule in `freelance-gig/workflows/build.md`, and a new catalog-gaps memory.

## Where We Paused

**Last action:** Ran `/session-close`; retrospective changes applied and verified.

**Next action:** Andrés sends `email-1-cold-open.txt` to travis.turner@twilightmed.com from andyfreelancer84@gmail.com. Everything is drafted and waiting on him.

**Blockers:** None technical. All remaining steps are Andrés's to perform.

## Files to Read First

All under `C:\Users\andre\repos\freelance-jobs\twilight-medical\` — **NOT a git repo, local to this desktop only, not backed up anywhere.**

- `email-1-cold-open.txt` — the send-ready cold email (244 words, zero links, TO/FROM at top)
- `email-2-followup.txt` — follow-up for 5–7 days later, the free DMARC fix
- `gig-brief.json` — full brief, classification, 5 open questions, and a `notVerified` list
- `proposal-twilight-medical.html` — priced proposal (send only if he asks for numbers)
- `internal-analysis.html` — blunt internal teardown, full severity
- `sample-la-landing.html` + `deploy/` — the LA demo and its Vercel deploy config
- `..\_brand\email-signature.html` — signature kit (reusable across all jobs)

**Live URLs:**
- Deck: https://gamma.app/docs/Twilight-Medical-Growth-Review-6qdloiwxcjz5wzk
- LA demo (live, public): https://twilight-la-preview.vercel.app
- Internal teardown: https://claude.ai/code/artifact/20dffecb-c61f-49ee-8eb4-4b4fd92260d7
- Proposal: https://claude.ai/code/artifact/94a9ea33-cf90-4b45-b818-b857d39f490a
- LA demo artifact: https://claude.ai/code/artifact/044ae648-2e31-4c3c-86d0-8fc5c5ca80bf
- Signature kit: https://claude.ai/code/artifact/2c36bfac-165e-4913-bda4-09a9800cf969

## Notes / Gotchas

- **Gamma invented a statistic.** With `textMode: "preserve"` explicitly set, it produced "58 clicks per 100 searches vs 41, a 41% CTR advantage" attributed to "Milestone Internet, Organic Click Curve Research (2020)". Nobody wrote that. It was removed via an edit pass and verified gone. It also ignored `themeId: slate` (shipped `blues`) and `imageOptions: themeAccent` (added 6 AI images). **Read any Gamma back before trusting it.** Now documented in `skills/CLAUDE.md`.
- **The deck still contains one unverifiable element:** a chevron `infographic` on the parts-catalog slide is a *generated image*, so text baked into its pixels cannot be checked by reading the deck. Eyeball it before showing anyone.
- **Two `[CONFIRM]` markers remain in the LA demo** (`sample-la-landing.html` and `deploy/index.html`) — the FAQ answer about LA-market response time. Deliberately not invented; needs a real number from Travis before that page goes anywhere near live.
- **Vercel deploys new projects behind `ssoProtection` by default.** The demo initially served a login wall. Disabled via API **on that project only** (`twilight-la-preview`); `website`/behind-thequeue.com, `mr-putrids-den-web` and `kuma-talent-web` were not touched.
- **Strategy decision:** the deck is deliberately **held back** — it is the reason to reply, not a link in the cold email. Email 1 has **zero links** on purpose (lowest spam score, and a reply becomes the only path forward).
- **The security finding is deliberately absent from email 1.** It is the most persuasive item and the fastest way to insult him cold. It surfaces in email 2, framed as a gift with credit for the Proofpoint/SPF he already got right.
- **Do not overstate his DMARC.** His SPF ends in `-all` (hard fail). Saying "your domain can be spoofed right now" would be an overstatement to a man who sells NIST consulting. The accurate claim, used in email 2: `fo=1` is set with no `rua`/`ruf` address, so no reports are generated at all.
- **andyfreelancer.com has no DMARC record whatsoever** and no DKIM. Email 2 hands Travis a DMARC fix — fix ours first or the asymmetry is embarrassing. DNS is authoritative at **DigitalOcean**; add records there and never change nameservers (site runs on DO App Platform behind Cloudflare).
- Sending identity is now `andyfreelancer84@gmail.com` (new Gmail). Chosen over Purelymail/Porkbun/IONOS because Travis sits behind **Proofpoint** and gmail.com's established reputation beats a cold custom domain with no sending history.

## Questions to Answer

- Did Andrés send email 1? If yes, when — email 2 goes 5–7 days later, Tue–Thu morning Pacific.
- **Add `google_ads_audit` to `services.config.js`?** Travis's most urgent problem is the one service with no price in the catalog. See `project_freelance_catalog_gaps` memory.
- Should `C:\Users\andre\repos\freelance-jobs\` become a git repo? Two client jobs now live there (`twilight-medical`, `ozimuth-logo-branding`) plus `_brand`, with zero backup.
- Third "breakup" email for the sequence — offered, not yet written.
- Purelymail ($10/yr, unlimited domains) still worth setting up for andyfreelancer/BTQ/MPD/Kuma mail, independently of this pitch.
