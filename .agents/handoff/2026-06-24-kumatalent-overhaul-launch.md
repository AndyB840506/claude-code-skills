# Handoff: Kuma Talent overhaul + subdomain launch + HireSignal invite fix
**Date:** 2026-06-24
**Status:** Complete
---
## What We Accomplished This Session

- **Kuma Talent marketing overhaul** (`C:\Users\andre\repos\kuma-talent-web\index.html`): premium editorial redesign, de-boxed audiences + Why Kuma grids (border dividers, not nested cards), "K" brand mark in nav. Deployed to Vercel (project `kuma-talent-web`, account mrputridsden).
  - Fixed a **CSS class collision**: the audiences "For Candidates" column reused `class="aud cand"`, inheriting the hero shortlist's `.cand { display:grid; 38px 1fr auto }` and crushing the column. Renamed to `.candidates`.
  - **Stripped all dash/slash filler** (recurring user feedback "veo muchos - y /"): removed every em-dash clause, middot "·" separator, and hyphen-buzzword pileup (interview-ready, time-to-hire, pre-screened, AI-administered, no-show). Verified 0 em-dashes / 0 middots in visible copy.
- **Subdomain architecture live**: `kumatalent.com` + `www` → marketing site (Vercel); `app.kumatalent.com` → HireSignal (DO App Platform `hiresignal-pqsee`). DNS authoritative on DigitalOcean, registrar GoDaddy, email MX preserved. Apex set as the **serving/production** domain in Vercel (www redirects/also serves).
- **HireSignal invite-link fix** (`C:\Users\andre\repos\hiresignal`): invite links were hardcoded to `www.kumatalent.com` via `config.php` `PUBLIC_BASE_URL` default. Changed default to `https://app.kumatalent.com` + Dockerfile `ServerName`. Committed `f6ceada`, pushed to `origin` (Lucca-Tech/hiresignal) master → DO auto-deploy (`deploy_on_push: true`). User confirmed new invites now stamp `app.kumatalent.com` ("ya quedó").
- **Rescue redirect** for invites already sent: `vercel.json` in kuma-talent-web redirects `/index.php → app.kumatalent.com/index.php` (307, query string preserved). Verified live.
- **Skill update** (retrospective): web-page-kit `docs/design-guide.md` Rule 0 — expanded the em-dash ban into a full "punctuation-as-filler" family (em-dash + middot + hyphen-buzzwords) with a grep verification, since this feedback recurred across Lucca + Kuma.
- **Memory:** added `reference_kuma_infra.md` (indexed in MEMORY.md) capturing the full topology, deploy mechanisms, and the Vercel-cert-churn gotcha.

## Where We Paused
**Last action:** Session-close ritual — applied retrospective edit to design-guide.md, audit passed clean, writing this handoff.
**Next action:** Nothing required — work is complete and verified live.
**Blockers:** None.

## Files to Read First
- `memory/reference_kuma_infra.md` — Kuma/HireSignal infra, deploy paths, gotchas
- `C:\Users\andre\repos\hiresignal\config.php` (line ~72) — `PUBLIC_BASE_URL` default
- `C:\Users\andre\repos\kuma-talent-web\vercel.json` — the invite-link rescue redirect

## Notes / Gotchas
- **Don't churn Vercel custom domains** — removing/re-adding resets Let's Encrypt issuance and rate-limits the cert. The www cert got stuck this way; fix that worked was setting the apex as the serving domain (its cert issued fast) and leaving www alone to recover.
- **Don't move nameservers to Vercel** — DO must stay authoritative (it holds the app CNAME + MX). Adding `ns*.vercel-dns.com` records *inside* the DO zone is inert (delegation is at the registrar).
- HireSignal has **no admin-UI field** for the base URL; it reads the `config.php` default. To switch domains later, edit config.php or add a Settings field.
- **Security:** a DO env-vars screenshot exposed live secrets — `SMTP_PASS` (Gmail app password), `ADMIN_PASSWORD` (`KumaAdmin2026`), `ANTHROPIC_API_KEY`. Recommended the user rotate them; not yet done.

## Questions to Answer
- (Optional, user's call) Rotate the exposed HireSignal secrets?
- (Optional) Add a "Public Base URL" field to HireSignal's admin Settings so future domain changes don't need a code push?
