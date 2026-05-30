# HireSignal Scoring — Quick Reference

## Scoring Dimensions

```
Technical Depth (20%)     → Architecture, debugging, production
Authenticity (20%)        → Consistency, specificity, AI detection
English Proficiency (5%)  → Response time, vocabulary, grammar
Behavioral/Cultural (5%)  → Ownership, initiative, fit
Other (50%)              → Cognitive flexibility, pressure resilience
```

## Verdict Logic

```
Score = (technical × 0.20) + (authentic × 0.20) + (english × 0.05) + 
        (behavioral × 0.05) + (other × 0.50)

FIT if: score ≥ 6.5 AND no CRITICAL contradictions
NOT_FIT if: score < 6.5 OR CRITICAL contradiction exists
```

## Contradiction Severity

| Level | When to Use | Impact |
|-------|-----------|--------|
| CRITICAL | Core contradiction (timeline, role mismatch) | Overrides to NOT_FIT |
| WARNING | Significant inconsistency (skill claim vs reality) | Flags, analyze context |
| NOTE | Minor variation (normal human inconsistency) | Document only |

## API Quick Start

```bash
# Score a transcript
curl -X POST http://localhost:3000/score/transcript \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "...",
    "role": "Senior Engineer",
    "culture": "startup"
  }'

# Get report
curl http://localhost:3000/report/abc123

# Health check
curl http://localhost:3000/health
```

## Key Files

- **HIRESIGNAL_SCORING_ENGINE_SPEC.md** → Full technical spec
- **HIRESIGNAL_SCORING_TECH_OPTIONS.md** → Tech decision
- **workflows/design-scoring-engine.md** → Define dimensions
- **workflows/implement-tech-option.md** → Build MVP
- **workflows/test-and-deploy.md** → QA & launch

## Timeline

- **Week 1:** Design dimensions + implement core API
- **Week 2:** Testing + recruiter feedback + production deploy
- **After:** Monitor, iterate, add P2 (dynamic config)

## Common Questions

**Q: How long does scoring take?**
A: 3-5 seconds per transcript (Claude API latency)

**Q: What does it cost?**
A: ~$0.40 per transcript via Claude API (Option B)

**Q: Can I change the scoring logic?**
A: Yes - adjust Claude prompts in `src/scoring.ts`

**Q: How accurate is it?**
A: Target 95%+ accuracy on test set, validated with recruiters
