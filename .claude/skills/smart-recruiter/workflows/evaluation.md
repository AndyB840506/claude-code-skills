# Workflow: Evaluation — Score & Generate Report

Run after the candidate interview closes.

## Step 1: Score Each Dimension

Use the rubric from [evaluation-rubric.md](../docs/evaluation-rubric.md). Score each:

| Dimension | Weight | Score |
|---|---|---|
| Must-have requirements met | 40% | 0–10 |
| Cultural fit | 20% | 0–10 |
| Motivation & expectations alignment | 20% | 0–10 |
| Communication & soft skills | 20% | 0–10 |

Calculate weighted score.

## Step 2: Determine Verdict

Apply thresholds:

- **Strong Fit** (8.0–10): Recommend to advance
- **Possible Fit** (5.0–7.9): Advance with reservations
- **Not a Fit** (0–4.9): Do not recommend

## Step 3: Display Quick Summary

Show in chat:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCREENING RESULT — [Candidate Name]
Position: [Job Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDICT: [Strong Fit / Possible Fit / Not a Fit]
Score: [X.X / 10]

✅ Top strengths:
  • [Strength 1]
  • [Strength 2]

⚠️  Main concern:
  • [Concern]

Full report saved → report-[name]-[date].md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Step 4: Generate Full Report

Save as `report-[candidate-name]-[YYYY-MM-DD].md`

Use the structure from [report-template.md](../templates/report-template.md), filling in:

- Candidate name and position
- Scores for each dimension
- Strengths (with evidence from interview)
- Concerns/gaps
- Notable quotes
- Salary expectations
- Final recommendation (2–3 sentences for hiring team)

Include only evidence from the actual interview — never assume or invent data.
