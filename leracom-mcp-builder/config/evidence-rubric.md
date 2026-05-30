# HireSignal Evidence Extraction Rubric

> ⚠️ **Fuente canónica:** `hiresignal-scoring/docs/evidence-rubric.md`
> Este archivo es una copia de referencia para leracom-mcp-builder.
> Si la rúbrica cambia, actualizar la fuente primaria primero, luego sincronizar aquí.

**Status:** Locked per Step 0 Requirements (2026-05-12)  
**Owner:** Scoring Engine  
**Purpose:** Standardize evidence extraction for each dimension

---

## Overview

Each dimension requires **3 direct quotes** from the transcript with:
- Direct quote text
- Context (question/topic being discussed)
- Confidence score (0.7-1.0)
- Reasoning (why this supports the score)

---

## Dimensions

### Technical Depth (20% weight)
- Problem-solving approach, architecture reasoning, debugging capability, production experience
- Confidence Threshold: 0.7+

### Authenticity (20% weight)
- Consistency across multiple mentions, specificity, timeline coherence, experience validation
- Confidence Threshold: 0.7+

### English Proficiency (5% weight)
- Response time, vocabulary accuracy, grammar quality, comprehension
- Confidence Threshold: 0.7+

### Behavioral/Cultural Fit (5% weight)
- Ownership mentality, initiative, adaptability, culture alignment
- Confidence Threshold: 0.7+

### Cognitive Flexibility (2% weight)
- Handles ambiguity, adapts approach, considers multiple perspectives
- Confidence Threshold: 0.7+

### Culture-Specific Fit (varies)
- Startup/Leadership/Corporate/Remote/Collaborative alignment
- Confidence Threshold: 0.7+

---

## Confidence Scale

- 1.0 = Crystal clear, undeniable evidence
- 0.9 = Very strong, clear example
- 0.8 = Strong, good example
- 0.7 = Acceptable, supports point
- <0.7 = Do not use (too weak)

---

## Confidence Score Calculation

```
Average confidence = (quote1_confidence + quote2_confidence + quote3_confidence) / 3

Interpretation:
- 0.9+ = Excellent evidence basis
- 0.8-0.89 = Good evidence basis
- 0.7-0.79 = Acceptable evidence basis
- <0.7 = Insufficient evidence
```

---

**Version:** 1.0  
**Last Updated:** 2026-05-12
