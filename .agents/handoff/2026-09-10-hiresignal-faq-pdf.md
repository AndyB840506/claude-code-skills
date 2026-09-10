# Handoff: HireSignal client FAQ (PDF)
**Date:** 2026-09-10 (Thursday)
**Machine:** desktop (E:\)
**Status:** Complete. The FAQ PDF is delivered but NOT committed to the hiresignal repo (awaiting Andy's decision).
---
## What We Accomplished This Session
- A client FAQ for HireSignal (EN, Letter, 4 pages, "HireSignal by Kuma Talent" brand, Kuma palette + Fraunces/Inter, bear logo):
  - PDF: `C:\Users\andre\repos\hiresignal\docs\HireSignal-FAQ-2026-09.pdf`
  - Source: `C:\Users\andre\repos\hiresignal\docs\faq-hiresignal-EN.html` (render with headless Edge, see memory `reference_html_to_pdf_edge`)
- Andy's decisions (AskUserQuestion menu): mixed audience (HR buyer + IT reviewer), name the key subprocessors (Anthropic, DigitalOcean) without internals, known gaps (SOC 2, SSO, DPA/retention, SLA) as brief "Not yet" answers.
- Deliberately excluded (NDA only): weights, cut-offs, contradiction penalties, detection patterns, the prompt, model version, cost per interview.
- Every claim checked against the code at hiresignal HEAD `a083628`: the three axes + disqualifiers (`api/intelligence-engine.php` ~663-690), every interview visible in the ranking (`admin/ranking.php` ~98), single-use expiring invites, admin locked when no password is set + cookie flags, per-endpoint rate limit, database TLS (`db.php` sslmode=require), sessions in Postgres (`session-store.php`), CORS origin-locked (`api/site-cors.php`), EN/FR/ES assessment, CSV export, AI disclosure EN+FR. Anthropic quote checked via WebFetch of anthropic.com/legal/commercial-terms today.
- Retrospective: 3 memory entries — `feedback_always_show_image_paths` widened to any file with an absolute path (Andy had to ask "where is the file?"), new `reference_html_to_pdf_edge`, new `project_hiresignal_client_docs`.
- Skill-kit audit: 0 issues (29 SKILL.md, 0 over 50 lines, 0 real trigger collisions; known warning D on mrputridsden).

## Where We Paused
**Last action:** session close (retrospective + audit applied).
**Next action:** ask Andy whether to commit the 2 FAQ files to hiresignal (push to `Lucca-Tech/hiresignal` master = production redeploy).
**Blockers:** Andy's decision on the commit; confirming that `hello@kumatalent.com` is a real mailbox.

## Files to Read First
- `C:\Users\andre\repos\hiresignal\docs\faq-hiresignal-EN.html` — the HTML comment at the top lists the scope and where every claim was verified.
- `C:\Users\andre\repos\hiresignal\docs\deck-hgs-technical-security.md` — the 08-25 source, now STALE (see gotchas).

## Notes / Gotchas
- **The 08-25 technical deck is stale** compared with the switch to three axes on 08-26: it still says "Output is a verdict, a score" and "Enough critical contradictions is a rejection". The code DOES fail requirements_met on 2+ critical contradictions, but it doesn't hide the candidate. Fix it before presenting it again.
- `.do/app.yaml` says `region: nyc`; memory (`reference_kuma_infra`) says ATL1. Both are US, so the FAQ says "United States". Not resolved.
- `docs/HireSignal-costos-whitelabel-vs-RecruitX-2026-07-24.pdf` was already untracked before this session; not ours to touch.
- The FAQ's commercial commitments to review: full export at the end of the engagement and PIPEDA (both from the formal proposal already sent); "retention terms agreed in your contract" and "we will scope SSO" (new).

## Questions to Answer
- Commit the FAQ to hiresignal (triggers a deploy) or keep it outside the repo?
- Does `hello@kumatalent.com` exist? If not, which contact goes in the PDF?
- ~~Is a French version wanted?~~ Resolved: NO. Andy (2026-09-10): the FAQ is for internal use, so English is enough.
