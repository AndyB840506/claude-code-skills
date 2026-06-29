# Build — generate the actual deliverable

Requires a `gig-brief.json` from [intake.md](intake.md).

## 1. Matched service → reuse the real methodology

If `classification.matchedServiceId` is set:
- Read `C:\Users\andre\repos\the-freelancer\freelancer\prompts\{serviceId}.md`
  live — methodology, design rules, scope definitions, truth rules for that
  specific service (see [../docs/reuse-map.md](../docs/reuse-map.md)).
- Apply the `BASE_RULES` output contract from
  `freelancer/deliverable.js`: single self-contained HTML file (when
  `deliverableType` is html), inline CSS/JS, print-safe, brand frame UNLESS the
  deliverable IS the client's own site (then it carries the client's branding),
  client's language, facts only from the brief/JD/web_fetch — unknowns go in a
  visible pending-questions marker, never guessed.
- If the prompt file is missing/renamed, tell Andy and fall back to generic
  handling below rather than failing silently.

## 2. Unmatched/custom job → scope generically

- Web/UI build → hand off to `frontend-design` or `web-page-kit` (already in
  this repo) rather than re-deriving layout/design rules here.
- Copy-only ask → draft directly, same voice bar as the proposal stage.
- Dev/automation ask → scaffold a project skeleton under
  `C:\Users\andre\repos\` matching Andy's real stack (Express/Node, DO App
  Platform — see `reference_deploy_mechanisms.md`), not a generic boilerplate
  unrelated to how Andy actually deploys.
- Still apply the same truth rules: every claim sourced from the brief/JD, no
  invented facts, no invented price.

## 3. No AI-tell giveaways — explicit requirement, not optional polish

A deliverable that reads as AI-generated risks the client relationship. This
applies to every deliverable type, not just web pages:

**Visual** (web pages, logos, graphics):
- For any web/HTML build (matched `web_page`/`social_to_web` or generic),
  read `c:\Users\andre\.claude\skills\.claude\skills\web-page-kit\docs\design-guide.md`
  Rule 0 live and run its anti-generic checklist before delivery — that file is
  the authoritative, detailed list (banned defaults, punctuation-as-filler AI
  tells like em-dash/middot/hyphen-buzzword pileups). Don't re-derive a shorter
  version here; this section is the floor for deliverable types Rule 0 doesn't
  cover (logos, standalone graphics), not a replacement for it on web work.
- For logos/graphics: no telltale font/palette defaults (Inter/Roboto/system
  fonts + purple gradient), no default-looking AI-generated stock imagery.
- Before generating, name ONE concrete, client-specific creative angle (a real
  detail from their business/JD) and build the deliverable around it instead
  of a safe template with their name swapped in.

**Written** (copy, audits, proposals):
- No formulaic AI tells: em-dash hedging, "it's not just X, it's Y," triplet
  lists, over-uniform paragraph lengths, generic transitions ("In today's
  fast-paced world..."), qualifier-stacking.
- Concrete, opinionated, varied rhythm — same voice specificity as the bot's
  playbook, not a safe neutral register.

## 4. Self-check before declaring done

Before presenting the deliverable, do one explicit pass over the draft asking:
**does anything here look or read like a template, or like AI wrote it on
autopilot?** If yes, name the specific tell and fix it — don't just note it.
This is a required step, not a suggestion.

## 5. Save and report

Save the deliverable under the gig's working folder in
`C:\Users\andre\repos\freelance-jobs\<slug>\` — never under `~/.claude`. Tell
Andy what was produced, what's still pending (from the brief's
`pendingQuestions` plus anything new), and where the file lives.
