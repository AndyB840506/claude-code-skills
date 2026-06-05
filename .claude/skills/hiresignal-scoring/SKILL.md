---
name: hiresignal-scoring
description: "Interview candidate scoring engine for HireSignal. Takes an interview transcript and job description, scores the candidate across 7 dimensions (Technical Depth, Authenticity, English Proficiency, Behavioral Fit, Cognitive Flexibility, Pressure Resilience, Culture-Specific Fit), detects contradictions, applies verdict logic, and generates a confidential HTML assessment report. Triggers (EN): score candidate, interview assessment, hiresignal score, candidate evaluation, interview report, score interview transcript, generate candidate report, interview scoring, assess candidate, hiring decision report. Triggers (ES): puntuar candidato, evaluar entrevista, reporte de candidato, scoring de entrevista, evaluación de candidato, generar reporte de entrevista, hiresignal scoring, decisión de contratación."
---

# HireSignal Scoring Engine

Scores an interview transcript against 7 weighted dimensions and outputs a
confidential HTML assessment report for internal staff only.

Schema: `config/scoring-schema.json` · Template: `config/report-template.json`

---

## Step 0 — Gather inputs

Ask in a single message:

> To generate the assessment report I need:
>
> 1. **Interview transcript** — paste or attach the full transcript
> 2. **Job description** — paste the JD or describe the role + seniority level
> 3. **Culture factor** (optional) — startup / leadership / corporate / remote /
>    collaborative (default: none)
> 4. **English threshold** (optional) — minimum English score required (default: 7)

Do not advance to Step 1 until the transcript and JD are provided.

---

## Step 1 — Load schema and score

Read `config/scoring-schema.json`.

Score each dimension (0–10) with exactly 3 evidence quotes per dimension:

| Dimension | Default weight |
|-----------|---------------|
| Technical Depth | 0.34 |
| Authenticity | 0.33 |
| English Proficiency | 0.08 |
| Behavioral Fit | 0.08 |
| Cognitive Flexibility | 0.03 |
| Pressure Resilience | 0.02 |
| Culture-Specific Fit | 0.12 |

Adjust weights based on the JD if role-specific priorities are evident.
All weights must sum to 1.0.

**Dealbreaker check (apply before computing overall score):**
- CRITICAL_CONTRADICTION → auto REJECT regardless of score
- UNREACHABLE (3+ failed attempts) → auto REJECT
- INTERVIEW_ABANDONMENT → auto REJECT
- ENGLISH_THRESHOLD_FAIL → auto REJECT if score < threshold

**Verdict thresholds by seniority:**
- Junior: 6.0 · Mid: 6.5 · Senior: 7.0 · Leadership: 7.5

---

## Step 2 — Contradiction analysis

Classify every detected inconsistency:
- **CRITICAL** — timeline/location/role mismatch → dealbreaker
- **WARNING** — skill claim vs demonstrated ability → affects authenticity score
- **NOTE** — minor memory variance → document only, no penalty

---

## Step 3 — Generate HTML report

Read `config/report-template.json`.

Render the full HTML with all sections:
1. Header (candidate name, position, interview date)
2. Executive summary (verdict, overall score, confidence %)
3. Scoring breakdown (7 dimensions with evidence quotes)
4. Contradiction analysis
5. Overall assessment with score formula
6. Recruiter notes + questions for next round
7. Next steps
8. Confidentiality footer

**File:** `hiresignal-report-[candidate-slug]-[YYYY-MM-DD].html`

**Security:** CONFIDENTIAL — Internal Staff Only. Never share with candidates.

Open the file after writing:
```powershell
Start-Process "hiresignal-report-[candidate-slug]-[YYYY-MM-DD].html"
```

---

## Step 4 — Chat summary

```
Report generated: hiresignal-report-[name]-[date].html
Candidate: [name]
Position: [title]

Verdict: PASS / PASS-CONDITIONAL / REJECT
Overall score: X.X/10 (threshold: X.X)

Dimension scores:
  Technical Depth:       X/10
  Authenticity:          X/10
  English Proficiency:   X/10 [PASS/FAIL threshold X]
  Behavioral Fit:        X/10
  Cognitive Flexibility: X/10
  Pressure Resilience:   X/10
  Culture-Specific Fit:  X/10

Contradictions: X CRITICAL · X WARNING · X NOTE
Dealbreakers: [none / list]

Top concern: [one sentence]
```
