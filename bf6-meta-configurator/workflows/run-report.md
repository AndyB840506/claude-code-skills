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

**Two traps found 2026-10-15:**
- **bfhub's page header date ("updated Oct 15, 2026") is NOT the build date.** Each loadout
  carries its own date (in 2026 they were still Oct–Nov 2025). Label builds with the entry
  date ("build dated 2025"), never with the page date: the July run did the opposite.
- **Near-identical names are different weapons:** RPK-74M and RPKM are separate LMGs
  (wzstats lists both). The July data gave the RPK-74M a build bfhub publishes for the
  RPKM. Match the exact name string before attaching a build to a weapon.

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

**Pass 4, vehicles (added 2026-10-15):** builds per seat (bftactics.com/vehicle-builds is
the bulk source, GameRant as alt), EA's vehicle page for the roster and NATO/PAX names,
a vehicle tier list (Timesaver), counters (Switchblade, Timesaver anti-vehicle), and
vehicle control settings (Dexerto, Overgear, GameRant). Read every vehicle line of the
current patch notes and attach it to the vehicle it touches. **REDSEC roster:** as of
2026-10-15 EA only says which vehicles are NOT in REDSEC (Mobile AA, Attack Helicopter,
Attack Jet, Fighter Jet). Never list a vehicle as in REDSEC without a source saying so.

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

Write the data as two files in `<drive>:\Claude Output\bf6\data\` (`E:` desktop, `D:`
laptop): `weapons.json` (generated, patch, modes, patternBuild, controllerSettings,
sources) and `vehicles.json` (tiers, s5Changes, groups, counters, controls, sources).
Open the previous copies first: they are the baseline for "what changed". The schema is
whatever `templates/template.html` reads; copy the shape of the previous files.

Before building, update the site repo, because the build writes into it:
`git -C C:\Users\andre\repos\lucca-tech-web pull --ff-only origin master`. If it is not a
fast-forward, stop and sort it out first: never build on top of a stale clone.

Then build, following [html-spec.md](html-spec.md) for copy and verification rules:

```
python scripts/build.py data\weapons.json data\vehicles.json "<drive>:\Claude Output\bf6\bf6-meta-app.html" "C:\Users\andre\repos\lucca-tech-web\bf6\index.html"
```

**Stable path, same file every time** (the user's bookmark must keep working). Run the
html-spec verification, then open it: `Start-Process "<path>"`.

## Step 4b — Publish to luccatech.com/bf6/ (only with the user's OK)

The public copy lives in `repos\lucca-tech-web\bf6\index.html` (build.py already wrote
it; Step 4 already pulled the repo). Then: `node build.js` (refreshes sitemap lastmod), commit,
run the `deploy-preflight` skill, and deploy by hand with Vercel (prebuilt; recipe in the
Lucca Tech memory). Verify the live page with `curl -sL` against the local file.

## Step 5 — Chat summary (compact, user's language)

```
✓ App actualizada: <path> (abierta)
✓ Parche: <version + fecha> · datos de hoy
✓ Cambios vs datos anteriores: <top movers / "primer llenado">

#1 por categoría — MP:      #1 por categoría — REDSEC:
  AR  → <arma>                AR  → <arma>
  SMG → <arma>                ...
Vehículos: <cambios del parche que mueven la tier list>
Publicado en luccatech.com/bf6/: <sí, verificado en vivo / no, pendiente de OK>
```
