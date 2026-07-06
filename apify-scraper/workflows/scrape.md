# Execution

**Rules for every `apify` command:**
1. Pass `--json` for machine-readable output (stable across CLI versions).
2. Redirect stderr with `2>/dev/null` (stderr contains progress messages that
   break JSON parsers).

## Prerequisites

- Apify CLI v1.5.0+ (`npm install -g apify-cli`)
- `APIFY_TOKEN` set (env var, or `apify login` for an interactive browser
  flow). Generate a token at https://console.apify.com/settings/integrations

If a command fails with an auth error, check `APIFY_TOKEN` is set before
anything else.

## Step 1 — Understand goal and select Actor

**First, run the ethics gate from `SKILL.md`** (robots.txt / AI-crawler
exclusion check for the target site) — required before selecting an Actor,
not only when the user is trying to avoid Apify's cost.

Identify the target platform and use case. Check `docs/actor-index.md` first
for a known Actor. If the task matches one of the playbooks listed in
`SKILL.md`, read that playbook instead of building the pipeline from scratch —
it already has the right Actor sequence, input fields, and cost gotchas.

If no Actor matches in the index, search dynamically:

```bash
apify actors search "KEYWORDS" --json --limit 10 2>/dev/null
```

From results: `items[].username`/`items[].name` (Actor ID), `items[].title`,
`items[].stats.totalUsers30Days`, `items[].currentPricingInfo.pricingModel`.

## Step 2 — Fetch Actor schema and check cost

Fetch the input schema dynamically:

```bash
apify actors info "ACTOR_ID" --input --json 2>/dev/null
```

**Before running anything that isn't FREE-tier**, read `docs/gotchas.md`'s
cost estimation protocol — most Actors are pay-per-event, and the user needs
an upfront estimate before a run that could cost real money.

For Actor documentation: `apify actors info "ACTOR_ID" --readme`

## Step 3 — Configure and run

**Skip user preferences** for simple lookups (e.g. "how many followers does X
have"). Go straight to running with quick-answer mode.

For larger tasks, confirm output format (quick answer / CSV / JSON) and
result count before running.

**Standard run (blocking):**

```bash
apify actors call "ACTOR_ID" --input-file input.json --json 2>/dev/null
```

Prefer `--input-file input.json` for large or complex inputs. For tiny
inputs, inline JSON is acceptable with shell quoting:
`--input '{"maxItems":10}'`.

From output: `.id` (run ID), `.status`, `.defaultDatasetId`,
`.stats.durationMillis`

**Fetch results:**

```bash
apify datasets get-items DATASET_ID --format json
```

For CSV: `apify datasets get-items DATASET_ID --format csv`

**Quick answer mode:** Fetch results as JSON, pick top 5, present formatted
in chat.

**Save to file:** Fetch results, use the Write tool to save as
`YYYY-MM-DD_descriptive-name.csv` or `.json`.

**Large/long-running scrapes:**

```bash
apify actors start "ACTOR_ID" --input-file input.json --json 2>/dev/null
```

Poll: `apify runs info RUN_ID --json 2>/dev/null` (check `.status` for
`SUCCEEDED`).

## Step 4 — Deliver results

Report: result count, file location (if saved), key data fields, and links:
- Dataset: `https://console.apify.com/storage/datasets/DATASET_ID`
- Run: `https://console.apify.com/actors/runs/RUN_ID`

For multi-step playbooks: mention the next pipeline step from the playbook
if there is one.

## Troubleshooting

See `docs/gotchas.md` for the full list (cookie-dependent Actors, rate
limiting, empty results, deprecated Actors, LinkedIn/SEO pricing tiers). Quick
reference for run failures:

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `status: FAILED` | Actor crashed or input invalid | Read `.statusMessage` in JSON; check run log at `https://console.apify.com/actors/runs/RUN_ID/log` |
| `isDeprecated: true` | Actor is end-of-life | Search for replacement: `apify actors search "KEYWORDS" --json` |
| Empty dataset | Query too narrow, geo-restriction, or anti-bot block | Broaden search terms; enable Apify Proxy; check Actor README |
| Run takes >10 minutes | Large scrape or slow target site | Switch to `apify actors start` + poll with `apify runs info` |
