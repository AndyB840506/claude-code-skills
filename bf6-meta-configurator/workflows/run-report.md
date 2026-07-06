# Run Report — data refresh flow

## Step 0 — No setup menu (app model, 2026-07-06)

Preferences (mode, playstyle, class filter, platform) are selected INSIDE the
app and persist via localStorage — do NOT ask for them. Detect language from
the user's message for CHAT replies only; **the app is ALWAYS in English**
(native game terms — translations read awkward; user decision 2026-07-06).
Always fetch data for BOTH modes and ALL platforms — the app filters locally.

## Step 1 — Fresh data sweep (parallel, capped)

Announce briefly ("Buscando el meta del parche actual… 🔍"), then run the
searches **in parallel** (multiple WebSearch calls in one message — not
sequentially). Use the CURRENT month/year in queries:

- `"Battlefield 6" patch notes weapon balance <month year>` (+ site:ea.com variant)
- `Battlefield 6 weapon meta tier list <month year>` (skip if mode = REDSEC only)
- `REDSEC battlefield meta best weapons loadout <month year>` (skip if mode = MP only)
- `Battlefield 6 best controller settings aim deadzone <month year>`

Then WebFetch the most promising URLs — **max 10 fetches total**. Two are
mandatory: **`bfhub.gg/meta/mp` and `bfhub.gg/meta/br`** — as of 2026-07-06 they
are the only found source publishing full attachment loadouts with exact names
(wzstats/battlefieldmeta hide them behind JS subpages; VGC/boostmatch 403).
Prefer sources that show a publish/update date. Record: patch version + date, buffs/nerfs,
attachment data, aim/deadzone changes, every URL used.

**Staleness rule:** if the newest usable source is >60 days old, the report and
the chat summary get a visible `STALE` banner ("meta de <date> — puede haber
cambiado"). Never present old data as current.

**Fallback:** nothing solid found → say so plainly, build from the newest
verified data available, mark everything `STALE`/`COMMUNITY`. Never fail silently.

## Step 2 — Rank Top 3 per category, PER MODE

MP and REDSEC are **separate rankings** (different TTK context, armor,
loot-based attachment access). For each mode requested, per weapon category
confirmed by sources: rank by (1) recent buffs/nerfs, (2) TTK, (3) DPS,
(4) recoil control, (5) ADS speed. Each weapon: name, 1-line reason,
TTK/DPS **only if a source states them**, source tier.

### Attachment slots — the no-blanks / no-inventions contract

For every slot (muzzle, barrel, optic, underbarrel, magazine, specialty),
exactly ONE of these three states — never an empty cell, never "TBD":

1. **Sourced name** — a source names the attachment → use it + tier badge.
2. **Pattern pick** (`INFERRED` badge, name marked `*`) — no build published
   for this weapon → assemble one from attachment names that RECUR across the
   current meta builds fetched this run (e.g. `Standard Suppressor*`,
   `Ribbed Vertical*`, `RO-M 1.75X*`, `FMJ*`). Real names only — seen in
   sources this run — never fabricated. Weapon-specific slots with unknowable
   names (barrels) get generic phrasing ("Factory barrel*"). Optic follows
   playstyle.
3. **`SIN DATOS` chip** — the slot may not exist for this weapon / nothing can
   be responsibly recommended → an explicit gray chip, styled, not a blank.

Optic always follows playstyle: Aggressive → 1x; Versatile → 2–3x;
Long Range → 4x+ (snipers may take 4x+ regardless — note it when sources agree).

## Step 3 — Controller settings (searched, never canned)

This section burned the user before — it shipped hardcoded values. Rules:

- Build the table from **this run's search results**: patch notes touching
  aim/deadzones + current pro/community consensus for the user's platform.
- Every row: **Setting | Value | Reason | Where to find it | Source tier**.
- Include at minimum: look sensitivity H/V, ADS multiplier(s), left/right stick
  deadzones, aim response curve, aim acceleration, aim assist mode, trigger
  deadzones, vibration/adaptive triggers (PS5).
- If a setting changed in a recent patch, flag it: "cambió en <patch>".
- **Only if the sweep found nothing** for a row, use the BF-series baseline
  value labeled `BASELINE` (amber badge) — and say in the section header that
  baseline rows are starting points, not current meta.

## Step 4 — Regenerate the app

Follow [html-spec.md](html-spec.md). **Stable path — same file every time** (the
user's bookmark must keep working): `E:\Claude Output\bf6\bf6-meta-app.html`
(desktop) or `D:\Claude Output\bf6\bf6-meta-app.html` (laptop) — create the
folder if missing, detect which drive exists. Embed ALL fetched data (both
modes, all platforms' settings) in the JSON block; the app renders and filters
client-side. Open it: `Start-Process "<path>"` (PowerShell).

## Step 5 — Chat summary (compact, user's language)

```
✓ App actualizada: <path> (abierta)
✓ Parche: <version + fecha> · datos de hoy
✓ Cambios vs datos anteriores: <top movers / "primer llenado">

#1 por categoría — MP:      #1 por categoría — REDSEC:
  AR  → <arma>                AR  → <arma>
  SMG → <arma>                ...
```
