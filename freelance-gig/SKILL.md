---
name: freelance-gig
description: "Turn a freelance job posting or client requirement into a pitch and/or a finished deliverable, in Andy's real voice and pricing. Reuses the live services/voice/prompt config from the-freelancer repo instead of generic templates. Triggers: freelance job, job posting, JD, client brief, Upwork, Fiverr, freelance proposal, pitch this gig, quote this job, build this gig."
---

# Freelance Gig — JD In, Pitch and/or Deliverable Out

For freelance work found outside andyfreelancer.com's own intake bot (Upwork, Fiverr,
direct outreach, anything not already automated). Reuses Andy's real service catalog,
pricing, voice playbook, and deliverable prompts live from `the-freelancer` repo — see
[docs/reuse-map.md](docs/reuse-map.md) for exact pointers. Never invents prices or facts.

## Workflow

1. **Intake** — [workflows/intake.md](workflows/intake.md)
   Take the JD (pasted text, URL, or file), extract the brief, classify against the
   7 known services, save `gig-brief.json`, ask which stage(s) to run.
2. **Proposal** — [workflows/proposal.md](workflows/proposal.md)
   Draft a pitch in Andy's voice. Surfaces an existing price range only if matched;
   never invents one.
3. **Build** — [workflows/build.md](workflows/build.md)
   Generate the actual deliverable, matched or custom. Includes a mandatory
   no-AI-tell self-check before declaring anything ready.

Start at intake unless a `gig-brief.json` already exists for this gig (then ask
which stage to resume). Default working folder: `C:\Users\andre\repos\freelance-jobs\<slug>\`
— never under `~/.claude`.
