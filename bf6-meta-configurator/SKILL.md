---
name: bf6-meta-configurator
description: "Data refresher for the BF6 Meta Ops app — an interactive local HTML app covering Battlefield 6 Multiplayer AND REDSEC (battle royale) weapon meta + controller settings. The user picks mode/playstyle/class/platform INSIDE the app (localStorage-persisted); invoking this skill just re-fetches fresh patch/meta/settings data and regenerates the app file. Nothing hardcoded, nothing invented; every data point carries a source tier. Short triggers: bf6, BF6, battlefield, battlefield 6, redsec, REDSEC. Triggers (ES): actualiza el meta bf6, meta bf6, armas meta battlefield 6, meta redsec, ajustes de control bf6, deadzone bf6, sensibilidad bf6, tier list bf6, qué arma usar en bf6. Triggers (EN): update bf6 meta, refresh bf6 app, weapon meta bf6, best gun bf6, redsec meta, bf6 controller settings, bf6 deadzones, bf6 tier list, battle royale bf6 loadout."
---

# BF6 Meta Configurator — app refresher

The deliverable is **`bf6-meta-app.html`** — an interactive single-file app
(mode MP/REDSEC, playstyle, class filter, and platform are selected IN the app;
choices persist via localStorage; weapon cards click-open into full attachment
loadouts). This skill's only job on invocation: **fetch fresh data and
regenerate that file at the same path**, then open it.

**Core rule — never invent data.** No weapon stats, attachment names, or
settings values a source didn't provide. Weapons without a published build get
"pattern picks": attachment names that recur across the current meta builds,
marked `*` + `INFERRED`. Every data point carries a tier:
`CONFIRMED` / `COMMUNITY` / `INFERRED` / `NO DATA` / `STALE`.

## Execution

Follow [workflows/run-report.md](workflows/run-report.md):

1. **No setup menu** — preferences live inside the app. Chat replies follow the
   user's language; **the app itself is ALWAYS in English** (native game terms).
2. **Fresh data sweep** — parallel searches (patch notes, MP meta, REDSEC meta,
   controller/aim changes) + mandatory `bfhub.gg/meta/mp` and `/meta/br`
   fetches for exact attachment builds. Max 10 fetches.
3. **Rank Top 3 per category, PER MODE** — MP and REDSEC are different metas.
4. **Regenerate the app** per [workflows/html-spec.md](workflows/html-spec.md)
   at `E:\Claude Output\bf6\bf6-meta-app.html` (desktop) or `D:\...` (laptop) —
   same path every time so the user's bookmark keeps working — embedding ALL
   fetched data in the JSON block. The app shows its own data age and
   self-marks STALE after 60 days.
5. **Open it** (`Start-Process`) and post a compact chat summary (what changed
   vs the previous data, patch version, freshness).
