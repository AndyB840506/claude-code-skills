# Run Report — main flow

## Step 0 — Setup (ONE menu, no ping-pong)

Detect language from the user's invoking message (Spanish message → todo en
español; English → English). Never ask which language.

**If `last-run.json` exists** in the skill folder, first offer a one-tap rerun
via `AskUserQuestion` (single question): "¿Usar tu última config? — {platform} ·
{mode} · {class} · {playstyle}" with options **Sí, igual** / **Cambiar algo**.
If "Sí" → skip straight to Step 1.

**Full menu** (first run, or "Cambiar algo"): ONE `AskUserQuestion` call with
all 4 questions:

1. **Platform** — PS5 (DualSense) / Xbox / PC gamepad
2. **Mode** — Multiplayer / REDSEC (battle royale) / Both *(default: Both)*
3. **Class** — All (default) / Assault / Engineer / Support / Recon
4. **Playstyle** — Versatile (default) / Aggressive (CQC) / Long Range

After the run completes, write the four answers + date to `last-run.json`.

## Step 1 — Fresh data sweep (parallel, capped)

Announce briefly ("Buscando el meta del parche actual… 🔍"), then run the
searches **in parallel** (multiple WebSearch calls in one message — not
sequentially). Use the CURRENT month/year in queries:

- `"Battlefield 6" patch notes weapon balance <month year>` (+ site:ea.com variant)
- `Battlefield 6 weapon meta tier list <month year>` (skip if mode = REDSEC only)
- `REDSEC battlefield meta best weapons loadout <month year>` (skip if mode = MP only)
- `Battlefield 6 best controller settings aim deadzone <month year>`

Then WebFetch the most promising URLs — **max 8 fetches total**. Prefer sources
that show a publish/update date. Record: patch version + date, buffs/nerfs,
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
2. **Generic effect recommendation** (`INFERRED` badge) — no source → describe
   the effect to pick, e.g. "supresor con menor penalización de retroceso que
   tengas desbloqueado", "mira 1x (red dot/holo) por tu estilo CQC". NEVER
   fabricate a proper name.
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

## Step 4 — HTML report

Follow [html-spec.md](html-spec.md). Filename `bf6-meta-YYYY-MM-DD.html`, saved
to `E:\Claude Output\bf6\` (desktop) or `D:\Claude Output\bf6\` (laptop) —
create the folder if missing, detect which drive exists. Open it:
`Start-Process "<path>"` (PowerShell). Old reports are kept.

## Step 5 — Chat summary (compact, user's language)

```
✓ Reporte: <path> (abierto)
✓ Fuente: <patch/source + fecha> [STALE si aplica]
✓ Setup: <platform · mode · class · playstyle>

#1 por categoría — MP:      #1 por categoría — REDSEC:
  AR  → <arma>                AR  → <arma>
  SMG → <arma>                ...

¿Filtrar por clase, cambiar estilo, o profundizar en un arma?
```
