# HireSignal Contradiction Detection & Classification Rules

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

### Types

#### 1. Timeline Mismatch
**Pattern:** Candidate gives conflicting dates/durations for same experience

**Examples:**
- "I worked at Acme for 5 years" → later "I was there from 2015-2018" (3 years)
- "I joined in Q1 2020" → later "I've been here since 2019"
- "I spent 2 years on the project" → later "it was 6 months"

**Detection:**
- Compare all timeline claims in transcript
- Flag dates that differ by >1 month
- Check employment periods for gaps or overlaps

**Resolution:**
- Quote both conflicting statements
- Ask: Which date is correct?
- If unresolved: CRITICAL contradiction detected

---

#### 2. Location/Company Mismatch
**Pattern:** Candidate claims different company/location for same role

**Examples:**
- "I was at Google in Mountain View" → later "I was at Google in London"
- "I worked at Acme Corp" → later "I was at Acme Inc"
- "I led the SF office" → later "I managed the NYC team"

**Detection:**
- Track all geographic/organizational claims
- Flag changes in location or company name
- Verify if different offices/subsidiaries could explain difference

**Resolution:**
- Quote both statements
- Ask: Where exactly?
- If unresolved: CRITICAL contradiction detected

---

#### 3. Role/Responsibility Mismatch
**Pattern:** Candidate claims different responsibilities for same position

**Examples:**
- "I was the lead architect" → later "I was a junior member of the team"
- "I managed 5 engineers" → later "I was an individual contributor"
- "I owned the payment system" → later "I helped on payment stuff"

**Detection:**
- Map all role descriptions (title, scope, responsibilities)
- Flag significant changes in seniority or scope
- Track accountability claims (I did vs team did)

**Resolution:**
- Quote both statements
- Ask: What were your actual responsibilities?
- If unresolved: CRITICAL contradiction detected

---

#### 4. Skill Dishonesty
**Pattern:** Candidate claims expertise but cannot demonstrate it

**Examples:**
- "I'm an expert in Kubernetes" → cannot explain basic concepts
- "I led database optimization" → cannot discuss index strategy
- "I'm a full-stack developer" → only knows frontend

**Detection:**
- Compare skill claims with technical depth shown
- Look for buzzwords without substance
- Test understanding through follow-up questions

**Resolution:**
- Quote skill claim and evidence gap
- Ask: Can you explain?
- If unresolved: CRITICAL contradiction detected

---

#### 5. Unreachable After 3 Attempts
**Pattern:** Candidate cannot be reached for interview/follow-up

**Examples:**
- No response to 3 separate contact attempts (email, phone, message)
- Misses scheduled interview without notice
- Cannot confirm basic information

**Detection:**
- Log all contact attempts with timestamps
- Automatic trigger after 3 attempts with no response

**Action:**
- CRITICAL dealbreaker
- Disqualify: "Unreachable"

---

#### 6. Interview Abandonment
**Pattern:** Candidate abandons call or interview mid-process

**Examples:**
- Drops call unexpectedly during interview
- Leaves meeting without explanation mid-way
- Stops responding mid-conversation

**Detection:**
- Transcript ends abruptly
- Call duration shorter than expected
- Last message is candidate, no response after

**Action:**
- CRITICAL dealbreaker
- Disqualify: "Interview abandonment"

---

## WARNING Contradictions (Flag & Analyze)

**Definition:** Significant inconsistency that raises questions but doesn't automatically disqualify.  
**Impact:** Affects authenticity score, requires context analysis  
**Action:** Flag for manual review, may require clarification

### Types

#### 1. Timeline Variance (Minor)
**Pattern:** Dates off by <1 month but conflicting

**Examples:**
- "Started in January" → later "Early February"
- "About 2 years" → later "23 months"

**Detection:**
- Differences within 1-month tolerance
- Still contradictory but within human error range

**Action:**
- Flag as WARNING
- Analyze: Could this be natural memory variance?
- Ask for clarification if needed

---

#### 2. Skill Claim vs Reality Discrepancy
**Pattern:** Candidate claims skill but demonstrates different capability level

**Examples:**
- Claims "Senior level" but shows mid-level understanding
- Says "5 years experience" but discusses only recent 2 years
- Mentions advanced techniques but applies basic approaches

**Detection:**
- Score for skill claim (what candidate said)
- Score for demonstrated ability (what they showed)
- Compare: If different, flag as WARNING

**Action:**
- Quote claim and evidence
- Analyze: Overstatement or genuine gap?
- May require clarification

---

#### 3. Conflicting Project Accounts
**Pattern:** Different versions of same project story

**Examples:**
- "I built the system solo" → later "We built it as a team"
- "It was a success" → later "We had issues"
- "I led this" → later "I contributed to this"

**Detection:**
- Track all mentions of same project
- Flag when account changes significantly
- Note if different emphasis or accountability

**Action:**
- Quote both versions
- Analyze: Could both be true? Different perspectives?
- Flag as WARNING if material difference

---

#### 4. Experience Scope Inconsistency
**Pattern:** Candidate changes scope/scale of claimed experience

**Examples:**
- "Managed 100 engineers" → later "Managed a team"
- "Built product used by millions" → later "Internal tool"
- "Led company growth" → later "Contributed to growth"

**Detection:**
- Compare scale claims across interview
- Flag when numbers/scope change significantly

**Action:**
- Quote both claims
- Ask for clarification
- Analyze impact on authenticity score

---

## NOTE Contradictions (Document Only)

**Definition:** Minor variation expected in normal human storytelling.  
**Impact:** Noted but not penalized  
**Action:** Document for completeness

### Types

#### 1. Different Emphasis/Framing
**Example:**
- First mention: "I worked on the payment system"
- Later: "I was part of the payment team"

**Why it's a NOTE:** Same experience, different framing. Normal human communication.

---

#### 2. Normal Memory Inconsistency
**Example:**
- "We launched in March" → later "Spring of that year"

**Why it's a NOTE:** Both statements accurate, just different levels of precision.

---

#### 3. Contextual Variation
**Example:**
- When asked about role: "I was a backend engineer"
- When asked about projects: "I worked on both frontend and backend"

**Why it's a NOTE:** Different question context may elicit different level of detail.

---

## Detection Workflow

```
1. Read entire transcript
   ↓
2. Extract all claims (skills, experience, timeline, scope)
   ↓
3. Compare claims across transcript
   ↓
4. Identify contradictions
   ↓
5. Classify severity:
   - CRITICAL → Dealbreaker → NOT_FIT
   - WARNING → Flag → Affects score
   - NOTE → Document → No penalty
   ↓
6. If CRITICAL detected → Stop, disqualify
   ↓
7. If WARNING → Analyze context, quantify impact
   ↓
8. If NOTE → Document and continue
```

---

## Scoring Impact

### Authenticity Score Based on Contradictions

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

## Example Analysis

**Transcript Excerpt:**

```
Q: Tell me about your experience with distributed systems
A: "I've worked with Kubernetes for about 5 years in production environments"

Q: Where did you gain that experience?
A: "At Google from 2018-2023, managed container orchestration for services"

Q: What specific challenges did you solve?
A: "We had to scale from 10K to 100K containers, implemented auto-scaling"

Q: How long were you at Google?
A: "I joined in late 2017, left in early 2024, so about 6 years"
```

**Contradiction Detected:**

- **Claim 1:** "5 years with Kubernetes" (2018-2023 = 5 years ✓)
- **Claim 2:** "At Google 2018-2023" ✓
- **Claim 3:** "Joined late 2017, left early 2024" (2017-2024 = ~6 years) ⚠️
- **Conflict:** Started working at Google in 2017 or 2018? Timeline shifts by 1 year

**Classification:** WARNING (not CRITICAL because still ~5-6 years, difference is 1 year)

**Authenticity Impact:**
- Exact start date matters for verification
- Could indicate hazy memory or intentional imprecision
- Ask for clarification before finalizing score

**Action:** Classify as WARNING, flag for review, may ask "When exactly did you start at Google?"

---

## Implementation Notes

- All contradictions must be quoted directly from transcript
- Use timestamps if available
- Always include context (question asked)
- Confidence score based on clarity of contradiction (0.7-1.0 = clear)
- Manual review required for all CRITICAL contradictions
- Scoring engine flags contradictions; human reviewer confirms severity

---

**Version:** 1.0  
**Last Updated:** 2026-05-12  
**Next Review:** After first 50 candidate scores
