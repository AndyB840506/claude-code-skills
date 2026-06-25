# Handoff: Kuma Talent — Warm Den redesign + free CV-capture

**Date:** 2026-06-25
**Status:** Complete — site live, CV capture verified end-to-end

---

## What We Accomplished This Session

- **Finished & deployed the "Warm Den" redesign** of `kumatalent.com` (Vercel `kuma-talent-web`): earth-tone palette (terracotta/ochre/sage/espresso/cream), Fraunces + Outfit fonts, single-line bear + signal-wave logo with CSS draw-in animation.
- **Removed the AI-look tells** the owner flagged: dash/slash pileups and "cards on top of cards" (float-chip).
- **Collapsed all CTAs to a single "Join Kuma"** button (nav + hero + audiences + CTA band + footer, 7 spots). They no longer link to HireSignal and **no email/mailto appears anywhere** in the static HTML (verified 0 traces of gmail/kumatalent49/mailto/app.kumatalent.com).
- **Built a free candidate-CV capture system** with NO paid service, NO respondent login, NO email exposed, NO DigitalOcean load:
  - `#join` on-site form with **Candidate / Employer tabs** (Candidate → CV file-upload; Employer → Company field).
  - JS reads CV as base64 → `fetch(..., {mode:'no-cors'})` POSTs JSON to a **Google Apps Script web app** → saves CV to Drive folder *"Kuma Talent - CVs"* + appends a row to Sheet **"Kuma Talent Database"** (`18Q4_asLlyBO0c752nVfErHxgRKuRXDn8-LbWkJruin0`).
  - Verified live: endpoint returned `{"success":true}`; owner confirmed the attachment landed in the Sheet and the file in Drive.
- **Replaced the 🇨🇦 emoji** (renders as "CA" on Windows) with an inline SVG Canadian flag at hero "Proudly Canadian" + footer.
- **Retrospective applied** to `web-page-kit/docs/design-guide.md`:
  1. Flag/regional-indicator emojis don't render on Windows → use inline SVG flag (extended the emoji-as-icons ban).
  2. New note on capturing files/CVs free with no login (Web3Forms can't attach files; Google Forms forces Google sign-in; Apps Script web app → Drive + Sheet).
- **Memory updated:** `reference_kuma_infra.md` documents the Warm Den redesign + the Apps Script CV-capture architecture, the incognito/authuser gotcha, and the no-cors note.

## Where We Paused

**Last action:** Applied the two retrospective diffs to `design-guide.md`; ran the skill audit (clean); writing this handoff.
**Next action:** Commit design-guide.md + this handoff, push to GitHub. Session is otherwise closed.
**Blockers:** None. Owner confirmed all previously-exposed secrets were rotated.

## Files to Read First

- `C:\Users\andre\repos\kuma-talent-web\index.html` — the live page (Warm Den + #join form + Apps Script URL).
- `~/.claude/projects/.../memory/reference_kuma_infra.md` — full infra + CV-capture architecture and gotchas.
- `.claude/skills/web-page-kit/docs/design-guide.md` — updated emoji + static-form notes.

## Notes / Gotchas

- **Deploy:** `vercel deploy --prod --yes --cwd "C:\Users\andre\repos\kuma-talent-web"` — NOT git push.
- **Apps Script editor** throws "unable to open the file" when multiple Google accounts are logged in (`authuser=1` mismatch) → use an **incognito window signed in only as kumatalent49**.
- Apps Script returns no CORS headers → form uses `no-cors` (opaque response), shows optimistic success.
- Keep `kumatalent49@gmail.com` OFF the page (owner's hard rule).

## Questions to Answer

- Owner planned to delete the "SETUP TEST" row from the Sheet — confirm it's gone (owner's task).
