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
mandatory: **`bfhub.gg/meta/mp` and `bfhub.gg/meta/br`** — bulk source of full
attachment loadouts with exact names (wzstats/battlefieldmeta hide theirs
behind JS subpages; VGC/boostmatch 403). Prefer sources that show a date.

**Pass 2 — per-weapon loadout searches (this is where proper names live):**
for EVERY top-ranked weapon still missing a named build after the bfhub fetch,
run `"<weapon>" best loadout attachments Battlefield 6` — the search summaries
themselves usually return full builds (GameRant, Dexerto, Dot Esports,
Battlefinity, PCGamesN, fdaytalk). Battlefinity publishes **per-playstyle
builds** (close-range / versatile / mid-range) — capture all variants so the
app's playstyle switch changes builds visibly.

**Pass 3 — community pulse (user requirement 2026-07-06: not just "official"
sources):** at least one Reddit/social-flavored search per run (e.g. `reddit
REDSEC meta loadout settings`, include YouTube/TikTok results). This is what
surfaced the 1.3.1.0 controller-recoil nerf counter-tune and the BR-vs-Gauntlet
(plate count) meta split — flavor intel official sites don't carry. Label it
`COMMUNITY`.

**Controller settings need per-platform sources** — one generic guide is NOT
enough (user: "no one size fits all"): SCUF (PC/Xbox), a PS5/DualSense-specific
guide (thecontrollerpeople), and a REDSEC-specific preset (mitchcactus). The
app shows a different table per platform + a REDSEC override block. Record: patch version + date, buffs/nerfs,
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

Every weapon card carries a click-to-expand build. Priority order per weapon:

1. **Per-playstyle sourced builds** (best) — Battlefinity/fdaytalk style
   variants; the app picks the build matching the user's playstyle.
2. **Single sourced build** — used for all playstyles, labeled
   "one published build".
3. **Pattern pick** (`INFERRED`, names marked `*`) — assembled from attachment
   names that RECUR across this run's meta builds. Real names only — seen in
   sources this run — never fabricated. Unknowable weapon-specific slots
   (barrels) get generic phrasing ("Factory barrel*"). Optic follows playstyle.

After Pass 2, pattern picks should be the rare exception, not the norm — if a
top-3 weapon is still on a pattern build, say so in the chat summary.

**No ghost cards** (user feedback 2026-07-06): render only weapons that exist
in sources — a category with one sourced weapon shows one card, never
"NO DATA" placeholders. Fill thin categories with additional meta-tier weapons
from bfhub (ranks #4/#5, neutral chip) when available.

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
