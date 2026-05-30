---
name: bf6-meta-configurator
description: "Weapon meta configurator for Battlefield 6. Auto-fetches developer patch notes, analyzes buffs and nerfs, and generates a Top 3 weapons per category with optimal attachment loadouts plus controller settings tuned for low recoil and high TTK/DPS. Outputs a mobile-friendly HTML report that opens in the browser. Short triggers: bf6, BF6, battlefield, battlefield 6. Triggers (ES): meta bf6, armas meta battlefield 6, mejor arma bf6, build armas battlefield, attachments meta bf6, configurar control bf6, top armas battlefield 6, tier list armas bf6, configuración control battlefield, qué arma usar en bf6, mejores armas bf6. Triggers (EN): weapon meta bf6, best gun bf6, bf6 meta loadout, battlefield 6 best weapons, bf6 attachment build, bf6 controller settings, top guns battlefield 6, bf6 tier list, best class bf6, battlefield 6 weapon guide."
---

# BF6 Meta Configurator

Auto-fetches Battlefield 6 patch notes, ranks weapons by current meta (TTK · DPS · recoil), and delivers a Top 3 per category with full attachment lists plus controller settings — as a mobile-ready HTML report.

**Core rule: never invent weapon stats or attachment names. Only use data found in patch notes or verified community sources. When uncertain, mark it explicitly.**

---

## Step 0 — Language Selection + Preferences

### Step 0.1 — Ask language (always in both languages simultaneously)

No matter what language the user used to invoke the skill, respond with this exact bilingual message:

> What language do you prefer? / ¿En qué idioma prefieres continuar?
>
> 🇬🇧 **English** · 🇪🇸 **Español**

Accept any short answer: "English", "EN", "inglés", "español", "ES", "1", "2", etc.
Default to English if the response is unclear.

### Step 0.2 — Ask preferences (in the chosen language, single block)

**MANDATORY: Send ALL 3 questions in a single message. Do NOT send the message without all 3 included. Do NOT advance to Step 1 until the user answers all 3 — or explicitly says to use defaults.**

**If English:**
> Ready to build your BF6 meta! Before I fetch the latest patch notes, I need 3 quick answers:
>
> 1. **Platform** — PS5 (DualSense) or Xbox / PC gamepad?
> 2. **Preferred class** — All classes (default), Assault, Support, Engineer, or Recon?
> 3. **Playstyle** — Versatile (default), Aggressive (CQC), or Long Range?
>
> Reply with all 3 — or just say "defaults" and I'll use: All classes · Versatile.

**If Spanish:**
> ¡Listo para armar el meta de BF6! Antes de buscar los últimos cambios, necesito 3 respuestas rápidas:
>
> 1. **Plataforma** — PS5 (DualSense) o Xbox / PC con mando?
> 2. **Clase favorita** — Todas (default), Asalto, Soporte, Ingeniero, o Reconocimiento?
> 3. **Estilo de juego** — Versátil (default), Agresivo (CQC), o Largo alcance?
>
> Responde las 3 — o escribe "defaults" y uso: Todas las clases · Versátil.

**Rules:**
- Wait for the user to answer ALL 3 before proceeding to Step 1 — no exceptions
- Defaults if explicitly skipped: Class = All, Playstyle = Versatile
- Accept shorthand: "PS5, all, versatile" counts as 3 answers
- Use the chosen language for ALL subsequent steps, messages, and the chat summary

---

## Step 1 — Auto-fetch Patch Notes

Announce: `"Searching latest BF6 patch notes... 🔍"`

Run **WebSearch** sequentially with these queries (stop when you find solid results):

1. `"Battlefield 6" patch notes weapon balance 2026 site:ea.com OR site:battlefield.com`
2. `"Battlefield 6" developer update weapon buff nerf 2026`
3. `BF6 weapon meta update 2026 Reddit OR YouTube`
4. `"BF6" OR "Battlefield 6" weapon stats tier list 2026`

For each promising URL, use **WebFetch** to read the actual content.

**Identify and record:**
- Patch/update version and date
- Weapons buffed (damage ↑, recoil ↓, ADS speed ↑, etc.)
- Weapons nerfed (damage ↓, recoil ↑, mag size ↓, etc.)
- Any attachment changes
- Source URL(s)

**Fallback — if no official patch notes found:**
Inform the user clearly:
> "No official patch notes found yet. Using beta/alpha data and community consensus as the basis — treat recommendations as provisional."

Continue with whatever verified data was found. Never block or fail silently.

### Pass 2 — Per-weapon deep stats search

After finding patch notes, run targeted searches for every weapon in the Top 3 candidates that has no confirmed attachment data. For each such weapon:

1. `battlefieldlabs "bf6" "[weapon name]" attachments stats`
2. `site:reddit.com "Battlefield 6" "[weapon name]" best attachments 2026`
3. `"[weapon name]" battlefield 6 meta loadout build 2026`

WebFetch any promising URL and extract attachment names, TTK, DPS.

**Source confidence tiers:**
- `CONFIRMED` — data from official patch notes, battlefieldlabs, or 2+ independent verified sources
- `COMMUNITY` — data from 1 community source (forum post, YouTube creator breakdown)
- `INFERRED` — no external source; built from attachment effect logic in Step 2

Track the tier for every weapon's attachment data. Never leave a slot empty.

---

## Step 2 — Analyze & Rank Weapons

For each weapon category present in BF6 (use only categories confirmed by sources — typically: Assault Rifle, SMG, LMG, Sniper Rifle, Marksman/DMR, Shotgun, Sidearm):

### Ranking criteria (apply in order):

1. **Recent buffs** → significant upward push in ranking
2. **Recent nerfs** → downward push
3. **TTK** (Time to Kill in ms at optimal range) — lower = better
4. **DPS** (Damage per Second) — higher = better
5. **Recoil control** — lower = better for meta (especially with controller)
6. **ADS speed** (ms) — lower = better for reaction fights

### For each Top 3 weapon in a category, collect:

- Weapon name
- Why it ranks here (1 sentence — e.g., "Buffed in v1.4 — now best TTK in AR class")
- Estimated TTK at optimal range (if found in sources, otherwise omit)
- Estimated DPS (if available)
- **Full attachment loadout:**
  - Muzzle
  - Barrel
  - Optic (adapt to playstyle: CQC → red dot / holo; Versatile → 2-3x; Long Range → 4x+)
  - Stock / Underbarrel
  - Magazine
  - Specialty / Perk (if BF6 has this slot)

**NEVER leave an attachment slot as TBD.** If no source confirms the attachment, apply the inference algorithm below.

### Attachment Inference Algorithm (use when source data is missing)

1. **Identify weapon archetype** from known stats or category:
   - High RPM (>700) / lower damage → priority: recoil control + mag size
   - Low RPM (<500) / high damage → priority: range + first-shot accuracy
   - Mid RPM + mid damage → priority: balanced recoil + ADS speed

2. **Apply slot-by-slot meta logic:**
   - **Muzzle**: Choose suppressor variant with lowest recoil penalty (silence + stability). If no suppressor available, choose muzzle brake (recoil reduction only).
   - **Barrel**: For high-RPM → lightweight barrel (faster ADS, accept slight range loss). For high-damage/slow RPM → extended barrel (range + accuracy). For new/unknown → standard barrel (neutral).
   - **Optic**: Match to playstyle from Step 0: Aggressive → 1x red dot / holo; Versatile → 2–3x variable; Long Range → 4x+.
   - **Underbarrel**: Vertical foregrip → reduces vertical recoil (default for high-RPM). Angled foregrip → reduces first-shot recoil (default for burst/semi). None if weight penalty is too high.
   - **Magazine**: Largest capacity available that doesn't exceed 20% ADS speed penalty. For SMG: extended mag. For AR: fast mag variant if TTK is already good.
   - **Ammo**: FMJ (general versatility, default). Hollow Point if playstyle = Aggressive (CQC).

3. **Write the inferred attachment name as best-guess based on BF6 naming conventions** seen in other weapons (e.g., "LIGHTENED SUPPRESSOR", "EXTENDED BARREL", "VERTICAL GRIP"). Add `*` suffix to indicate it's inferred: e.g., `LIGHTENED SUPPRESSOR*`.

4. **Mark the weapon's data source badge** as `INFERRED` in the HTML output.

---

## Step 3 — Controller Settings

Generate recommended settings based on the platform selected in Step 0.

### Guiding principles (non-negotiable):
- **Priority 1:** Recoil control — settings that let you stay on target through full-auto bursts
- **Priority 2:** Fast TTK — high enough sensitivity to track moving targets
- **Priority 3:** Fast ADS — quick enough to react to flanks

Before generating settings, search for the exact BF6 in-game menu paths:
`"Battlefield 6" controller settings menu location 2026`
WebFetch any official or community guide that shows the Settings navigation structure.

### PS5 — DualSense Settings

Output as a 4-column table in the HTML: **Setting | Value | Reason | Where to find it**

| Parameter | Recommended Value | Reason | Where to find it |
|---|---|---|---|
| Look Sensitivity (H/V) | 5–6 / 5–6 | Balanced tracking without overshooting | Settings → Controls → Controller → Look Sensitivity |
| ADS Sensitivity Multiplier | 0.70–0.80 | Slows aim when scoped for precision | Settings → Controls → Controller → ADS Sens. Multiplier |
| Deadzone (Left stick) | 0.05–0.08 | Eliminates drift without dead feel | Settings → Controls → Controller → Left Stick Deadzone |
| Deadzone (Right stick) | 0.05–0.08 | Same as above | Settings → Controls → Controller → Right Stick Deadzone |
| Aim Acceleration | Off or minimum | Predictable, linear response | Settings → Controls → Controller → Aim Acceleration |
| Aim Curve | Linear | Consistent 1:1 input-to-output | Settings → Controls → Controller → Aim Response Curve |
| Adaptive Triggers | Resistance on fire (if supported) | Tactile feedback | Settings → Accessibility → Adaptive Triggers |
| Vibration | Light or Off | Reduces distraction during sustained fire | Settings → Controls → Controller → Vibration Intensity |

> Note: Verify exact menu paths in-game — these reflect standard BF game layout. Adjust if BF6 differs. Fine-tune in the shooting range.

### Xbox / PC Gamepad Settings

Output as a 4-column table in the HTML: **Setting | Value | Reason | Where to find it**

| Parameter | Recommended Value | Reason | Where to find it |
|---|---|---|---|
| Look Sensitivity (H/V) | 5–6 / 5–6 | Balanced tracking | Settings → Controls → Controller → Look Sensitivity |
| ADS Multiplier | 0.75 | Precision while aiming | Settings → Controls → Controller → ADS Sens. Multiplier |
| Inner Deadzone | 0.05 | Minimal drift compensation | Settings → Controls → Controller → Inner Deadzone |
| Outer Deadzone | 0.00 | Full range of motion | Settings → Controls → Controller → Outer Deadzone |
| Trigger Sensitivity | High (or Max) | Faster fire response | Settings → Controls → Controller → Trigger Deadzone |
| Aim Assist Mode | Rotation + Slow (if available) | Rotational assist + no snap | Settings → Controls → Controller → Aim Assist Type |
| Aim Curve | Linear | Predictable feel | Settings → Controls → Controller → Aim Response Curve |

> Note: If exact menu path was found via WebSearch, use that instead. These are BF-series defaults — verify in BF6.

---

## Step 4 — Generate HTML Report

Build the complete HTML as a single self-contained file.

**Filename:** `bf6-meta-YYYY-MM-DD.html` (use today's actual date)

**Design direction:**
Dark military UI. Think tactical HUD — not gaming-flashy. Deep dark background, tactical green or teal accents, high-contrast white/light text, rank badges in gold/silver/bronze. Clean sans-serif font — system font or Google Fonts loaded from CDN. Express the feel of a real battlefield operations screen. Color choices are yours — prioritize readability and contrast over decoration.

**Structure the HTML as follows:**

### 1. Embed a JSON data block

Inside a `<script id="meta-data" type="application/json">` tag, embed all the meta data as structured JSON:

```json
{
  "generated": "YYYY-MM-DD",
  "patchSource": "URL or 'Community consensus'",
  "patchDate": "YYYY-MM-DD or 'Unknown'",
  "platform": "PS5 | Xbox",
  "playstyle": "Aggressive | Versatile | Long Range",
  "weapons": {
    "AssaultRifle": [
      {
        "rank": 1,
        "name": "WeaponName",
        "reason": "Why top 3",
        "ttk": "250ms",
        "dps": "180",
        "dataSource": "CONFIRMED | COMMUNITY | INFERRED | PENDING",
        "attachments": {
          "muzzle": "...",
          "barrel": "...",
          "optic": "...",
          "stock": "...",
          "magazine": "...",
          "specialty": "..."
        },
        "attachmentSource": "CONFIRMED | COMMUNITY | INFERRED"
      }
    ]
  },
  "controllerSettings": {
    "lookSensitivity": "5/5",
    "adsMul": "0.75",
    "deadzoneLeft": "0.06",
    "deadzoneRight": "0.06"
  }
}
```

This JSON block is what makes the report portable for a future mobile app — the app can simply fetch and parse this data.

### 2. Header
- Title: `BF6 META REPORT`
- Subtitle: Platform | Playstyle | Date generated
- Patch source badge (green if official, amber if community)

### 3. Weapon Sections (one per category)
Use tabs or an accordion (JavaScript, no external library needed). For each category:
- Category label (e.g., `ASSAULT RIFLES`)
- 3 weapon cards side by side on desktop, stacked on mobile
- Each card:
  - Rank badge (#1 gold, #2 silver, #3 bronze)
  - **Data source badge** (top-right corner of card):
    - `✓ CONFIRMED` — green — official patch notes or 2+ verified sources
    - `⚙ COMMUNITY` — blue — 1 community source (forum, YouTube)
    - `◈ INFERRED` — amber — built from attachment logic, no external source
    - `⏳ PENDING` — grey — weapon not yet released, no data available
  - Weapon name + reason line + TTK/DPS stats if available
  - Attachment table — slots marked with `*` are inferred (show tooltip or small note)

### 4. Controller Settings Section
Four-column table: **Setting | Value | Reason | Where to find it**.
On mobile, collapse the Reason column (hide via CSS `display:none` at small breakpoint, keep Setting + Value + Location visible).
Add note below table: "Verify paths in-game — may vary by platform build."

### 5. Sources Footer
List every URL fetched, with date accessed.

**Mobile-first CSS requirements:**
- All layouts use CSS Grid or Flexbox with `flex-wrap: wrap`
- Cards: `min-width: 280px`, grow to fill
- Font sizes in `rem`, not `px`
- Viewport meta tag included
- No fixed widths that break on small screens

**Open the file automatically after writing:**

```powershell
Start-Process "bf6-meta-YYYY-MM-DD.html"
```

Or via Bash:

```bash
start bf6-meta-YYYY-MM-DD.html
```

---

## Step 5 — Chat Summary

After the HTML opens, show a compact summary in the chat:

```
✓ Report opened: bf6-meta-[date].html
✓ Source: [patch source + date]
✓ Platform: [PS5 / Xbox]
✓ Categories covered: [list]

Top #1 per category:
  AR  → [weapon name]
  SMG → [weapon name]
  LMG → [weapon name]
  ...

Want to filter by class, adjust playstyle, or drill into a specific weapon?
```

If using Spanish, mirror the summary in Spanish.

---

## Re-run Behavior

This skill is designed to be re-run any time. Each run:
1. Does a fresh WebSearch for patch notes (catches new updates)
2. Re-ranks weapons based on latest data
3. Generates a new HTML file with today's date (previous files are kept)

The JSON data block inside the HTML makes each report a standalone snapshot — useful for tracking meta evolution over time and as the data layer for a future Android/iOS app.
