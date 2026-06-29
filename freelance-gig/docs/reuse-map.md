# Reuse Map — `the-freelancer` repo

This skill never copies these files into itself. Read them live, every run, from
`C:\Users\andre\repos\the-freelancer\` — that way the skill can't drift from
Andy's production system. If any path below is missing or renamed, tell Andy and
fall back to generic handling (don't fail silently, don't guess at a replacement).

## Service catalog

`C:\Users\andre\repos\the-freelancer\services.config.js`
7 services: `lead_generation`, `web_page`, `seo_audit`, `business_audit`,
`social_to_web`, `meta_ads_audit`, `copywriting`. Each has `id`, bilingual
`name`/`description`, `scopes` (tiered low/high USD), `intakeQuestions`,
`deliverableType`.

Classify a JD against this catalog the same way `resolveServiceId()` does in
`freelancer/deliverable.js` (lines ~26–35): normalize both sides (lowercase,
strip accents, strip non-alphanumerics) and match against `id`, English `name`,
or Spanish `name` via substring containment.

## Voice playbook

`C:\Users\andre\repos\the-freelancer\freelancer\bot.js` — `SYSTEM_PROMPT`
(lines ~10–117). Persona "Andy": sharp, curious, confident, not salesy,
trilingual (match client's language). Conversational craft rules: one
genuinely useful micro-insight, mirror energy, react to substance before
asking the next question, never discount below range (reframe to value
instead), celebrate the close, vary phrasing — never open two consecutive
messages the same way.

Regional pricing table (lines ~38–50) and the rule "NEVER invent pricing
outside the ranges above" (line ~110) — pull from there, never from memory or
estimation.

## Deliverable output contract

`C:\Users\andre\repos\the-freelancer\freelancer\deliverable.js` —
`BASE_RULES` constant (lines ~12–23): single self-contained HTML file, inline
CSS/JS, print-safe colors, brand frame ("The Freelancer", teal #0d9488) for
reports/audits, EXCEPTION: client's own branding when the deliverable IS their
website (Web Page Kit, Social Profile to Web). Write in the client's language.
Truth rules: only facts from the transcript/JD/tools actually used; unknowns go
in a visible "Preguntas pendientes / Pending questions" section, never guessed.

## Per-service deliverable prompts

`C:\Users\andre\repos\the-freelancer\freelancer\prompts\{service_id}.md` — one
file per matched service (e.g. `web_page.md`), each with its own methodology,
design rules, scope definitions, and truth rules. Read the one matching the
classified `serviceId`.

## What this skill adds (not in `the-freelancer`)

- Classifying an *external* JD (Upwork/Fiverr/direct text/file) into this
  catalog — the bot only ever sees orders that already came through Andy's own
  site form.
- Handling unmatched/custom jobs gracefully (the bot has no fallback for "not
  one of the 7 services").
- An explicit no-AI-tell self-check before any deliverable is called done — see
  `workflows/build.md`.
