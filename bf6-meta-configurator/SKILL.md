---
name: bf6-meta-configurator
description: "Weapon meta + controller settings configurator for Battlefield 6, covering Multiplayer AND REDSEC (battle royale) separately. Fetches the latest patch notes and current-month community meta fresh on every run (weapons, attachments, aim/deadzone settings — nothing hardcoded, nothing invented), ranks a Top 3 per weapon category per mode, and outputs a mobile-friendly tactical HTML report. Remembers your last setup for one-tap re-runs. Short triggers: bf6, BF6, battlefield, battlefield 6, redsec, REDSEC. Triggers (ES): meta bf6, armas meta battlefield 6, mejor arma bf6, meta redsec, ajustes de control bf6, deadzone bf6, sensibilidad bf6, configurar control bf6, top armas battlefield 6, tier list bf6, qué arma usar en bf6. Triggers (EN): weapon meta bf6, best gun bf6, bf6 meta loadout, redsec meta, bf6 controller settings, bf6 deadzones, bf6 aim settings, best weapons battlefield 6, bf6 tier list, battle royale bf6 loadout."
---

# BF6 Meta Configurator

Fresh-data configurator: current weapon meta (Multiplayer and REDSEC ranked
separately) + controller settings, rebuilt from live sources on every run and
delivered as a tactical HTML report.

**Core rule — never invent data.** No weapon stats, attachment names, or
settings values that a source didn't provide. Unsourced attachment slots get a
generic effect description ("the suppressor with the lowest recoil penalty you
have unlocked"), never a made-up proper name. Every data point carries a source
tier: `CONFIRMED` / `COMMUNITY` / `INFERRED` / `STALE`.

## Execution

Follow [workflows/run-report.md](workflows/run-report.md) end to end:

1. **Setup menu** — one `AskUserQuestion` call (platform · mode MP/REDSEC/both ·
   class · playstyle). Language auto-detected from the user's message. If
   `last-run.json` exists, offer the previous setup as a one-tap option first.
2. **Fresh data sweep** — parallel searches: patch notes, MP meta, REDSEC meta,
   and controller/aim setting changes for the current patch. Sources older than
   60 days ⇒ STALE banner.
3. **Rank Top 3 per category, PER MODE** — MP and REDSEC are different metas.
4. **Controller settings** — searched fresh each run (patch aim changes + pro
   consensus), never served from a canned table; a baseline table exists only
   as a clearly-labeled fallback.
5. **HTML report** — per [workflows/html-spec.md](workflows/html-spec.md).
   Output to `E:\Claude Output\bf6\` (desktop) or `D:\Claude Output\bf6\`
   (laptop) — never inside `~/.claude` — then open it and post a compact chat
   summary.
6. **Persist** the chosen setup to `last-run.json` in this folder.

## Re-run behavior

Designed to re-run after every patch: each run re-fetches everything and writes
a new dated report (old ones are kept as meta-evolution snapshots — the embedded
JSON block is the data layer for a future companion app).
