> **DRAFT — For internal review by Andres Bermudez and Hugo Lancheros before submission.**
> Items marked ⚠️ require action or verification before this document is finalized.
> **Note:** This version targets NRC IRAP (National Research Council — Industrial Research Assistance Program). Before submitting, consult with an IRAP Industrial Technology Advisor (ITA) to confirm project eligibility and eligible labour cost scope.

---

# Grant Proposal
## Kuma Group AI Platform for Canadian Small and Medium Enterprises
### Module 1: Kuma Flow — Multi-Channel AI Lead Engagement | Module 2: AI-Powered Text Candidate Screening

**Submitted to:** NRC IRAP — National Research Council Industrial Research Assistance Program
**Applicant Organization:** Kuma Group
**Business Registration:** ⚠️ *Pending — business must be registered in Ontario before submission*
**Primary Contact:** Hugo Lancheros, Marketing & Sales Director (Ontario, Canada)
**Co-Founder:** Andres Bermudez, Lead Developer (Remote — Colombia)
**Contact Email:** hello@kumatalent.com | **Phone:** +1 (587) 894-9527
**Submission Date:** May 2026
**Requested Funding:** $58,000 CAD
**Project Duration:** 12 months

---

> ⚠️ **IRAP Labour Eligibility Note:**
> NRC IRAP reimburses eligible Canadian R&D labour costs. Hugo Lancheros's Ontario-based hours are fully IRAP-eligible. Andres Bermudez's hours, performed remotely from Colombia, may not qualify as eligible Canadian labour under IRAP guidelines. Before submission, confirm the eligible labour portion with your assigned ITA (Industrial Technology Advisor). The budget figures below reflect total project costs — the IRAP contribution should be scoped to the Canadian-based eligible portion only.

---

## Executive Summary

Canada's small and medium enterprises face two challenges that together define whether a business survives or grows: **finding customers** and **finding the right people to serve them.** Both require speed, consistency, and intelligent engagement that most SMEs cannot deliver with the limited staff and budgets available to them.

Kuma Group proposes the development of a dual-module, Canadian-built AI platform that addresses both challenges simultaneously:

- **Module 1 — Kuma Flow:** Captures leads from any digital channel (SMS, email, WhatsApp, Instagram, Facebook, Telegram), responds to each customer within seconds on that same platform, and manages a smart follow-up cadence until a sale is made or the lead is placed in a long-term nurture cycle.

- **Module 2 — Hiresignal Text Candidate Screening:** When a Canadian SME needs to hire, AI conducts a conversational text-based pre-screening with every applicant — automatically, at any hour — ranking candidates by fit before a business owner reads a single resume. No voice calls. No scheduling. No recruitment agency fees.

Both modules are built on AI technology Kuma Group has already developed and proven in market through our existing **Hiresignal** platform. This is not speculative R&D — it is the disciplined extension of a working, made-in-Canada AI system into a commercially viable, nationally deployable platform.

**Total grant request: $58,000 CAD**
**Time to full deployment: 10 weeks**
**Canadian SMEs in pilot cohort: 15–25 businesses**

---

## The Team

**Andres Bermudez — Lead Developer** *(Remote — Colombia)*
Andres is the architect and primary developer of Hiresignal, Kuma Group's existing AI interview platform. He has hands-on experience building conversational AI systems using Anthropic's Claude API, PHP backend infrastructure, and multi-channel messaging integrations. He leads all technical development for this project.

**Hugo Lancheros — Marketing & Sales Director** *(Ontario, Canada)*
Hugo leads Kuma Group's go-to-market strategy and client relationships. He manages the Canadian SME pilot cohort, leads stakeholder communications, and oversees the commercialization pathway. Hugo is the primary Canadian-based team member and IRAP point of contact.

*⚠️ Hugo: add 2–3 sentences about your background, experience in sales/marketing, and any industry-specific knowledge relevant to Canadian SMEs.*

---

## The Problem: Two Gaps Costing Canadian SMEs Every Day

### Gap 1 — The Customer Response Gap

Modern consumers expect a response within minutes. A potential customer who clicks a Facebook ad at 9:30 PM and gets no reply until the next morning has, in most cases, already called a competitor. Large businesses solve this with enterprise CRM platforms and dedicated after-hours teams — tools that cost $3,000–$10,000 CAD per month, well beyond what a small Canadian business can justify.

The result: Canadian SMEs spend real money driving traffic through digital ads and social media, then lose a significant portion of those leads because no one was available to respond in time, on the right channel.

### Gap 2 — The Hiring Gap

Labour shortages are one of the most consistently cited challenges facing Canadian small businesses. Across every sector — skilled trades, hospitality, retail, healthcare support, childcare, manufacturing, and logistics — SMEs struggle to hire efficiently. Yet the standard hiring process for an SME is brutal:

- Post a job on Indeed or LinkedIn
- Receive 30–80 applications, most not meeting basic requirements
- Read every resume manually (3–5 minutes each = hours of lost productivity)
- Contact candidates by phone, many of whom don't answer
- Schedule interviews with people who don't show up

Recruitment agencies solve this problem — but charge 15–25% of a candidate's annual salary per placement. For a $50,000/year role, that's $7,500–$12,500 CAD per hire. For a small business making three or four hires per year, recruitment fees become one of their largest variable costs.

**The R&D opportunity:** Building AI that conducts genuinely useful, contextually adaptive, multi-turn text conversations for both lead qualification and candidate screening — at any hour, at no marginal cost per interaction — requires meaningful technical innovation. Kuma Group is addressing unsolved problems in conversational AI scoring, cross-channel session persistence, and adaptive tone management for non-technical end users.

---

## The Innovation: Why This Qualifies as Canadian R&D

This project is not an integration of existing commercial AI tools. It involves the development of novel technical capabilities:

**Technical uncertainties being addressed:**
1. **Adaptive conversation scoring** — Building a scoring model that evaluates lead quality or candidate fit from unstructured, multi-turn text exchanges, where the AI must infer implicit signals (tone, specificity, responsiveness) in addition to explicit responses.
2. **Cross-channel session management** — Maintaining conversational context and follow-up state across six messaging platforms without requiring a unified identity from the customer.
3. **Tone-calibrated AI for SME contexts** — Calibrating Claude AI conversation flows for the varied registers required across industries (trades, food service, healthcare, professional services) without requiring per-business model fine-tuning.
4. **Cooling and re-engagement logic** — Developing the state machine and timing system that determines when to follow up, when to pause, and when to re-engage after silence, without appearing intrusive.

These are non-trivial engineering and AI design problems. The solutions, once built, will be owned entirely by a Canadian company and deployable to the Canadian market.

---

## The Solution: A Dual-Module Canadian AI Platform

### Module 1 — Kuma Flow

**How it works for a Canadian SME:**

A local contractor runs a Facebook ad. A homeowner in Oakville clicks "Get a Quote" at 8:15 PM. That click opens a WhatsApp conversation. Within 10 seconds, Kuma Flow responds: *"Hi! Thanks for reaching out about your project. To make sure we connect you with the right person — is this for a renovation, a repair, or something new?"*

The conversation continues naturally. The AI gathers what the customer needs, their timeline, and their contact details. If the homeowner stops responding, the system sends a friendly follow-up the next day, then again on Day 4 — always on WhatsApp, always in a non-pushy tone. After four attempts without a response, the lead enters a 30-day rest period, then the system re-engages automatically with a fresh message.

The business owner wakes up to a dashboard showing qualified leads, their conversation history, and a recommended next action — with zero after-hours effort required.

**Supported channels:**

| Channel | Capture | AI Response | Automated Follow-Up | Ad-Triggered Entry |
|---|:---:|:---:|:---:|:---:|
| SMS | ✓ | ✓ | ✓ | ✓ |
| Email | ✓ | ✓ | ✓ | ✓ |
| WhatsApp | ✓ | ✓ | ✓ | ✓ |
| Instagram Direct | ✓ | ✓ | ✓ | ✓ |
| Facebook Messenger | ✓ | ✓ | ✓ | ✓ |
| Telegram | ✓ | ✓ | ✓ | ✓ |

---

### Module 2 — Hiresignal Text Candidate Screening

**How it works for a Canadian SME:**

A restaurant owner in Mississauga needs to hire two line cooks. She posts the job and receives 47 applications over three days. Normally, this would mean an entire day away from the kitchen.

Instead, within minutes of each application arriving, Hiresignal automatically sends the candidate a text message: *"Hi [Name], thanks for applying to [Restaurant] for the Line Cook position. I have a few quick questions to make sure this is a great fit for both of you — takes about 5 minutes and you can reply whenever is convenient."*

The AI conducts a structured but conversational text screening:
- Availability and start date
- Relevant experience and certifications
- Comfort with the pace and type of cuisine
- Compensation expectations
- Any questions or concerns they'd like answered before an interview

Each candidate is scored on fit. The restaurant owner opens her dashboard and sees five candidates ranked highest — with their full conversation summaries — and those not meeting criteria marked with a brief explanation. She calls the top two that afternoon and hires one the next day.

**No voice calls required.** Candidates respond on their own schedule, from any phone, via SMS or WhatsApp.

---

## Why This Is Canadian Technology — Not Another Foreign Subscription

Canadian SMEs currently spend an estimated significant portion of their technology budgets on US-headquartered platforms: Salesforce, HubSpot, Indeed, LinkedIn, ZipRecruiter. These subscriptions:

- Remove capital from the Canadian economy
- Store Canadian resident and candidate data on servers subject to US jurisdiction
- Generate no Canadian intellectual property
- Create no Canadian jobs

**The Kuma Group platform is different:**

- Ontario-registered Canadian company with a distributed development team
- Intellectual property owned by a Canadian company
- Designed for Canadian hosting infrastructure (PIPEDA-aligned)
- Subscription revenue from Canadian SMEs stays in Canada
- As the platform scales, it creates Canadian technology jobs — not foreign shareholder returns

Canada's federal AI strategy explicitly calls for domestic AI capability — not dependency on foreign platforms. This project is a direct expression of that mandate: a Canadian team building Canadian AI, for Canadian businesses, owned by a Canadian company.

---

## Economic and National Impact

### Direct Impact: Canadian SME Pilot Cohort (15–25 Businesses)

Pilot businesses will be selected across sectors where the lead response gap and hiring gap are most acute: skilled trades, professional services, retail, food service, childcare, and personal care services.

Each pilot SME gains access to both modules and will be measured before and after deployment on:

**Module 1 (Kuma Flow):**
- Average response time to new leads (baseline vs. post-deployment)
- Percentage of leads receiving follow-up within 24 hours
- Lead-to-qualified-conversation rate

**Module 2 (Candidate Screening):**
- Time spent per hire (hours of owner/manager time)
- Cost-per-qualified-candidate (vs. agency or manual process)
- Candidate response rate to text screening vs. phone tag

### Canadian Job Creation

| Role | Type | Count | Duration |
|---|---|---|---|
| Lead Developer (Andres Bermudez) | Remote — Colombia | 1 FTE | 10 months |
| Marketing & Sales (Hugo Lancheros) | Direct — Ontario | 1 FTE | 12 months |
| Junior Developer / QA | Direct — Ontario | 1 part-time | 6 months |
| SME Onboarding Specialist | Direct — Ontario | 1 part-time | 8 months |

**Indirect job creation:** SMEs that convert more leads and hire more efficiently are positioned to grow revenue and headcount. Conservative projections for the 15–25 pilot businesses suggest **20–45 indirect jobs** created or retained within 18 months.

### Alignment with Canada's Digital Innovation Priorities

| Federal Priority | How This Project Delivers |
|---|---|
| Canadian AI sovereignty and innovation | Canadian-built, Canadian-hosted, Canadian IP — directly advances Canada's national AI strategy |
| SME productivity and digital transformation | Addresses the productivity gap for approximately 1.2 million Canadian SMEs through AI automation |
| Canadian labour market modernization | AI screening improves hiring quality, speed, and consistency for SMEs nationwide |
| PIPEDA-compliant data infrastructure | Canadian data residency by design; no US jurisdiction exposure for Canadian citizen data |
| Export-ready Canadian technology | Scalable SaaS platform with international market potential, built and owned in Canada |
| R&D employment and skills development | Direct R&D employment in Ontario; advances Canada's applied AI development capability |

---

## Implementation Plan

### Phase 1 — Kuma Flow Foundation (Weeks 1–3)
**Deliverable:** Kuma Flow core live — SMS and Email channels operational

- Extend existing database with lead management and conversation tables
- Build sales qualification conversation mode within Hiresignal AI engine
- GoHighLevel webhook integration
- SMS and email channels end-to-end
- Basic admin dashboard: lead list, status, conversation history
- Submit Meta developer application (processes in parallel throughout Phase 1–2)

---

### Phase 2 — Kuma Flow Full Channels + Follow-Up Engine (Weeks 4–5)
**Deliverable:** All 6 channels live; automated follow-up and cooling system operational

- WhatsApp and Telegram channels
- Follow-up scheduler: state machine, cooling period, message cadence
- Lead scoring output based on AI conversation
- Ad click-to-message URL templates for all platforms

---

### Phase 3 — Module 2: Hiresignal Text Screening (Weeks 5–7)
*(Runs in parallel with Phase 2 completion)*
**Deliverable:** Candidate screening via text fully operational

- Job requisition intake form (employer defines role, must-haves, and disqualifiers)
- Automated candidate outreach via SMS and WhatsApp on application receipt
- AI text-based screening conversation (structured qualification, flexible tone)
- Candidate scoring algorithm (availability, experience, compensation alignment, culture signals)
- Employer dashboard: ranked candidates, conversation summaries, recommended next actions
- Integration note: voice module architecture preserved but not activated in this phase

---

### Phase 4 — Meta Channels + Admin Polish (Weeks 6–8)
**Deliverable:** Instagram and Facebook Messenger live; full admin dashboards for both modules

- Instagram DM and Facebook Messenger activated (pending Meta approval, submitted Week 1)
- Full analytics: channel breakdown, campaign attribution, conversion tracking
- Candidate pipeline view for hiring module
- Security audit, rate limiting, PIPEDA compliance review

---

### Phase 5 — Production Deployment & SME Pilot Launch (Weeks 9–10 → Month 3)
**Deliverable:** 15–25 Canadian SMEs live on both modules; baseline data collection begins

- Production deployment on Canadian cloud infrastructure
- Pilot cohort onboarded across both modules
- Weekly performance reviews with pilot participants
- System tuning based on real-world data

---

### Phase 6 — Evaluation & Commercialization (Months 4–12)
**Deliverable:** Impact report; commercial model live; sustainability confirmed

- 6-month impact assessment across both modules for all pilot SMEs
- Refinement of AI screening and qualification logic
- Commercial pricing tiers launched for Canadian market
- 12-month IRAP project completion report submitted to NRC

---

## Budget

> ⚠️ **IRAP Note:** Only Canadian-based labour hours are eligible for IRAP reimbursement. Hugo Lancheros's Ontario-based hours (Marketing & Sales and SME onboarding) are fully eligible. Andres Bermudez's development hours, performed from Colombia, should be confirmed with your ITA before including in the eligible labour claim. Infrastructure and third-party service costs are generally not reimbursable under IRAP.

### Module 1 — Kuma Flow Development

| Item | Hours | Rate (CAD) | Cost (CAD) |
|---|---|---|---|
| AI engine extension + channel integration | 90 hrs | $115/hr | $10,350 |
| Follow-up engine + lead database | 55 hrs | $115/hr | $6,325 |
| Junior developer / QA | 40 hrs | $70/hr | $2,800 |
| **Module 1 Subtotal** | | | **$19,475** |

---

### Module 2 — Hiresignal Text Screening Development

| Item | Hours | Rate (CAD) | Cost (CAD) |
|---|---|---|---|
| Candidate outreach + text conversation flow | 22 hrs | $115/hr | $2,530 |
| Scoring algorithm + ranking logic | 18 hrs | $115/hr | $2,070 |
| Employer dashboard (job intake + candidate pipeline) | 18 hrs | $115/hr | $2,070 |
| Junior developer / QA | 20 hrs | $70/hr | $1,400 |
| **Module 2 Subtotal** | | | **$8,070** |

---

### Shared Development Costs

| Item | Hours | Rate (CAD) | Cost (CAD) |
|---|---|---|---|
| Project management (Andres + Hugo coordination) | 20 hrs | $95/hr | $1,900 |
| Security review, PIPEDA compliance check | 10 hrs | $115/hr | $1,150 |
| Production deployment + infrastructure setup | 12 hrs | $115/hr | $1,380 |
| Documentation + onboarding materials | 10 hrs | $70/hr | $700 |
| **Shared Subtotal** | | | **$5,130** |

---

### Platform Infrastructure — First 12 Months

| Service | Purpose | Monthly (CAD) | Annual (CAD) |
|---|---|---|---|
| GoHighLevel Agency Pro | Channel backbone for Module 1 | $407 | $4,884 |
| Anthropic Claude API | AI engine for both modules (~1,500 conversations/month) | $370 | $4,440 |
| Canadian Cloud Hosting | Webhook server, cron scheduler | $40 | $480 |
| Database (Supabase) | Leads, candidates, conversations | $35 | $420 |
| WhatsApp conversation fees | Meta per-conversation billing | $60 | $720 |
| SMS messaging (Twilio via GHL) | Per-message charges | $35 | $420 |
| **Infrastructure Subtotal** | | **$947/mo** | **$11,364** |

---

### Pilot Program Delivery

| Item | Cost (CAD) |
|---|---|
| SME onboarding (15–25 businesses, both modules) | $4,200 |
| Training workshops and reference materials | $2,100 |
| Pilot monitoring, reporting, and performance reviews | $2,800 |
| **Pilot Subtotal** | **$9,100** |

---

### Contingency (10%)

| Item | Cost (CAD) |
|---|---|
| Contingency reserve | $5,314 |

*(Covers Meta review delays, pilot scope adjustments, additional SME onboarding needs)*

---

### Total Budget Summary

| Category | Amount (CAD) |
|---|---|
| Module 1 development | $19,475 |
| Module 2 development | $8,070 |
| Shared development costs | $5,130 |
| Platform infrastructure (12 months) | $11,364 |
| Pilot program delivery | $9,100 |
| Contingency (10%) | $5,314 |
| **Total Grant Request** | **$58,453** |
| **Requested (rounded)** | **$58,500** |

---

### Sustainability After Grant Period

After the 12-month grant period, the platform sustains itself through a tiered commercial licensing model offered to Canadian SMEs:

| Tier | Includes | Monthly Price (CAD) |
|---|---|---|
| Starter | 1 module (Lead or Hiring), up to 3 channels, 200 conversations | $349 |
| Growth | Both modules, all channels, 1,000 conversations | $599 |
| Scale | Both modules, all channels, unlimited conversations, priority support | $999 |

**Break-even point:** Approximately 35–40 paying SME subscribers at the Growth tier.
**Canadian market potential:** With approximately 1.2 million registered small businesses in Canada *(verify against latest Statistics Canada Business Register before submission)*, even 0.01% adoption represents 120 paying customers — well above the break-even threshold — and a commercially viable, job-sustaining Canadian technology company.

---

## Measurable Outcomes and Evaluation

Outcomes reported at 6 months and 12 months:

| Metric | Target |
|---|---|
| Canadian SMEs in active pilot | 15 – 25 |
| Average lead response time (before vs. after) | Reduction from hours to under 60 seconds |
| Time-per-hire for pilot SMEs using Module 2 | Reduction of 60%+ vs. manual process |
| Cost-per-qualified-candidate vs. recruitment agency | Reduction of 70%+ |
| Canadian direct jobs created | 3 – 4 |
| Estimated indirect jobs (SME growth + stable hiring) | 20 – 45 |
| Platform uptime | 99.5%+ |
| Data hosted on Canadian infrastructure | 100% |
| Paying subscribers at month 12 | 20+ (path to sustainability confirmed) |
| IRAP project completion report | Submitted on time |

---

## Organizational Capacity

**Kuma Group** is a technology venture founded by Andres Bermudez and Hugo Lancheros, focused on applied AI solutions for business operations. The team has demonstrated capacity to build and deploy production AI systems through the development of Hiresignal — a fully operational AI conversational interview platform — built entirely in-house, currently in active use, and serving as the technical foundation for both modules proposed in this project.

Kuma Group is Ontario-registered with a distributed remote team. Andres Bermudez leads technical development remotely from Colombia; Hugo Lancheros manages business operations and client relationships from Ontario. This structure is common to Canadian technology startups and is consistent with IRAP's recognition that modern R&D teams operate across geographic boundaries.

**Evidence of technical capacity:**
- Hiresignal platform: live, production PHP + Claude AI conversational system
- Multi-turn conversation management with history, state, and scoring built and tested
- Real-world validation of the AI engine's ability to conduct structured, professional text conversations

**Funding history:** This is Kuma Group's first external grant application. The team has self-funded all development to date, demonstrating commitment without external support.

> ⚠️ **Before submission — items to resolve:**
>
> 1. **ITA assignment:** Contact NRC IRAP to be assigned an Industrial Technology Advisor. The ITA reviews the project for technical merit and innovation before a formal application is accepted.
>
> 2. **Business registration:** An active Ontario business registration is required. Register at ontario.ca/businessregistry (~$60 CAD, same day). See the companion document *Ontario Business Registration — Draft Reference* for step-by-step guidance.
>
> 3. **IRAP labour eligibility confirmation:** Work with your ITA to confirm which labour costs in the budget qualify as IRAP-eligible Canadian R&D. Only Hugo's Canadian-based hours are likely eligible without further documentation about Andres's status.
>
> 4. **Financial statement:** Prepare a simple one-page summary of current assets and any existing Hiresignal revenue. IRAP requires basic financial documentation.
>
> 5. **Hugo's bio:** Add 2–3 sentences about background and experience (line 47 of this document).

---

## Statement of Canadian Technology Commitment

Kuma Group commits to the following conditions as part of this project:

1. All product development and client-facing work managed by Canadian-based personnel
2. Intellectual property developed under this project remains owned by Kuma Group, a registered Ontario business
3. Production data hosted on Canadian cloud infrastructure; PIPEDA compliance documented
4. A public impact report published at 12 months detailing measurable outcomes for pilot SMEs
5. The commercialization model will prioritize Canadian SME access before any international expansion
6. Full project accounting and IRAP progress reports provided to NRC on the agreed schedule

---

## Conclusion

Canada's small businesses are the backbone of this country's economy, and they face the same two challenges year after year: not enough customers, and not enough of the right people to serve them. Those challenges are not going to disappear — but they can be met with better tools.

Kuma Group has already built the AI technology to address both. What this funding enables is not a research project or a prototype. It is the step from a working internal system to a Canadian-owned, nationally deployable platform that puts enterprise-grade capability in the hands of a trades contractor in Hamilton, a restaurant owner in Vancouver, or a childcare operator in Halifax.

The technology stays in Canada. The jobs stay in Canada. The intellectual property stays in Canada. And the small businesses that use it — and the people they hire and the customers they serve — stay, grow, and contribute to Canada's economy for years to come.

We respectfully request **$58,500 CAD** to make that possible.

---

*All cost estimates are in Canadian dollars. USD-denominated platform costs converted at approximately 1.37 CAD/USD. Developer rates reflect current Ontario market rates. Statistics referencing Canadian SME counts are approximate — Kuma Group recommends verifying figures against the most current Statistics Canada Business Register before final submission. This proposal reflects the platform as designed in May 2026; voice functionality for Hiresignal is architecturally supported but excluded from this scope due to cost considerations. IRAP eligibility determinations are subject to review by the assigned Industrial Technology Advisor.*
