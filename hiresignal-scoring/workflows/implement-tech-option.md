# Workflow: Implement Tech Option

**Goal:** Choose and implement the scoring engine using one of three tech options.

**Duration:** 1-2 weeks  
**Owner:** Backend engineer  
**Output:** Working MVP (API endpoints + report generation)

---

## Step 0: Choose Your Tech Stack

**Read first:**
- `docs/tech-options.md` — Compare all 3 options
- `HIRESIGNAL_SCORING_TECH_OPTIONS.md` — Detailed comparison

**Decision matrix:**

| Option | Build Time | Day-1 Accuracy | Cost/Transcript | Recommendation |
|--------|-----------|-----------------|-----------------|-----------------|
| A: Pure Python | 50 hours | 70% | $0 | Long-term |
| B: Claude API | 25 hours | 90% | $0.40 | **RECOMMENDED MVP** |
| C: Hybrid | 60 hours | 85% | $0.10 | Future optimization |

**Recommendation:** Start with **Option B (Claude API)** for fastest MVP.

---

## Step 1: Setup Development Environment

**Task:** Create project structure and dependencies

### Option B: Claude API (Recommended)

```bash
# Create project
mkdir hiresignal-scoring
cd hiresignal-scoring
npm init -y

# Install dependencies
npm install express axios dotenv
npm install --save-dev typescript ts-node @types/express @types/node

# Create structure
mkdir src
touch src/index.ts
touch .env
```

**Environment variables (.env):**
```
CLAUDE_API_KEY=sk_...
LERACOM_API_KEY=...
NODE_ENV=development
PORT=3000
```

---

## Step 2: Implement Core Endpoints

**Task:** Build the API that Claude will call

### Endpoint 1: POST /score/transcript

```typescript
// src/index.ts
import express from "express";
import Anthropic from "@anthropic-sdk/sdk";

const app = express();
const client = new Anthropic({
  apiKey: process.env.CLAUDE_API_KEY,
});

app.post("/score/transcript", async (req, res) => {
  const { transcript, role, culture, jd_context } = req.body;

  // Call Claude to analyze transcript
  const message = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 4096,
    messages: [{
      role: "user",
      content: `Analyze this interview transcript for a ${role} role in a ${culture} culture.

Transcript:
${transcript}

${jd_context ? `Job Context: ${jd_context}` : ""}

Return ONLY valid JSON (no markdown, no explanation):
{
  "technical_depth": {
    "score": 0-10,
    "evidence": ["quote1", "quote2"],
    "reasoning": "..."
  },
  "authenticity": {
    "score": 0-10,
    "contradictions": [{"severity": "CRITICAL|WARNING|NOTE", "issue": "...", "evidence": "..."}],
    "reasoning": "..."
  },
  "english": {
    "score": 0-10,
    "passes_minimum": true,
    "reasoning": "..."
  },
  "behavioral": {
    "score": 0-10,
    "reasoning": "..."
  },
  "verdict": "FIT|NOT_FIT",
  "overall_score": 0-10,
  "reasoning": "..."
}`
    }]
  });

  // Parse Claude response
  const result = JSON.parse(
    message.content[0].type === "text" ? message.content[0].text : "{}"
  );

  // Save to database
  // Generate report
  
  res.json({
    scoring_id: generateId(),
    ...result,
    report_url: `/report/${generateId()}.html`
  });
});

app.listen(3000, () => {
  console.log("Scoring engine running on port 3000");
});
```

### Endpoint 2: GET /report/{id}

```typescript
app.get("/report/:id", async (req, res) => {
  // Fetch scoring from DB
  // Generate HTML report
  // Return or stream PDF
  
  const html = `
    <html>
      <head><title>Interview Report</title></head>
      <body>
        <h1>${result.verdict}</h1>
        <p>Score: ${result.overall_score}/10</p>
        <div class="evidence">
          ${Object.entries(result).map(([dim, data]) => `
            <section>
              <h3>${dim}: ${data.score}/10</h3>
              <p>${data.reasoning}</p>
              <blockquote>${data.evidence[0]}</blockquote>
            </section>
          `).join("")}
        </div>
      </body>
    </html>
  `;
  
  res.setHeader("Content-Type", "text/html");
  res.send(html);
});
```

---

## Step 3: Handle Contradictions

**Task:** Implement contradiction detection and classification

```typescript
const analyzeContradictions = async (transcript: string) => {
  const message = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 2000,
    messages: [{
      role: "user",
      content: `Find all contradictions in this interview transcript.

Transcript:
${transcript}

Return JSON:
{
  "contradictions": [
    {
      "severity": "CRITICAL|WARNING|NOTE",
      "issue": "...",
      "evidence_1": "quote from first mention",
      "evidence_2": "quote from contradiction",
      "context": "..."
    }
  ]
}`
    }]
  });

  return JSON.parse(message.content[0].type === "text" ? message.content[0].text : "{}");
};
```

---

## Step 4: Generate Report

**Task:** Convert scores + contradictions into HTML/PDF

```typescript
const generateReport = (scores: any) => {
  const template = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Interview Assessment</title>
        <style>
          body { font-family: system-ui; margin: 40px; }
          .verdict { font-size: 32px; font-weight: bold; }
          .fit { color: green; }
          .not-fit { color: red; }
          .score-card { border: 1px solid #ccc; padding: 20px; margin: 10px 0; }
          .evidence { background: #f5f5f5; padding: 10px; margin: 5px 0; }
          .contradiction { border-left: 3px solid orange; padding: 10px; }
        </style>
      </head>
      <body>
        <h1 class="verdict ${scores.verdict.toLowerCase()}">
          ${scores.verdict}
        </h1>
        <p>Score: ${scores.overall_score}/10 (Confidence: ${scores.confidence}%)</p>
        <p>${scores.reasoning}</p>

        <h2>Detailed Scores</h2>
        ${Object.entries(scores.scores).map(([dim, data]: any) => `
          <div class="score-card">
            <h3>${dim}: ${data.score}/10</h3>
            <p>${data.reasoning}</p>
            ${data.evidence?.map((q: string) => `
              <div class="evidence">
                <blockquote>"${q}"</blockquote>
              </div>
            `).join("") || ""}
          </div>
        `).join("")}

        <h2>Contradictions</h2>
        ${scores.contradictions_summary.critical > 0 ? `
          <p style="color: red;">⚠️ ${scores.contradictions_summary.critical} CRITICAL contradictions detected</p>
        ` : ""}
        ${scores.contradictions_summary.warning > 0 ? `
          <p style="color: orange;">⚠️ ${scores.contradictions_summary.warning} warnings</p>
        ` : ""}

        <h2>Next Steps</h2>
        <ul>
          ${scores.next_steps.map((step: string) => `<li>${step}</li>`).join("")}
        </ul>
      </body>
    </html>
  `;

  return template;
};
```

---

## Step 5: Test with Sample Transcripts

**Task:** Verify scoring accuracy before deployment

**Test cases:**
- [ ] High performer (technical + authentic) → should score 8+
- [ ] Contradictory candidate (authentic score 4-5) → should flag warnings
- [ ] Weak technical → should score 3-5
- [ ] CRITICAL contradiction → should override to NOT_FIT

**Test transcript:**
Use a real interview transcript or create synthetic ones.

```bash
# Test endpoint
curl -X POST http://localhost:3000/score/transcript \
  -H "Content-Type: application/json" \
  -d '{"transcript": "...", "role": "Senior Engineer", "culture": "startup"}'
```

---

## Step 6: Deploy to Production

**Task:** Make scoring engine available to recruiters

**Options:**

**Option 1: AWS Lambda**
```bash
# Package function
npm run build
zip -r function.zip dist node_modules

# Deploy
aws lambda create-function --runtime nodejs18.x --handler index.handler ...
```

**Option 2: Docker + ECS**
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY src ./src
RUN npm run build
CMD ["node", "dist/index.js"]
```

**Option 3: Vercel (Easiest)**
```bash
vercel deploy
```

---

## Step 7: Monitor & Iterate

**Task:** Track scoring accuracy and adjust logic

**Metrics to track:**
- Scoring consistency (95%+ target)
- Recruiter feedback accuracy
- API latency (<5 sec target)
- Cost per transcript (track usage)

**Feedback loop:**
- Week 1: Collect recruiter feedback on 10 scorings
- Week 2: Adjust scoring logic based on feedback
- Deploy updated version
- Repeat

---

## Output

**Deliverables:**
1. **API server** — Deployed and accessible
2. **Scoring service** — Working with Claude
3. **Report generator** — HTML/PDF working
4. **Test results** — 95%+ consistency verified
5. **Monitoring dashboard** — Track metrics

**Next step:** → `workflows/test-and-deploy.md`

---

## Reference

- Code template: `docs/code-template-option-b.ts`
- Full spec: `HIRESIGNAL_SCORING_ENGINE_SPEC.md`
- Tech options: `HIRESIGNAL_SCORING_TECH_OPTIONS.md`
