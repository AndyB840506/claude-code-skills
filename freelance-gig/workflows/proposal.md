# Proposal — pitch in Andy's voice

Requires a `gig-brief.json` from [intake.md](intake.md).

## 1. Load the voice playbook live

Read `SYSTEM_PROMPT` in
`C:\Users\andre\repos\the-freelancer\freelancer\bot.js` (see
[../docs/reuse-map.md](../docs/reuse-map.md)). Pull from it, don't paraphrase
from memory:
- Persona: Andy — sharp, curious, confident, not salesy.
- Language: match the client's language exactly (from the brief).
- Conversational craft: one genuine micro-insight about THEIR business (not
  generic flattery), mirror their energy/formality, react to substance, vary
  phrasing — a pitch is one "turn," so this mostly shapes tone and the opening
  line, not a back-and-forth.
- Never discount below the established range — if budget signals in the brief
  look tight, reframe to value or propose the smaller scope honestly instead of
  inventing a lower number.

## 2. Pricing — never invented

- **Matched service**: surface the existing price range from
  `services.config.js` for the matched `serviceId` (use the appropriate scope
  tier if the brief's budget/scope signals point to one; otherwise give the
  full range). This is a reference, not a final quote.
- **Custom/unmatched job**: do not suggest any number. Say scope needs a quick
  scoping conversation before pricing, consistent with "no invented data" and
  the global no-suggested-pricing principle.

## 3. Write the pitch

One pitch, ready to paste into the platform or send as an email/DM:
- Open by speaking to something specific in their actual JD/business — never a
  generic opener ("I am writing to express interest...").
- Show, don't claim, relevant capability — one concrete angle tied to their
  request.
- State scope and (if matched) price range plainly.
- Clear, low-friction next step (a question, not a hard CTA).
- No AI-writing tells: no "not just X, it's Y," no triplet lists, no generic
  transitions, no qualifier-stacking. Read it back once before presenting —
  would a sharp, busy freelancer actually have written this turn?

## 4. Output

Give Andy the pitch text directly. If the gig is also going to build
([build.md](build.md)), say so and ask whether to proceed now or pause here.
