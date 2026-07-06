# App Spec — "Field Ops Terminal" (interactive)

One self-contained file (inline CSS/JS, Google Fonts CDN allowed). The named
concept is **Field Ops Terminal**: a military intel console rendering a live
briefing — not a gamer landing page. If it looks like a generic dark dashboard
with three cards, it's wrong.

**It is an APP, not a report** (user decision 2026-07-06): a controls row at
the top — Mode (MP/REDSEC) · Playstyle · Class filter · Platform — as tactical
segmented buttons; every choice re-renders client-side from the embedded JSON
and persists in `localStorage` (key `bf6ops`). Playstyle switches the optic on
pattern-pick builds; platform filters the controller-settings rows; class
filter hides non-matching weapon categories. A data-age chip in the header
computes age from the JSON `generated` date and self-marks **STALE — RE-RUN THE
SKILL** past 60 days. All copy in English.

## Banned (generic-AI tells)

Centered hero + 3 equal cards, purple/blue gradients, glassmorphism, rounded
pill buttons everywhere, Inter/system-default headers, emoji as icons,
decorative progress rings.

## Art direction

- **Palette:** near-black olive `#0C0F0A` base; panel `#141A12`; primary accent
  phosphor green `#9FE870`; secondary amber `#E8B44F` (warnings/INFERRED);
  alert red `#E85D4F` (nerfs/STALE); text `#E8EDE4`; muted `#7A8471`.
  Rank chips: gold `#D4AF37` / silver `#B8BDC4` / bronze `#B08D57`.
- **Type:** headers **Barlow Condensed** (700, uppercase, tracked +4%); data &
  numbers **IBM Plex Mono**; body **Barlow**. Sizes in `rem`.
- **Texture:** 1px scanline overlay at ~3% opacity + faint dot-grid on panels.
  Thin 1px borders with clipped corners (CSS `clip-path` notch on one corner)
  instead of big border-radius — console panels, not app cards.
- **Motion:** subtle only — section reveal (translateY 8px + fade), a one-time
  "boot" flicker on the header. No parallax, no floating blobs.

## Layout

1. **Header bar** — `BF6 // META REPORT` + mono meta-line: patch, date,
   platform, playstyle. STALE banner here when applicable (amber, full-width).
2. **Mode switch** — MP / REDSEC as two tactical tabs (only if both requested).
   Persist choice with a `data-` attribute; no library.
3. **Category nav** — sticky horizontal strip of mono chips (AR · SMG · LMG …)
   that scroll-jump to sections.
4. **Weapon cards** — per category, 3 cards in `grid-template-columns:
   repeat(auto-fit, minmax(280px, 1fr))`. Card anatomy: rank chip top-left,
   source badge top-right (`✓ CONFIRMED` green / `⚙ COMMUNITY` blue /
   `◈ INFERRED` amber / `NO DATA` gray / `STALE` red-outline), weapon name in
   condensed caps, one-line reason, TTK/DPS as mono stat pair, and a
   **"LOADOUT ▸" affordance: clicking the card expands the full attachment
   loadout in place** (accordion; slot | attachment name | build source line
   with its own badge + date). Pattern-pick names carry `*` and render amber.
   No cell is ever empty — see run-report.md's contract. All report copy in
   English.
5. **Controller settings** — 5-column table (Setting | Value | Reason | Where |
   Source). On ≤480px hide "Reason" (`display:none`), keep the rest. Rows that
   changed this patch get a green left-border.
6. **Sources footer** — every URL + access date, mono, small.

## Data block

Keep the `<script id="meta-data" type="application/json">` snapshot (generated
date, patch, platform, playstyle, per-mode weapons with attachments + tiers,
controller settings). It is the data layer for a future companion app.

## Mobile-first checks (before delivering)

Viewport meta present; no fixed widths; cards stack at 280px; tables inside
`overflow-x:auto` wrappers; tap targets ≥44px; text ≥14px equivalent. Verify by
resizing logic mentally against 360px width — if a table would overflow the
viewport without its scroll wrapper, fix it before writing the file.
