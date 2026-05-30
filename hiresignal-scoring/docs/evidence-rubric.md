# HireSignal Evidence Extraction Rubric

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

**Confidence Scale:**
- 1.0 = Crystal clear, undeniable evidence
- 0.9 = Very strong, clear example
- 0.8 = Strong, good example
- 0.7 = Acceptable, supports point
- <0.7 = Do not use (too weak)

---

## Dimension 1: Technical Depth (20% weight)

**What to Extract:**
- Problem-solving approach (surface vs deep thinking)
- Architecture reasoning (understands tradeoffs)
- Debugging capability (root cause analysis)
- Production experience (handles edge cases, failure scenarios)
- Anti-buzzword behavior (demonstrates real knowledge)

**Quote Requirements:** 3 quotes minimum  
**Confidence Threshold:** 0.7+

### Evidence Quality Matrix

| Quality Level | Confidence | Example | Use? |
|--------------|-----------|---------|------|
| **Excellent** | 0.95+ | Candidate explains complete architecture with tradeoffs | ✅ Use |
| **Good** | 0.8-0.94 | Candidate discusses debugging strategy with reasoning | ✅ Use |
| **Acceptable** | 0.7-0.79 | Candidate mentions relevant technical experience | ✅ Use |
| **Weak** | <0.7 | Candidate uses buzzword without explanation | ❌ Skip |

### Example Evidence Extraction

**Dimension Score:** 8/10

**Quote 1 (Confidence: 0.95)**
```json
{
  "quote": "I'd use a message queue to decouple the services because we needed asynchronous processing without tight coupling",
  "context": "Architecture design question about system scalability",
  "confidence": 0.95,
  "reasoning": "Shows understanding of both technical solution AND WHY (decoupling, async) - demonstrates depth beyond buzzword"
}
```

**Quote 2 (Confidence: 0.88)**
```json
{
  "quote": "When we hit the memory leak in production, I traced it to the event listener not being cleared in the cleanup. Took us 3 days to isolate but once we identified the pattern, the fix was straightforward",
  "context": "Production debugging experience",
  "confidence": 0.88,
  "reasoning": "Shows root cause analysis (not just symptom fixing), production pressure handling, systematic troubleshooting"
}
```

**Quote 3 (Confidence: 0.82)**
```json
{
  "quote": "We handle 100K concurrent connections by using connection pooling and implementing circuit breakers to prevent cascade failures",
  "context": "High-scale production experience",
  "confidence": 0.82,
  "reasoning": "Demonstrates understanding of production resilience patterns, real-world constraints"
}
```

---

## Dimension 2: Authenticity (20% weight)

**What to Extract:**
- Consistency across multiple mentions of same experience
- Specificity (details vs generalizations)
- Timeline coherence (dates make sense)
- Experience validation (claims match demonstrated knowledge)
- AI usage detection (natural vs coached responses)

**Quote Requirements:** 3 quotes minimum (can include contradictions)  
**Confidence Threshold:** 0.7+

### Evidence Quality Matrix

| Quality Level | Confidence | Example | Use? |
|--------------|-----------|---------|------|
| **Excellent** | 0.95+ | Same story told 2+ ways with consistent details | ✅ Use |
| **Good** | 0.8-0.94 | Specific date/timeline claim that's verifiable | ✅ Use |
| **Acceptable** | 0.7-0.79 | General experience claim with some specificity | ✅ Use |
| **Weak** | <0.7 | Vague statement or AI-detected pattern | ❌ Skip |

### Example Evidence Extraction

**Dimension Score:** 7/10 (one minor contradiction flagged)

**Quote 1 (Consistency) - Confidence: 0.92**
```json
{
  "quote": "I led the migration from MySQL to PostgreSQL at Acme. Started in Q3 2021, took about 4 months, handled 500GB database with zero downtime",
  "context": "Project leadership experience",
  "confidence": 0.92,
  "reasoning": "Specific timeline, quantified scope, clear ownership - testable claims"
}
```

**Quote 2 (Consistency - Same Project) - Confidence: 0.89**
```json
{
  "quote": "The PostgreSQL migration was challenging because we had to maintain backward compatibility during the transition. We ended up using dual-write pattern",
  "context": "Technical challenges in past projects",
  "confidence": 0.89,
  "reasoning": "Same project mentioned earlier, adds technical detail, consistent timeline. Shows real problem-solving."
}
```

**Quote 3 (Minor Contradiction) - Confidence: 0.78**
```json
{
  "quote": "We had about 100 engineers, but maybe it was closer to 80. It was a big team",
  "context": "Team size at previous company",
  "confidence": 0.78,
  "reasoning": "Vague/correcting on team size. Not dealbreaker (WARNING level) but suggests less precise memory or intentional vagueness"
}
```

**Contradiction Noted:** 100 vs 80 engineers = WARNING (±20% variance on team size)

---

## Dimension 3: English Proficiency (5% weight)

**What to Extract:**
- Response time (quick vs slow understanding)
- Vocabulary accuracy (correct term usage)
- Grammar quality (native-like vs ESL patterns)
- Comprehension (understands complex questions)
- Complex idea expression (can articulate nuance)

**Quote Requirements:** 3 quotes minimum (from different exchanges)  
**Confidence Threshold:** 0.7+

**Note:** This is both qualitative AND can be scored more objectively based on:
- Response latency in call transcript
- Grammar/syntax accuracy
- Vocabulary sophistication

### Evidence Quality Matrix

| Quality Level | Confidence | Example | Use? |
|--------------|-----------|---------|------|
| **Native-like** | 0.95+ | Complex ideas expressed clearly, immediate comprehension | ✅ Use |
| **Fluent** | 0.85-0.94 | Minor accent/hesitation but clear communication | ✅ Use |
| **Intermediate** | 0.75-0.84 | Understands most questions, occasional comprehension delay | ✅ Use |
| **Struggling** | <0.75 | Frequent misunderstandings or communication delays | ❌ Skip |

### Example Evidence Extraction

**Dimension Score:** 8/10

**Quote 1 (Vocabulary) - Confidence: 0.93**
```json
{
  "quote": "I implemented polymorphic behavior using interface segregation to reduce coupling between components",
  "context": "Technical design discussion",
  "confidence": 0.93,
  "reasoning": "Correct terminology, sophisticated vocabulary, accurate use of technical English"
}
```

**Quote 2 (Comprehension) - Confidence: 0.88**
```json
{
  "quote": "When you mention edge cases, you're talking about boundary conditions that might break the system, right? I've dealt with that in the caching layer",
  "context": "Complex concept probing",
  "confidence": 0.88,
  "reasoning": "Shows comprehension of nuanced concept, immediately translates to own experience"
}
```

**Quote 3 (Grammar/Expression) - Confidence: 0.85**
```json
{
  "quote": "The database performance was impacted because we didn't anticipate the query complexity would increase as data volume grew. If we had indexed properly from the start, we would have avoided the issue",
  "context": "Lessons learned discussion",
  "confidence": 0.85,
  "reasoning": "Complex sentence structure, correct use of conditional past, sophisticated expression"
}
```

---

## Dimension 4: Behavioral/Cultural Fit (5% weight)

**What to Extract:**
- Ownership mentality (I did vs team did)
- Initiative (proactivity vs reactivity)
- Adaptability (changes approach when needed)
- Culture alignment (depends on JD's culture_factor)

**Quote Requirements:** 3 quotes minimum (ideally from behavioral questions)  
**Confidence Threshold:** 0.7+

### Evidence Quality Matrix

| Quality Level | Confidence | Example | Use? |
|--------------|-----------|---------|------|
| **Excellent** | 0.95+ | Clear ownership, initiative, cultural alignment | ✅ Use |
| **Good** | 0.8-0.94 | Shows some ownership/initiative | ✅ Use |
| **Acceptable** | 0.7-0.79 | Mentions relevant behavior but less strong | ✅ Use |
| **Weak** | <0.7 | Passive language, avoids accountability | ❌ Skip |

### Example Evidence Extraction (Startup Culture)

**Dimension Score:** 7/10

**Quote 1 (Ownership) - Confidence: 0.92**
```json
{
  "quote": "When the critical service went down, I didn't wait for approval. I diagnosed the issue, deployed a fix, and got it back up in 2 hours. Then I wrote a post-mortem",
  "context": "Handling incident autonomously",
  "confidence": 0.92,
  "reasoning": "Uses 'I' language, shows initiative, bias for action without waiting for approval - strong startup signal"
}
```

**Quote 2 (Initiative) - Confidence: 0.87**
```json
{
  "quote": "I noticed we were wasting time in our deployment process, so I automated it and cut deployment time by 50%. Wasn't assigned to me, but it seemed like low-hanging fruit",
  "context": "Self-directed improvement",
  "confidence": 0.87,
  "reasoning": "Shows proactivity, sees problems and fixes them, doesn't wait for direction"
}
```

**Quote 3 (Culture Alignment) - Confidence: 0.80**
```json
{
  "quote": "I like the startup environment because you get to wear multiple hats and things move fast. I'm comfortable with ambiguity",
  "context": "Culture preference question",
  "confidence": 0.80,
  "reasoning": "Explicit comfort with startup constraints, mentions relevant preferences"
}
```

---

## Dimension 5: Cognitive Flexibility (2% weight)

**What to Extract:**
- Handles ambiguous questions (doesn't need perfect clarity)
- Adapts approach (changes strategy when challenged)
- Considers multiple perspectives (not stuck in one view)
- Recovers from mistakes (handles being wrong gracefully)

**Quote Requirements:** 3 quotes minimum  
**Confidence Threshold:** 0.7+

### Example Evidence Extraction

**Dimension Score:** 7/10

**Quote 1 (Handles Ambiguity) - Confidence: 0.85**
```json
{
  "quote": "With an ambiguous requirement, I'd first ask clarifying questions to understand the core need. If I still couldn't get clarity, I'd implement the most common use case first and build from there",
  "context": "How you handle unclear specifications",
  "confidence": 0.85,
  "reasoning": "Shows comfort with ambiguity, has structured approach to handle it"
}
```

**Quote 2 (Adapts Approach) - Confidence: 0.88**
```json
{
  "quote": "I initially thought the bottleneck was the database, but when you pointed out the logging overhead, I pivoted to profiling that instead and found the real issue",
  "context": "Technical discussion where being corrected",
  "confidence": 0.88,
  "reasoning": "Shows willingness to change approach based on new information"
}
```

**Quote 3 (Recovers from Mistakes) - Confidence: 0.82**
```json
{
  "quote": "I realized mid-meeting my assumption was wrong. Instead of defending it, I said 'let me reconsider' and we found a better solution together",
  "context": "Handling being wrong",
  "confidence": 0.82,
  "reasoning": "Graceful handling of error, collaborative problem-solving"
}
```

---

## Confidence Score Calculation

```
For each dimension:
  Average confidence = (quote1_confidence + quote2_confidence + quote3_confidence) / 3
  
Example:
  Quotes: 0.95, 0.88, 0.82
  Average: (0.95 + 0.88 + 0.82) / 3 = 0.88
```

**Interpretation:**
- 0.9+ = Excellent evidence basis
- 0.8-0.89 = Good evidence basis
- 0.7-0.79 = Acceptable evidence basis
- <0.7 = Insufficient evidence, use different quotes

---

## Quote Selection Best Practices

1. **Use direct quotes** — Copy verbatim from transcript, don't paraphrase
2. **Include timestamps** — If available, note where in interview
3. **Provide context** — What question prompted the response?
4. **Be specific** — "Architecture reasoning" not just "technical"
5. **Mix evidence types** — Don't use 3 quotes all about same topic
6. **Avoid cherry-picking** — If negative evidence exists, include it too

---

## Red Flags in Evidence Extraction

| Red Flag | What It Means | Action |
|----------|---------------|--------|
| Can't find 3 strong quotes | Candidate weak in dimension | Score lower, note in evidence |
| Quotes sound coached | Possible AI-generated answers | Flag for authenticity review |
| Quotes contradict each other | Consistency issue | Note as WARNING contradiction |
| All quotes from same topic | Narrow evidence base | Seek evidence from different areas |
| Had to lower confidence threshold | Weak evidence overall | Score lower on dimension |

---

**Version:** 1.0  
**Last Updated:** 2026-05-12  
**Next Review:** After first 50 candidate scores
