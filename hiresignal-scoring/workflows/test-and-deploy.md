# Workflow: Test and Deploy

**Goal:** Validate scoring engine accuracy and deploy to production.

**Duration:** 3-5 days  
**Owner:** Backend engineer + QA  
**Output:** Production-ready scoring engine with monitoring

---

## Step 0: Preparation

**Read first:**
- `workflows/implement-tech-option.md` — Current implementation
- `HIRESIGNAL_SCORING_ENGINE_SPEC.md` — Success criteria

---

## Step 1: Unit Testing

**Task:** Test individual scoring dimensions

```typescript
// src/__tests__/scoring.test.ts
import { scoreTranscript } from "../scoring";

describe("Scoring Engine", () => {
  it("detects technical depth from architecture discussion", async () => {
    const transcript = `
      Interviewer: How would you design a payment system?
      Candidate: I'd use a message queue to decouple...
    `;
    
    const result = await scoreTranscript(transcript, {});
    expect(result.technical_depth.score).toBeGreaterThanOrEqual(7);
  });

  it("flags contradictions with correct severity", async () => {
    const transcript = `
      Interviewer: How long did you work there?
      Candidate: 2 years...
      Interviewer: Tell me about a project from year 3?
      Candidate: ...
    `;
    
    const result = await scoreTranscript(transcript, {});
    expect(result.authenticity.contradictions[0].severity).toBe("CRITICAL");
  });

  it("passes English assessment for native speaker", async () => {
    // Transcript from native English speaker
    const result = await scoreTranscript(nativeTranscript, {});
    expect(result.english.score).toBeGreaterThanOrEqual(8);
    expect(result.english.passes_minimum).toBe(true);
  });
});
```

**Run tests:**
```bash
npm test
```

---

## Step 2: Integration Testing

**Task:** Test full pipeline (transcript → verdict → report)

```typescript
// src/__tests__/integration.test.ts
describe("End-to-end Scoring", () => {
  it("produces complete report from transcript", async () => {
    const transcript = readFile("fixtures/sample-interview.txt");
    
    const response = await fetch("http://localhost:3000/score/transcript", {
      method: "POST",
      body: JSON.stringify({
        transcript,
        role: "Senior Engineer",
        culture: "startup"
      })
    });

    const result = await response.json();
    
    expect(result.overall_score).toBeDefined();
    expect(result.verdict).toMatch(/FIT|NOT_FIT/);
    expect(result.report_url).toBeDefined();
    
    // Verify report can be fetched
    const report = await fetch(result.report_url);
    expect(report.status).toBe(200);
  });
});
```

---

## Step 3: Accuracy Testing

**Task:** Validate scoring against known results

**Test dataset:**
Create 10-20 sample transcripts with pre-agreed verdicts from recruiters.

```typescript
// src/__tests__/accuracy.test.ts
const testCases = [
  {
    name: "High performer - should be FIT",
    transcript: readFile("fixtures/high-performer.txt"),
    expected_verdict: "FIT",
    expected_score_min: 7,
  },
  {
    name: "Contradictory candidate - should flag CRITICAL",
    transcript: readFile("fixtures/contradictory.txt"),
    expected_critical_count: 1,
  },
  // ... more test cases
];

for (const testCase of testCases) {
  it(testCase.name, async () => {
    const result = await scoreTranscript(testCase.transcript, {});
    expect(result.verdict).toBe(testCase.expected_verdict);
    if (testCase.expected_score_min) {
      expect(result.overall_score).toBeGreaterThanOrEqual(testCase.expected_score_min);
    }
  });
}
```

**Target:** 95%+ accuracy on test set

---

## Step 4: Performance Testing

**Task:** Verify latency and cost

**Latency targets:**
- Scoring API: < 5 seconds per transcript
- Report generation: < 2 seconds

```bash
# Load test with 10 concurrent requests
artillery quick --count 10 --num 100 http://localhost:3000/score/transcript

# Expected: p99 latency < 5s
```

**Cost tracking (Option B - Claude API):**
- Each transcript call: ~$0.40
- Expected volume: 1000/month = $400
- Monitor and optimize if needed

---

## Step 5: Recruiter Acceptance Testing

**Task:** Get feedback from 5-10 recruiters

**Test protocol:**
1. Have recruiters interview candidates (normal process)
2. Run transcript through scoring engine
3. Collect feedback:
   - Is verdict accurate?
   - Is evidence helpful?
   - Are contradictions detected correctly?
   - Is report useful for decision-making?

**Feedback template:**
```
Candidate: [name]
Verdict: FIT / NOT_FIT / UNSURE
Score accuracy: 1-5 (1=completely wrong, 5=perfect)
Evidence quality: 1-5 (1=not useful, 5=very helpful)
Contradictions caught: Yes/No
Would use this report: Yes/No
Comments: ...
```

**Target:** 4+ average score, "would use" from 80%+

---

## Step 6: Fix Accuracy Issues

**Task:** Iterate based on feedback

**Common issues:**

**Issue 1: Scoring too high (false positives)**
- Symptom: Candidates flagged as FIT shouldn't be
- Fix: Adjust Claude prompt to be more critical
- Re-test with cases that failed

**Issue 2: Missing contradictions**
- Symptom: Contradictions not detected
- Fix: Add more specific prompting to Claude
- Example: "Look for timeline inconsistencies, skill claims vs actual experience"

**Issue 3: Poor evidence extraction**
- Symptom: Quotes don't match the score
- Fix: Improve prompt to be more specific about evidence
- Provide examples of good vs bad evidence

**Iteration process:**
1. Identify failures in recruiter feedback
2. Update Claude prompts or scoring logic
3. Re-test on full test set (target: 95%+)
4. Re-test with recruiters (sample of failed cases)
5. Deploy updated version

---

## Step 7: Setup Monitoring

**Task:** Track metrics in production

**Metrics to monitor:**

```typescript
// src/monitoring.ts
import { metrics } from "./lib/metrics";

// Log every scoring
app.post("/score/transcript", async (req, res) => {
  const start = Date.now();
  
  try {
    const result = await scoreTranscript(...);
    
    metrics.timing("score.latency", Date.now() - start);
    metrics.increment("score.success");
    metrics.gauge("score.overall", result.overall_score);
    
    res.json(result);
  } catch (err) {
    metrics.increment("score.error");
    res.status(500).json({ error: err.message });
  }
});

// Dashboard queries:
// - Daily scoring volume
// - Average latency
// - Error rate
// - Score distribution (% FIT vs NOT_FIT)
// - API cost
```

**Dashboard setup:**
- CloudWatch (AWS) or Datadog
- Key metrics: latency p99, error rate, daily volume
- Alerts: error rate > 5%, latency > 10 sec

---

## Step 8: Documentation & Training

**Task:** Document for recruiters and operations

**Deliverables:**

1. **API Documentation** (`docs/api-reference.md`)
   - POST /score/transcript
   - GET /report/{id}
   - Parameters, response format, error codes

2. **Recruiter Guide** (`docs/recruiter-guide.md`)
   - How to use scoring engine
   - How to interpret reports
   - How to provide feedback
   - Troubleshooting

3. **Operations Guide** (`docs/operations-guide.md`)
   - Monitoring & alerts
   - How to scale
   - Common issues & fixes
   - Cost optimization

4. **Maintenance Guide** (`docs/maintenance-guide.md`)
   - How to update scoring logic
   - How to retrain/improve accuracy
   - Monthly review process

---

## Step 9: Staging Deployment

**Task:** Deploy to staging environment before production

```bash
# Build & deploy to staging
npm run build
npm run deploy --environment=staging

# Test against staging
curl http://staging-scoring.example.com/score/transcript \
  -H "Content-Type: application/json" \
  -d '{...}'

# Run full test suite against staging
npm run test:integration --environment=staging
```

**Validation:**
- [ ] All endpoints working
- [ ] Report generation working
- [ ] Monitoring collecting data
- [ ] Database syncing correctly

---

## Step 10: Production Deployment

**Task:** Go live with scoring engine

```bash
# Deploy to production
npm run deploy --environment=production

# Health check
curl http://scoring.example.com/health

# Monitor metrics
# - Watch latency p99 (target: <5s)
# - Watch error rate (target: <1%)
# - Watch cost (target: $400-500/month for MVP volume)
```

**Rollback plan:**
If production issues:
```bash
# Rollback to previous version
npm run deploy --environment=production --version=v1.0.0
```

---

## Step 11: Post-Launch Monitoring

**Task:** Track accuracy and iterate for 2 weeks

**Daily checklist:**
- [ ] Error rate < 1%
- [ ] Latency p99 < 5 sec
- [ ] API cost within budget
- [ ] No escalations from recruiters

**Weekly review:**
- Gather recruiter feedback
- Identify 2-3 improvements
- Plan fixes for next week

**2-week evaluation:**
- Accuracy: 95%+?
- Recruiter satisfaction: 80%+?
- Production ready?
- If yes → move to next phase (Priority 2)

---

## Output

**Deliverables:**
1. ✅ Production-ready scoring engine
2. ✅ Monitoring & alerting
3. ✅ Documentation & training
4. ✅ Recruiter feedback process
5. ✅ Continuous improvement plan

**Success criteria:**
- ✅ 95%+ accuracy on test set
- ✅ 95%+ accuracy in production (recruiter validation)
- ✅ < 5 sec latency p99
- ✅ < 1% error rate
- ✅ 80%+ recruiter satisfaction
- ✅ Cost within budget

**Next phase:** Priority 2 - Dynamic configuration (connect JD → interview params)

---

## Reference

- Full spec: `HIRESIGNAL_SCORING_ENGINE_SPEC.md`
- Tech options: `HIRESIGNAL_SCORING_TECH_OPTIONS.md`
- Monitoring: `docs/monitoring-setup.md`
