# HireSignal Contradiction Detection & Classification Rules

> ⚠️ **Fuente canónica:** `hiresignal-scoring/docs/contradiction-rules.md`
> Este archivo es una copia de referencia para leracom-mcp-builder.
> Si las reglas cambian, actualizar la fuente primaria primero, luego sincronizar aquí.

**Status:** Locked per Step 0 Requirements (2026-05-12)  
**Owner:** Scoring Engine  
**Purpose:** Standardize how contradictions are identified, classified, and acted upon

---

## Overview

Contradictions are statements that conflict with each other within a single interview. Classification determines severity and impact on verdict.

---

## CRITICAL Contradictions (Dealbreaker)

**Definition:** Core contradiction that fundamentally questions candidate reliability or honesty.  
**Impact:** Automatic NOT_FIT verdict (override score)  
**Action:** Disqualify candidate

### Types: Timeline Mismatch, Location/Company Mismatch, Role/Responsibility Mismatch, Skill Dishonesty, Unreachable After 3 Attempts, Interview Abandonment

---

## WARNING Contradictions (Flag & Analyze)

**Definition:** Significant inconsistency that raises questions but doesn't automatically disqualify.  
**Impact:** Affects authenticity score, requires context analysis  
**Action:** Flag for manual review, may require clarification

### Types: Timeline Variance (Minor), Skill Claim vs Reality Discrepancy, Conflicting Project Accounts, Experience Scope Inconsistency

---

## NOTE Contradictions (Document Only)

**Definition:** Minor variation expected in normal human storytelling.  
**Impact:** Noted but not penalized  
**Action:** Document for completeness

---

## Scoring Impact

| Contradiction Count | Type | Impact on Authenticity Score |
|-------------------|------|-----|
| 0 CRITICAL | - | No impact (9-10 range) |
| 1+ CRITICAL | - | DEALBREAKER (NOT_FIT) |
| 0 WARNING | - | 9-10 (highly authentic) |
| 1-2 WARNING | - | 7-8 (consistent, minor issues) |
| 3-5 WARNING | - | 5-6 (multiple concerns) |
| 6+ WARNING | - | 0-4 (pattern of inconsistency) |
| Any NOTE | - | No penalty (normal) |

---

**Version:** 1.0  
**Last Updated:** 2026-05-12
