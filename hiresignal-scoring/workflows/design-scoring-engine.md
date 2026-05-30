# Workflow: Design Scoring Engine

**Goal:** Define the scoring dimensions, weighting, and logic for the HireSignal scoring engine.

**Duration:** 1-2 days  
**Owner:** Product + backend lead  
**Output:** Approved scoring schema + rubric

---

## Step 0: Context & Prerequisites

**Read first:**
- `INDEX_HIRESIGNAL_COMPLETE.md` — Overview
- `HIRESIGNAL_EXECUTIVE_SUMMARY.md` — Why this matters
- `HIRESIGNAL_SCORING_ENGINE_SPEC.md` — Complete technical spec

**Questions to answer:**
- [ ] What are the 5-7 scoring dimensions?
- [ ] What's the weighting for each dimension?
- [ ] What's the minimum score to be "FIT"?
- [ ] How do dealbreakers override score?

---

## Step 1: Define Scoring Dimensions

**Task:** Agree on what to score

**Dimensions (recommended):**

1. **Technical Depth (20%)**
   - Problem-solving approach
   - Architecture reasoning
   - Debugging capability
   - Production experience
   - Score: 0-10

2. **Authenticity (20%)**
   - Contradiction consistency
   - Specificity of responses
   - Timeline validation
   - AI usage detection
   - Score: 0-10

3. **English Proficiency (5%)**
   - Response time
   - Vocabulary
   - Grammar
   - Comprehension
   - Score: 0-10, threshold: 5-8

4. **Behavioral/Cultural Fit (5%)**
   - Ownership mentality
   - Initiative
   - Adaptability
   - Culture alignment
   - Score: 0-10

5. **Other (50% total)**
   - Cognitive flexibility (2%)
   - Pressure resilience (1%)
   - Leadership potential (varies)

**Questions:**
- Are these the right dimensions for your roles?
- Should you add/remove any?
- Are the percentages reasonable?

---

## Step 2: Define Contradiction Severity

**Task:** How to classify inconsistencies

**Severity levels (recommended):**

| Level | Definition | Example | Override? |
|-------|-----------|---------|-----------|
| CRITICAL | Core contradiction | Timeline doesn't match | YES (dealbreaker) |
| WARNING | Significant inconsistency | Skill claim vs reality | NO (flag, analyze) |
| NOTE | Minor variation | Normal human inconsistency | NO (note only) |

**Questions:**
- Are these severity levels right?
- What other contradictions should be CRITICAL?
- How many WARNINGs = NOT_FIT?

---

## Step 3: Define Verdict Logic

**Task:** How to calculate final verdict (FIT/NOT_FIT)

**Recommended formula:**

```
Overall Score = 
  (technical × 0.20) +
  (authenticity × 0.20) +
  (english × 0.05) +
  (behavioral × 0.05) +
  (other × 0.50)

Verdict = FIT if (score ≥ 6.5 AND no CRITICAL contradictions)
Verdict = NOT_FIT otherwise

Exception: If CRITICAL contradiction detected → NOT_FIT (override)
```

**Questions:**
- Is 6.5 the right threshold?
- Should the formula be weighted differently?
- Are dealbreaker overrides correct?

---

## Step 4: Define Evidence Requirements

**Task:** What evidence to extract per dimension

**Example (Technical Depth):**

```json
{
  "dimension": "technical_depth",
  "score": 8,
  "evidence": [
    {
      "quote": "I would use a message queue to decouple the services",
      "context": "Architecture question",
      "confidence": 0.9
    },
    {
      "quote": "We had to handle 100K concurrent connections",
      "context": "Production experience",
      "confidence": 0.85
    }
  ],
  "reasoning": "Strong architecture thinking, understands tradeoffs"
}
```

**Questions:**
- How many quotes per dimension?
- How specific should "context" be?
- How to measure confidence?

---

## Step 5: Define Report Schema

**Task:** What goes in the final report

**Recommended sections:**

```json
{
  "candidate": { "name", "email", "role", "interview_date" },
  "verdict": { "recommendation", "confidence", "reasoning" },
  "scores": {
    "technical_depth": { "score", "weight", "evidence", "reasoning" },
    "authenticity": { "score", "weight", "contradictions", "reasoning" },
    ...
  },
  "contradictions_summary": { "critical": 0, "warning": 1, "note": 2 },
  "overall_score": 7.4,
  "next_steps": [...]
}
```

**Questions:**
- Is this the right structure?
- What other fields needed?
- HTML/PDF format requirements?

---

## Step 6: Approval & Documentation

**Task:** Get stakeholder sign-off

**Checklist:**
- [ ] All dimensions defined
- [ ] Weighting agreed
- [ ] Verdict logic approved
- [ ] Evidence requirements clear
- [ ] Report schema locked
- [ ] Contradiction rules finalized

**Document:** Create `scoring-schema.json` with final spec

---

## Output

**Deliverables:**
1. `scoring-schema.json` — Dimensions, weights, logic
2. `contradiction-rules.md` — How to classify issues
3. `evidence-rubric.md` — What evidence to extract
4. `report-template.json` — Final report structure

**Next step:** → `workflows/implement-tech-option.md`

---

## Reference

- Full spec: `HIRESIGNAL_SCORING_ENGINE_SPEC.md`
- Dimensions detail: `docs/scoring-dimensions.md`
- Tech options: `docs/tech-options.md`
