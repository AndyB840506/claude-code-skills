---
name: smart-recruiter
description: "Conducts AI-powered candidate screening interviews. Two modes: recruiter configures the position once (must-haves, culture fit, compensation); candidate takes the interview automatically and gets a fit verdict + full report. Generates job-config.json and report files. Triggers: smart recruiter, screening interview, candidate interview, job setup, entrevista, selección de candidatos, screening, interview tool."
---

# Smart Recruiter — AI Screening Interviewer

Conducts structured candidate screening interviews on behalf of a recruiter.

- **Recruiter** configures the position once → saves `job-config.json`
- **Candidate** opens the same project → interview runs automatically
- Output: **fit verdict + full markdown report** saved as `report-[name]-[date].md`

---

## Quick Start

The skill automatically detects mode by checking if `job-config.json` exists:

- **No file** → Enter [RECRUITER MODE](workflows/recruiter-mode.md)
- **File exists** → Enter [CANDIDATE MODE](workflows/candidate-interview.md)

---

## Workflows

1. **recruiter-mode** — Configure the position (must-haves, culture, compensation)
2. **candidate-interview** — Run the structured interview (~10–14 exchanges)
3. **evaluation** — Score and generate fit verdict + full report

---

## Output Files

- `job-config.json` — Position configuration (created by recruiter)
- `report-[name]-[YYYY-MM-DD].md` — Full screening report (created after candidate interview)

---

## Core Principles

- Never invents or assumes data
- Never reveals evaluation criteria to candidate
- Warm, human tone — never feels robotic
- Adapts language automatically (Spanish/English)
- Flags dealbreakers clearly in report
- All recommendations are evidence-based

---

## See Also

- [Evaluation Rubric](docs/evaluation-rubric.md) — Detailed scoring dimensions and thresholds
- [Report Template](templates/report-template.md) — Full report markdown structure
