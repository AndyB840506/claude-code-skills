# Handoff: Chorus — synthetic-audience engine (Phase 1 MVP built + pushed)

**Date:** 2026-06-22
**Status:** Complete — Chorus Phase 1 built, verified (typecheck + build + end-to-end smoke), and pushed to a new private repo. Runs in mock mode today; live mode needs an API key. Phase 2/3 not started.

> Note: this is the SECOND session-close of the day. The earlier one (`35b7258`, handoff `2026-06-22-ep018-deploy-launched.md`) covered the EP.018 BTQ deploy. This handoff is only about the Chorus build that followed.

---

## What We Accomplished This Session

Andy saw MiroFish (github.com/666ghj/MiroFish, an "agent-based prediction engine") and asked if we could build something like it or cooler. We did.

- **Designed Chorus** — a horizontal synthetic-audience engine: define a panel (AI personas of a real audience) → throw a stimulus (title / job posting / landing copy / pitch) → get a **calibrated distribution** of reactions. The "cooler than MiroFish" thesis: honesty (distributions + bootstrap CIs, calibration-ready data model) instead of a "predict anything" black box; horizontal across Andy's businesses, not podcast-only.
- **Scoped via questions** (Andy chose): use case = synthetic audience for content; then pivoted unprompted to **multi-domain** (podcast + HireSignal + andyfreelancer); name = **Chorus**; stack = my pick.
- **Built Phase 1 end-to-end** at `C:\Users\andre\repos\chorus`:
  - Next.js 15 + TypeScript, server-side API (key never hits browser).
  - 3 templates: Behind the Queue listeners, HireSignal candidates, andyfreelancer prospects.
  - Engine: Opus persona generation (`src/lib/personas.ts`) → Haiku swarm, concurrency-capped + cost-metered (`swarm.ts`) → numeric aggregation w/ bootstrap 95% CI + sentiment + segment split + Opus synthesis of clustered themes/verdict (`synthesis.ts`). Mock mode (`mock.ts`, `anthropic.ts isMock()`). Local JSON store (`store.ts`).
  - API routes: `/api/templates`, `/api/panels`, `/api/run`. Dark dashboard UI (`src/app/page.tsx` + `globals.css`) with honest "directional, not a forecast" caveat.
- **Verified (not claimed):** `npm run typecheck` ✅, `npm run build` ✅ (5 routes), server boots, live smoke test of all 3 endpoints in mock mode — 40-persona HireSignal panel, run produced mean 39% (CI 31–47%), correctly verdicted a buzzword job posting as "Weak". Data persisted to `data/`.
- **Pushed:** private repo `AndyB840506/chorus` (commit "Chorus Phase 1…"). Created via `gh repo create chorus --source . --remote origin --private --push`.
- **Memories saved:** `project_chorus`, `feedback_build_horizontal_tools`, `feedback_mock_mode_llm_apps`, `feedback_cross_machine_portability`.
- **Retrospective:** no skill edits (net-new product in a separate repo; learnings captured as the 4 memories above). **Audit:** clean (all SKILL.md ≤50 lines, no loose files).

## Where We Paused

**Last action:** pushed Chorus to GitHub + saved memories + this session-close.
**Next action:** Andy's choice — Phase 2 (A/B head-to-head + interview any agent, my pick) or Phase 3 (calibration harness). Or just run it.
**Blockers:** none. Live mode needs Andy to paste `ANTHROPIC_API_KEY` into `chorus/.env.local`.

## Files to Read First

- `~/.claude/projects/.../memory/project_chorus.md` — full project context (repo, stack, roadmap, business angle)
- `C:\Users\andre\repos\chorus\README.md` — what it is + how to run
- `C:\Users\andre\repos\chorus\src\lib\` — the engine (personas / swarm / synthesis / anthropic / store / mock)
- `C:\Users\andre\repos\chorus\src\app\page.tsx` — the UI

## Notes / Gotchas

- **Chorus is a SEPARATE repo** (`AndyB840506/chorus`), NOT part of kit-skill-creator. Don't confuse the two.
- **Run it:** `cd chorus; npm run dev` → localhost:3000. Mock mode works with no key (`MOCK=1` or key absent). Add key in `.env.local` for real calls.
- **Desktop:** clone `AndyB840506/chorus`, `npm install`, add `.env.local`. Portable — no machine-specific paths; `data/` is local + gitignored. Sync via `git pull`.
- **Cost numbers in the UI are ESTIMATES** — placeholder per-token rates in `src/lib/anthropic.ts` (marked estimated). Verify against real Anthropic pricing before quoting a client.
- **Business angle:** sell as done-for-you panel-testing service today (no extra build); embed a free demo on andyfreelancer as lead-gen; SaaS only after clients prove they'll pay.

## Questions to Answer (al retomar)

- ¿Alguno de los next steps ya se hizo? (preguntar antes de asumir)
- ¿Andy ya probó Chorus con su API key (live mode)? ¿Funcionó la generación real de personas?
- ¿Phase 2 (A/B + interview) o Phase 3 (calibration)?
- ¿Avanzó el angle de andyfreelancer (servicio / demo)?
- (Hilos previos abiertos) EP.018 quote cards en Flow; andyfreelancer correo/indexación; MPD EP.005 sin grabar; EP.019 Gladiator próximo en roadmap BTQ.
