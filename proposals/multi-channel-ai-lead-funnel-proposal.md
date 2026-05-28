# Multi-Channel AI Lead Funnel System
## Investor & Stakeholder Proposal

**Prepared:** May 2026
**Version:** 1.0

---

## Executive Summary

We propose building an AI-powered lead capture and response system that meets customers exactly where they are — on any platform they use — and automatically responds through that same channel to qualify them and move them toward a purchase.

The system is built on top of our existing **Hiresignal AI conversation engine**, significantly reducing development time and cost. It captures leads triggered by social media ads, SMS campaigns, email, WhatsApp, Instagram, Facebook, and Telegram, then uses AI to qualify each lead and guide them toward the right product or service. If a lead goes quiet, a smart follow-up engine keeps the conversation alive — persistently but respectfully — until a sale or a deliberate cooling period.

**Total investment to full deployment: $12,500 – $15,000 (one-time build)**
**Monthly operating cost: $500 – $800/month (scales with volume)**
**Time to full deployment: 8 weeks**

---

## The Problem We're Solving

Leads are expensive to acquire. Most businesses lose them due to three avoidable failures:

1. **Wrong channel friction** — The lead came in on Instagram but gets an email response 24 hours later. Conversion drops dramatically.
2. **No follow-up system** — A lead that doesn't respond on Day 1 is forgotten.
3. **Manual qualification** — Sales teams spend time on leads that were never going to convert, missing the ones that would.

This system solves all three.

---

## How It Works

### Step 1 — Lead Enters Through Any Door

A potential customer sees one of our ads and clicks **"Contact Us."** That click opens a conversation on whatever platform is most natural for them:

- Clicks on a Facebook/Instagram ad → opens **WhatsApp** or **Facebook Messenger**
- Sees a text campaign → replies via **SMS**
- Clicks on an email → replies via **email**
- Finds us on Telegram → messages our **Telegram bot**

The moment they send that first message, the system knows exactly which channel they came from and which ad triggered their interest.

### Step 2 — AI Qualifies the Lead Immediately

Our AI (powered by Claude, the same engine behind Hiresignal) responds within seconds — on the same channel. It has one goal: understand what the customer needs and whether we can help them.

The AI conversation is friendly, human-feeling, and structured. It gathers:
- What product or service they're interested in
- Their timeline and urgency
- Whether they're the decision-maker
- Budget signals

This is the same technology we already use in Hiresignal's AI interviewer — repurposed for sales instead of candidate interviews. The conversation engine, the turn management, the Claude API integration: all already built and proven.

### Step 3 — Lead Is Scored and Stored

Every lead lands in a central database — regardless of which channel they came from. Each lead is:
- Tagged with their source channel and which ad campaign triggered them
- Given a qualification score based on the AI conversation
- Assigned to the right product or service category
- Tracked across every interaction in their full history

This is the single source of truth for all leads across all channels.

### Step 4 — Follow-Up Engine Keeps Leads Warm

Not every lead responds the first time. The system handles this with a smart, friendly follow-up cadence:

| Days Since Last Contact | Action |
|---|---|
| Day 1 | Friendly check-in: *"Hey, just wanted to make sure you got my message!"* |
| Day 4 | Soft reminder: *"I wanted to circle back — no pressure at all..."* |
| Day 9 | Value-add touch: *"Thought this might be useful for you..."* |
| Day 16 | Final attempt: *"Leaving this here in case the timing wasn't right..."* |
| After 4 attempts with no response | **Cooling period begins (30 days)** |
| After cooling period | Lead re-enters funnel automatically with a fresh angle |

**The lead is never deleted.** "No response" means "not yet" — not "never." The system keeps every lead in the pipeline, dormant but ready, until circumstances change.

### Step 5 — Qualified Leads Are Converted

Leads that engage with the AI and qualify are:
- Flagged as ready for human follow-up or direct sale
- Optionally handed off to a sales team member at the right moment
- Tracked to conversion so we can measure ROI per channel and per campaign

---

## Supported Channels

| Channel | Capture | AI Response | Follow-Up | Ad-Triggered |
|---|:---:|:---:|:---:|:---:|
| SMS | ✓ | ✓ | ✓ | ✓ |
| Email | ✓ | ✓ | ✓ | ✓ |
| WhatsApp | ✓ | ✓ | ✓ | ✓ |
| Instagram DM | ✓ | ✓ | ✓ | ✓ |
| Facebook Messenger | ✓ | ✓ | ✓ | ✓ |
| Telegram | ✓ | ✓ | ✓ | ✓ |

**Not feasible (platform policy, not technical):**
- LinkedIn — automated DM outreach violates their Terms of Service
- Twitter/X — DM API requires Enterprise tier (~$21,000/year)
- TikTok — No DM automation API exists

---

## Technical Architecture

The system is built in three layers:

```
[ Ads / Campaigns ]
        │
        ▼ click-to-message links
[ GoHighLevel — Channel Backbone ]
  SMS · Email · WhatsApp · Instagram · Facebook
        │
        ▼ webhook
[ Hiresignal AI Engine — Extended ]
  New "lead_funnel" conversation mode
  Claude API (Sonnet for qualification, Opus for closing)
  Lead database · Qualification scoring · Follow-up scheduler
        │
        ▼ API call (same channel)
[ Customer receives reply on the platform they wrote from ]
```

**What GoHighLevel provides:** Channel routing, message delivery compliance (TCPA for SMS), contact deduplication, conversation threading across all platforms under one roof.

**What Hiresignal provides:** The proven AI conversation engine, already trained and tested, now running a sales qualification flow instead of an interview flow.

**What is new custom code:** The webhook bridge connecting both, the lead database, the follow-up state machine, and the admin dashboard.

---

## Why Building On Hiresignal Is an Advantage

Most of the hard problems are already solved:

| Component | Status |
|---|---|
| Claude AI conversation engine | ✓ Already built and running |
| Turn management and message history | ✓ Already built |
| Conversation flow limits and state | ✓ Already built |
| PHP backend infrastructure | ✓ Already built |
| Admin authentication | ✓ Already built |

We are not starting from zero. We are extending a working product. This cuts development time roughly in half compared to a greenfield build.

---

## Implementation Timeline

### Phase 1 — Foundation (Weeks 1–3)
**Goal:** First lead captured and AI response delivered via SMS and Email

- Extend Hiresignal database with lead and conversation tables
- Build new `lead_funnel` conversation mode (sales system prompt, qualification logic)
- Connect GoHighLevel webhook receiver
- SMS and Email channels working end-to-end
- Basic admin view: see all leads and their status

**Milestone:** Send a test lead via SMS, receive AI response, see it in admin panel.

---

### Phase 2 — All Channels + Follow-Up Engine (Weeks 4–5)
**Goal:** All 6 channels live, follow-up engine running

- WhatsApp integration via GoHighLevel
- Telegram bot integration
- Follow-up scheduler: state machine, cooling period logic, message templates
- Lead qualification scoring based on AI conversation outcome
- Ad click-to-message URLs configured and tested

**Milestone:** Lead comes in via WhatsApp, doesn't respond, receives follow-up on Day 1 and Day 4 automatically.

*Note: Meta app review for Instagram and Facebook is submitted in Week 1 and runs in parallel. Review typically takes 3–7 business days.*

---

### Phase 3 — Instagram, Facebook & Production Polish (Weeks 6–7)
**Goal:** All Meta channels live, system production-ready

- Instagram DM channel activated (pending Meta approval)
- Facebook Messenger channel activated
- Full admin dashboard: lead pipeline, qualification scores, channel breakdown, campaign attribution
- Security review and rate limiting
- Load testing

**Milestone:** Lead clicks Facebook ad → opens Instagram DM → AI responds within 10 seconds.

---

### Phase 4 — QA & Production Deployment (Week 8)
**Goal:** System live in production environment

- End-to-end testing across all 6 channels
- Production server deployment
- Monitoring and alerting setup
- Handoff documentation

**Milestone:** System is live. Real leads flowing in. Team trained on the admin dashboard.

---

## Cost Breakdown

### One-Time Development Cost

| Phase | Estimated Hours | Cost (@ $85/hr) |
|---|---|---|
| Phase 1: Foundation | 50 hours | $4,250 |
| Phase 2: Channels + Follow-up | 45 hours | $3,825 |
| Phase 3: Meta + Polish | 30 hours | $2,550 |
| Phase 4: QA + Deployment | 20 hours | $1,700 |
| **Total** | **145 hours** | **$12,325** |

**Recommended budget with 20% contingency: $15,000**
*(Contingency covers: scope adjustments, Meta review delays requiring rework, additional channels or features requested mid-build)*

---

### Monthly Operating Costs

These are the platform fees required to keep the system running after deployment:

| Service | Purpose | Monthly Cost |
|---|---|---|
| GoHighLevel Agency Pro | Channel backbone: SMS, Email, WhatsApp, Instagram, Facebook routing | $297 |
| Claude API (Anthropic) | AI conversation engine | $130 – $360* |
| Server Hosting (Railway) | Webhook bridge + cron jobs | $20 |
| Database (Supabase Pro) | Lead storage and conversation history | $25 |
| WhatsApp conversation fees | Meta charges per business-initiated conversation | $15 – $60* |
| SMS fees (via Twilio/GHL) | Per-message charges | $10 – $30* |
| **Total** | | **$500 – $790/month** |

*Variable costs scale with volume. Estimates based on 500–1,000 active conversations per month.*

**Cost per 1,000 conversations handled by AI: approximately $0.50 – $0.80 each.**

---

### Cost at Scale

| Monthly Conversations | Est. Monthly Cost | Cost Per Lead Handled |
|---|---|---|
| 500 | ~$530 | ~$1.06 |
| 1,000 | ~$700 | ~$0.70 |
| 2,500 | ~$1,050 | ~$0.42 |
| 5,000 | ~$1,600 | ~$0.32 |

The system becomes more cost-efficient as volume grows. GoHighLevel is a fixed cost; only the AI and messaging fees scale.

---

### Total Investment Summary

| Item | Amount |
|---|---|
| One-time build cost | $12,500 – $15,000 |
| Monthly operating cost | $500 – $800/month |
| **12-month total cost of ownership** | **$18,500 – $24,600** |

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Meta app review rejection (Instagram/Facebook) | Medium | Medium | Submit in Week 1; delays channel, not project. SMS/WhatsApp/Email are unaffected. |
| WhatsApp Business Account approval required | Low | Low | Simple registration process; 1–3 days. |
| AI response quality needs tuning | Medium | Low | System prompt is adjustable without code changes. |
| Scope creep on admin dashboard | Medium | Medium | Define admin panel requirements before Phase 3 begins. |
| GoHighLevel pricing changes | Low | Low | All channel logic is modular — can switch backbone if needed. |

---

## What This System Is Not

To set clear expectations:

- **Not a mass-blast tool.** This is a conversational system, not a bulk SMS or email blaster. Each lead has an individual AI conversation.
- **Not a replacement for sales staff on complex deals.** The AI qualifies and warms leads; human handoff is available for high-value closes.
- **Not available on LinkedIn, TikTok, or Twitter/X** due to those platforms' API restrictions.

---

## Recommended Next Steps

1. **Approve proposal and budget** → confirm $15,000 build budget and GoHighLevel subscription
2. **Register WhatsApp Business Account** → can be done today, needed for Week 2
3. **Submit Meta Developer App for review** → submit in Week 1, runs in parallel
4. **Define qualification criteria** → what questions should the AI ask? What answers qualify vs. disqualify a lead?
5. **Write follow-up message templates** → 4 messages per channel (can be AI-generated drafts, reviewed by team)
6. **Development begins**

---

*This proposal was prepared based on the existing Hiresignal codebase and platform capabilities as of May 2026. All cost estimates are in USD. Claude API pricing is based on publicly available Anthropic pricing for claude-sonnet-4-6 and claude-opus-4-7. GoHighLevel pricing is based on their published Agency Pro plan. Variable costs are estimates and will depend on actual lead volume.*
