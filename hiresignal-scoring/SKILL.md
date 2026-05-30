---
name: hiresignal-scoring
description: "Build and deploy HireSignal scoring engine (transcript → verdict + evidence). Use when implementing scoring infrastructure, generating interview reports, analyzing contradictions, or deploying candidate evaluation system. English triggers: score interview, build scoring engine, generate interview report, analyze transcript, detect contradictions, deploy scoring system, candidate evaluation. Triggers ES: puntuar entrevista, motor de scoring hiresignal, evaluar candidato, analizar transcripción, reporte de entrevista, implementar scoring, desplegar motor de puntuación, construir sistema de evaluación, sistema de scoring."
---

# HireSignal Scoring Skill

Automate the design and implementation of the scoring engine that converts raw interview transcripts into structured verdicts with evidence.

## Quick Start

**Goal:** Convert interview transcript → candidate verdict + evidence

**Workflow:**
1. **Design phase** → `workflows/design-scoring-engine.md`
2. **Implementation** → `workflows/implement-tech-option.md`
3. **Testing & deployment** → `workflows/test-and-deploy.md`

**Key documents** (in the HireSignal project, not inside this skill folder):
- Technical spec: `docs/hiresignal/HIRESIGNAL_SCORING_ENGINE_SPEC.md`
- Tech options: `docs/hiresignal/HIRESIGNAL_SCORING_TECH_OPTIONS.md`
- Business case: `docs/hiresignal/HIRESIGNAL_EXECUTIVE_SUMMARY.md`

## Common Tasks

| Need | Workflow |
|------|----------|
| Design scoring dimensions | `workflows/design-scoring-engine.md` |
| Choose tech stack | `workflows/implement-tech-option.md` |
| Build API endpoints | `workflows/implement-tech-option.md` |
| Create report templates | `workflows/test-and-deploy.md` |
| Deploy to production | `workflows/test-and-deploy.md` |
| Monitor accuracy | Ver scoring dimensions y contradiction detection arriba |
| Troubleshoot contradictions | `docs/hiresignal/INDEX_HIRESIGNAL_COMPLETE.md` *(HireSignal project only)* |

## Scoring Dimensions (20-20-5-5-50 Model)

```
Technical Depth    (20%)  → Architecture, debugging, production knowledge
Authenticity       (20%)  → Consistency, specificity, AI detection
English            (5%)   → Response time, vocabulary, grammar
Behavioral/Culture (5%)   → Ownership, initiative, team fit
Other              (50%)  → Context-sensitive signals
```

### What "Other (50%)" Includes

The remaining 50% weight evaluates context-specific signals based on role and company:

**Primary signals:**
- **Recency bias** — How current is the candidate's knowledge? (Recent bootcamp grad vs 10-year veteran)
- **Red flags** — Unexplained gaps, contradictions between statements, vague answers
- **Problem-solving approach** — How structured is their thinking? (trial-and-error vs methodical)
- **Communication clarity** — Can they explain complex ideas simply?

**Secondary signals (by role):**
- *Backend role:* Database design, system architecture, scalability thinking
- *Frontend role:* User experience thinking, accessibility awareness, component design
- *Full-stack role:* End-to-end system design, API-frontend integration
- *DevOps role:* Deployment strategy, monitoring, incident response

**Example evaluation:**
- Candidate answers technical questions perfectly (40/40 points)
- But describes 3 major contradictions in career timeline (-15 points, CRITICAL penalty)
- Shows problem-solving approach (+10 points for methodology)
- **Final Other score:** 35/50

**Full dimensions & scoring rubric:** `workflows/design-scoring-engine.md`

## Contradiction Detection & Penalties

Contradictions directly reduce score and indicate authenticity issues:

| Severity | Impact | Examples | Penalty |
|----------|--------|----------|---------|
| **CRITICAL** | Major inconsistency, likely fabrication | "Worked at Google 2020-2022" but resume says "Freelancer 2020-2022"; Claims expertise in tech released after interview date | **-15 points** |
| **WARNING** | Moderate inconsistency, needs clarification | "Senior engineer for 5 years" but describes junior-level work; Salary expectation misaligned with experience | **-5 points** |
| **NOTE** | Minor discrepancy, documented | Different tech names for same tool; Slight timeline overlap | **0 points** (flag for review) |

**How to detect:**
1. Extract timestamps and role names
2. Cross-check with LinkedIn, resume, or stated experience
3. Look for logical inconsistencies (e.g., "led team of 10" but "first leadership role")
4. Flag timeline gaps > 6 months

## Confidence Calculation

**Confidence = percentage of dimensions with STRONG evidence**

| Strong Evidence in | Confidence Multiplier |
|-------------------|----------------------|
| 5/5 dimensions | 100% |
| 4/5 dimensions | 85% |
| 3/5 dimensions | 70% |
| 2/5 dimensions | 50% |
| 1/5 dimensions | 25% |
| 0/5 dimensions | 0% (insufficient data) |

**What counts as STRONG evidence:**
- Direct quote demonstrating mastery or clear contradiction
- Specific example (not vague statement)
- Corroborated across multiple answers
- Timestamps/verifiable facts

**Example:**
- Candidate answers 5 dimensions: Technical (strong), Authenticity (strong), English (medium), Behavioral (weak), Other (strong)
- Confidence = 3/5 strong = **70%**
- Score 72, Confidence 70 → Verdict: **MAYBE**

## Verdict Format

Every scoring result returns this JSON structure:

```json
{
  "verdict": "HIRE|MAYBE|REJECT",
  "score": 72,
  "confidence": 70,
  "dimensions": {
    "technical_depth": 18,
    "authenticity": 16,
    "english": 4,
    "behavioral_culture": 4,
    "other": 30
  },
  "evidence": [
    { "quote": "...", "dimension": "technical_depth", "weight": "strong" },
    { "quote": "...", "dimension": "authenticity", "weight": "warning" }
  ],
  "contradictions": [
    { "type": "CRITICAL", "description": "...", "penalty": -15 }
  ],
  "timestamp": "2026-05-15T14:30:00Z"
}
```

**Minimum Data Requirements (Check FIRST):**

Before scoring, validate:
- **Minimum transcript length:** ≥ 5 minutes of interview content
- **Minimum answers per dimension:** ≥ 3 substantive answers per dimension (5 total)
  - "I don't know" doesn't count as an answer
  - One-word answers don't count
- **Minimum interviewer presence:** Interviewer must ask ≥ 1 question per dimension

**If requirements NOT met:**
- Return `verdict: "REJECT"`
- Set `score: 0`
- Set `confidence: 0`
- Add to response: `"insufficient_data": true`
- Message: "Transcript too short or lacks substantive answers across dimensions. Requires ≥5 min, ≥3 answers per dimension."

**Verdict rules (after validation):**
- `HIRE` — Score ≥ 75, confidence ≥ 80%, no CRITICAL contradictions
- `MAYBE` — Score 50–74 OR confidence 50–79% OR 1 WARNING contradiction
- `REJECT` — Score < 50 OR ≥ 2 CRITICAL contradictions OR (insufficient data confirmed)

## Current Status

**Phase:** Scoring engine build (Priority 1)  
**Timeline:** 2 weeks to MVP  
**Tech recommendation:** Claude API option  
**Owner:** Backend engineer  

**Related docs** *(paths relative to HireSignal project root — only available when working in that project):*
- `docs/hiresignal/INDEX_HIRESIGNAL_COMPLETE.md` — All HireSignal documentation
- `docs/hiresignal/HIRESIGNAL_EXECUTIVE_SUMMARY.md` — Business case
- `docs/hiresignal/HIRESIGNAL_SCORING_ENGINE_SPEC.md` — Complete spec
