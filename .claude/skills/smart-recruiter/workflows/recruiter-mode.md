# Workflow: Recruiter Mode — Configure Position

Gather position details through conversational questions. Save as `job-config.json`.

## Welcome Message

> **Smart Recruiter — Job Setup**
>
> Let's configure the position. I'll ask you a few questions to calibrate the interview.
> *(You can answer in Spanish or English — I'll follow your lead.)*

## Configuration Flow (Conversational)

Ask naturally, not as a checklist. Gather:

1. **Job title and seniority** (e.g. "Senior Backend Engineer")
2. **Must-have requirements** — dealbreakers if missing (3–5 max)
3. **Nice-to-have skills** — things that add value but aren't blockers
4. **Culture & team fit factors** — remote/hybrid, work style, values
5. **Compensation range** (optional)
6. **Interview language** — Spanish, English, or Auto-detect
7. **Custom questions** — any specific questions the recruiter wants to ask

## Save Configuration

After collecting all info, save as `job-config.json`:

```json
{
  "job_title": "",
  "seniority": "",
  "must_haves": [],
  "nice_to_haves": [],
  "culture_factors": [],
  "compensation_range": null,
  "interview_language": "auto",
  "custom_questions": []
}
```

## Confirmation Message

> ✅ **Configuration saved.**
>
> Share this project folder with the candidate. The interview will start automatically.
> The final fit report will be saved as `report-[name]-[date].md` in this folder.

**Next step:** Candidate opens the folder → interview runs automatically in Candidate Mode.
