# Intake — JD/requirement in, structured brief out

## 1. Get the input

Ask how the job came in if not already given, then take it as one of:
- **Pasted text** — JD or client brief, used as-is.
- **A URL** — Upwork/Fiverr/LinkedIn listing or similar. Use WebFetch to get
  the page content.
- **A file** — PDF/email/doc. Use Read (PDF-capable).

## 2. Extract the brief

From the raw input, pull out:
- What the client actually wants (one or two sentences, concrete — not a
  re-statement of the whole JD).
- Platform/source (Upwork, Fiverr, direct email, referral, etc.).
- Any deadline or budget signals mentioned.
- Client's existing site/socials if mentioned anywhere — note URLs so
  `build.md` can `web_fetch` them later.
- Language the JD/client is writing in (drives both pitch and deliverable
  language later).

If a fact you need isn't in the input, leave it blank and add a question to
`pendingQuestions` — never guess. (Truthfulness rule #1: no invented data.)

## 3. Classify against the known service catalog

Read `C:\Users\andre\repos\the-freelancer\services.config.js` live (see
[../docs/reuse-map.md](../docs/reuse-map.md) for the exact fields). Normalize
the client's request and each service's `id`/`name.en`/`name.es` the same way
`resolveServiceId()` does in `deliverable.js` — lowercase, strip accents, strip
non-alphanumerics, then substring-match. If it matches, record
`matchedServiceId` and `matchedServiceName`. If it doesn't clearly match any of
the 7, mark it as a **custom job** — don't force a weak match.

If the file is missing or its structure has changed, say so to Andy and
continue with a custom-job classification rather than failing.

## 4. Save the brief

Fill out `../templates/gig-brief.json` with everything gathered above. Ask
Andy where to save it — default to
`C:\Users\andre\repos\freelance-jobs\<slug>\gig-brief.json` (slug = short
kebab-case from client/company name or platform+date). Never save under
`~/.claude`.

## 5. Ask which stage(s) to run

Don't assume. Ask Andy conversationally: pitching only, already won (go
straight to build), or both in sequence. Set `stage.wantsProposal` /
`stage.wantsBuild` in the brief accordingly, then hand off to
[proposal.md](proposal.md) and/or [build.md](build.md).
