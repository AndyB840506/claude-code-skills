# Job market and recruitment workflows

## Job listing research
**When:** User wants to find and analyze job postings by role, company, or location.

### Pipeline
1. **Search jobs** -> `harvestapi/linkedin-job-search`
   - Key input: `keyword`, `location`, `datePosted`, `limit`
2. **Get job details** -> `apimaestro/linkedin-job-detail`
   - Pipe: `results[].jobUrl` -> `urls`
   - Key input: `urls`

### Output fields
Step 1: `title`, `company`, `location`, `jobUrl`, `postedDate`, `applicantsCount`
Step 2: `description`, `requirements`, `seniority`, `employmentType`, `salary`

### Gotcha
Both Actors are PPE. Step 1: ~$0.001/job. Step 2: ~$0.005/job. For 200 jobs, total ~$1.20. Estimate and confirm with user.

## Candidate sourcing
**When:** User wants to find potential candidates matching specific criteria.

### Pipeline
1. **Search profiles** -> `harvestapi/linkedin-profile-search`
   - Key input: `keyword`, `title`, `location`, `industry`, `limit`
2. **Enrich with details** -> `apimaestro/linkedin-profile-full-sections-scraper`
   - Pipe: `results[].profileUrl` -> `urls`
   - Key input: `urls`

### Output fields
Step 1: `fullName`, `headline`, `location`, `profileUrl`, `currentCompany`
Step 2: `experience[]`, `education[]`, `skills[]`, `certifications[]`, `languages[]`

### Gotcha
Step 2 (`apimaestro/linkedin-profile-full-sections-scraper`) costs ~$0.01/profile — the most expensive LinkedIn scraper. Use sparingly for shortlisted candidates only.

### Kuma Talent / HireSignal integration

This playbook is the outbound complement to candidates who apply directly
through the HireSignal app — use it to proactively source for a job rather
than wait for inbound applicants. Sourcing and inviting are deliberately kept
as **two separate funnels** (kumatalent.com inbound vs. LinkedIn outbound) —
the only thing they share is the job's JD, used to derive search criteria.

**Step 0 — Derive search criteria from the job's JD, don't guess keywords.**
HireSignal already has `api/jd-parser.php`, which extracts 16 structured
fields from a raw job description (`role_title`, `seniority`,
`required_stack`, `must_have_skills`, `industry_context`, `location_type`,
etc.) — the same fields used to drive the AI interview itself. Reuse that
output instead of inventing separate sourcing criteria:
- `role_title` -> `title` input for `harvestapi/linkedin-profile-search`
- `required_stack` + `must_have_skills` -> `keyword`
- `industry_context` -> `industry`
- `location_type` -> if `"remote"`, skip geographic narrowing; if
  `"on-site"`/`"hybrid"`, ask the user for the actual city/region (the JD
  parser doesn't return a literal location string)

Get the raw JD text by asking the user for the job code/title (they already
wrote it to create the job in HireSignal), or have them paste it directly.
The parser endpoint has no auth check, so it can be called directly:
`POST` to `api/jd-parser.php` with `{"job_description": "..."}`.

**No pre-interview scoring model.** Don't build a separate candidate-ranking
system for sourced profiles — HireSignal's AI interview is the real filter.
`admin/ranking.php` ranks by interview `score`, which only exists *after* a
candidate completes the interview — it has nothing to rank a sourced
candidate on before they're invited, and it requires no integration work:
once a sourced candidate completes their interview, they appear in the same
ranking as any other candidate for that `job_code`, automatically.

**Cap + pre-invite sort, not a scoring system.** Sourcing runs can easily
return more candidates than makes sense to invite. Default to a hard cap of
**20 candidates per run** (ask the user if they want fewer/more for a given
search). Before presenting the final list, sort candidates by how well their
`headline`/`experience`/`skills[]` (from enrichment) overlap with the JD's
`required_stack`/`must_have_skills`/`seniority` (from Step 0) — this is a
one-off sort to decide presentation order for *this batch*, done by reading
the data directly, not a persisted scoring model. Present the top N first;
if the search returned fewer than the cap, present all of them.

Sourced candidates do **not** go into HireSignal's production database or the
existing "Kuma Talent (Responses)" Google Sheet (that one is fed by the
kumatalent.com "Join Kuma" form for self-submitted candidates — keep
self-submitted and cold-sourced candidates separate, since they're on
different consent footing).

Instead, write results to the **"Kuma Talent — Sourced Candidates"** Google
Sheet (owned by the connected account, shared as needed —
`docs.google.com/spreadsheets/d/1TrSVLbmtjXktc_QxDQnyC73gNQOBUCxW6tspqq96ZdE`).
Columns: Date Sourced, Full Name, LinkedIn URL, Headline, Current Company,
Email, Job/Role Searched, Source, Status, Notes.

**Important tool limitation:** there is no Sheets API "append row" tool
available — only Drive's `create_file` (new files) and read tools. This means
you cannot append directly into the existing sheet. For each sourcing run:
1. Present the candidate list in chat first.
2. Create a new file via `create_file` (CSV content, auto-converts to a
   Sheet) named `Kuma Talent — Sourced Candidates — YYYY-MM-DD` with that
   batch's rows, matching the column order above.
3. Tell the user the new sheet's URL and that consolidating it into the
   master sheet (copy/paste rows, or moving into the same Drive folder) is a
   manual step on their end — don't claim it's been merged automatically.

Once the user reviews a sourced candidate and wants to screen them, generate
their invite the normal way through HireSignal's admin panel
(`admin/invites.php` — pick the job, paste the candidate's name/email as the
label, generate the link, send it). That step stays manual and untouched by
this skill — it doesn't call HireSignal's API or database directly.

## Sales signal outreach — job posting as buying signal
**When:** User wants to monitor company job postings as a signal to identify sales opportunities — e.g., a "Head of Data Engineering" hire suggests budget for data tooling.

### Pipeline
1. **Monitor target postings** -> `harvestapi/linkedin-job-search`
   - Key input: `searchUrl` (LinkedIn Jobs URL with company or role filters), `keywords`
2. **Get company context** -> `harvestapi/linkedin-company`
   - Pipe: `results[].companyUrl` -> `companyUrls`

### Output fields
Step 1: `title`, `companyName`, `description`, `employmentType`, `seniorityLevel`, `jobUrl`
Step 2: `name`, `industry`, `employeeCount`, `description`, `specialties[]`

### Gotcha
Job descriptions contain implicit buying signals — tech stack mentions, pain points, and headcount growth. Pass `description` to extract inferred tech stack and budget tier before prioritizing outreach. Contact finding (Hunter.io) is a separate API call, not an Apify Actor.

## Upwork job monitoring for freelancers
**When:** User wants to continuously monitor Upwork for new jobs matching their skills — directly relevant to freelance-gig work.

### Pipeline
1. **Scrape Upwork search** -> `apify/playwright-scraper`
   - Key input: `startUrls` (Upwork search URL with skill filters), `pseudoUrls`, `maxCrawledPages`

### Output fields
Step 1: `title`, `description`, `budget`, `clientJobsPosted`, `clientHireRate`, `postedAt`, `url`

### Gotcha
No dedicated Upwork Actor exists in the Apify Store — verify with `apify actors search "upwork"` for community options before defaulting to `apify/playwright-scraper`. Upwork pages are JS-heavy so Playwright is required over basic HTTP scraping. For high-frequency monitoring (every 15 min), store seen job URLs to avoid re-processing duplicates.

## GitHub contributor discovery
**When:** User wants to find developers who contribute to specific open-source projects.

### Pipeline
1. **Get contributors** -> `janbuchar/github-contributors-scraper`
   - Key input: `repoUrls`

### Output fields
Step 1: `username`, `contributions`, `profileUrl`, `avatarUrl`
