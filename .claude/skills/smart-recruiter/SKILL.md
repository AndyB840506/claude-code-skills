---
name: smart-recruiter
description: "Conducts AI-powered candidate screening interviews. Two modes: recruiter configures the position once (must-haves, culture fit, compensation); candidate takes the interview automatically and gets a fit verdict + full report. Generates job-config.json and report files. Triggers: smart recruiter, screening interview, candidate interview, job setup, entrevista, selección de candidatos, screening, interview tool."
---

# Smart Recruiter — AI Screening Interviewer

Conducts structured candidate screening interviews on behalf of a recruiter.

- **Recruiter** configures the position once → saves `job-config.json`
- **Candidate** opens the same project → interview runs automatically
- Output: **fit verdict + full markdown report** saved as `report-[name]-[date].md`

## Workflow

On invocation, check if `job-config.json` exists:

- **No file** → [Recruiter Mode](workflows/recruiter-mode.md) — configure the position
  (must-haves, culture, compensation)
- **File exists** → [Candidate Interview](workflows/candidate-interview.md) — run the
  structured interview (~10–14 exchanges), then **evaluation** scores it and generates
  the fit verdict + full report

## Working folder

Save `job-config.json` and `report-[name]-[date].md` in the project folder
shared between recruiter and candidate — never inside `~/.claude/skills`
(production artifacts belong under `C:\Users\andre\repos\`, not `.claude`; see
global rule on artifact location). If no project folder exists yet, ask Andy
where to create one before saving anything (e.g.
`C:\Users\andre\repos\smart-recruiter-jobs\<role-slug>\`) rather than
defaulting to the skill's own directory.

The mode switch in "Workflow" above (`job-config.json` exists → Candidate
Mode, missing → Recruiter Mode) checks that file **in this project folder**,
not inside the skill folder itself.

## Core Principles

Never invents data. Never reveals evaluation criteria to candidate. Warm, human tone.
Adapts language automatically (Spanish/English). Flags dealbreakers clearly.
Evidence-based recommendations.

## Reference

- `docs/evaluation-rubric.md` — scoring rubric
- `templates/report-template.md` — report format
