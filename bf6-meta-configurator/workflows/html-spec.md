# App Spec — "NEON SIEGE" (since 2026-10-15)

The app is generated, not hand-written: `templates/template.html` holds the design and
logic, `scripts/build.py` injects the data. **Edit the template, never the output file.**
The previous "Field Ops Terminal" design (olive and phosphor green) is retired.

```
python scripts/build.py <weapons.json> <vehicles.json> <out.html> [<copy-to.html> ...]
```

`build.py` cleans visible copy on the way in (an em dash between clauses becomes a
period, a middot separator becomes a comma) and aborts if one survives. `stats` keep
their middot: the app splits them into chips on it.

## Concept

A tactical briefing on a Las Vegas casino floor after hours, anchored to the official
Season 5 ("Siege of Vegas") key art. Approved by Andrés on 2026-10-15 ("premium, close to
BF6, the new season's colors"). When a new season ships, re-measure the palette from that
season's key art (pixel sampling, see below) instead of keeping these values by inertia.

- **Palette, measured from the S5 key art pixels:** wine-black base `#160A11`, neon
  magenta `#BA4BC0` (light tint `#E07BE6`), lavender rail `#A381D1`, ember `#C15129`
  (UI `#E0612F`, core `#F7BA6C`), brass `#CA914A` (light `#E8BD7A`). Text `#F6ECF0`.
- **Type:** Tanker (Fontshare) for display, Khand (Fontshare) for UI, JetBrains Mono
  for data. None shared with luccatech.com (Panchang, General Sans) on purpose.
- **Signature:** opening a build rolls each attachment into place like a slot reel.
- **Field:** fixed WebGL canvas behind everything: drifting neon bokeh plus rising
  embers that dodge the pointer; a tap fires a muzzle-flash ring.
- **Rail:** the key art's vertical lavender strip, used as the scroll progress bar.

## Layout

Hero (oversized "META OPS", side intel block) → WEAPONS / VEHICLES tabs → controls
(mode, playstyle, class, platform; playstyle and class hide in VEHICLES) → collapsible
Season 5 briefing → sticky section index → ranked editorial rows (huge rank numerals,
not a card grid) → tuning → footer with disclaimer and a CLOSED sources drawer.

Vehicles view: tier ladder S/A/B/C, vehicle groups with per-seat loadouts (main and alt
build), counters (anti-vehicle Engineer + target list), vehicle controls.

## Support button (Andrés, 2026-10-15)

Two Ko-fi links are hard-coded in the template: "Buy me a coffee" in the hero side block
and "Keep the updates coming on Ko-fi" in the footer, both to `https://ko-fi.com/boogie8405`.
Buy Me a Coffee does not pay out in Colombia, so it was replaced by Ko-fi on PayPal.
Keep both links on every rebuild; change the URL only if Andrés gives a new one.

## Sources stay hidden but present (Andrés, 2026-10-15)

He wants a clean page with no visible source clutter. Attribution is still required,
because the app republishes other sites' builds. So:
- **No site names in visible copy** (`reason`, notes, settings reasons). Say "in the
  meta rankings", "in usage tracking", "by build curators" instead.
- Site names live only in `src`, `source`, `rankingSource`, `tierSource` and `sources`,
  which render inside small closed "Intel" disclosures and the footer drawer.
- Check before delivering: no site name in `document.body.innerText`.

## Motion rules (learned the hard way, 2026-10-15)

- **No `steps()` flicker.** Andrés found the stepped neon flicker too abrupt. Use
  interpolated easing, `cubic-bezier(.22,1,.36,1)` across the board.
- **Never let an end state depend on a transition or on requestAnimationFrame.**
  Expansion animates height in px, then a timer pins `height:auto`. Crossfades remove
  their class after a forced reflow and `setTimeout`, never rAF (rAF pauses in background
  tabs). Reveals have three independent exits: observer, frame loop, safety timer.
- Full `prefers-reduced-motion` branch: no reels, no reveals; the canvas keeps its single
  frame (`preserveDrawingBuffer`).

## Verify before delivering (headless Edge, no human needed)

**Method:** use `web-page-kit/docs/mobile-qa-headless.md` (iframe harness, overflow probe,
headless gotchas, animated-page rules). Do not rebuild the harness from scratch: on
2026-10-15 it was reinvented here because nobody searched the kit first. What follows are
only the BF6-specific assertions to run with it.

**Run them with the saved script** (it does all of the below and prints a verdict):

```
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify/verify-all.ps1 -Html "<path to bf6-meta-app.html>"
```

Expect the last line `VERDICT: PASS (9 of 9 runs, every expected check present)`. Any
`NO RESULT` is a FAIL, not a skip. Proven both ways on 2026-10-15: PASS on the live app,
FAIL when a site name was put back into a visible reason.

- Run the 4 combos (weapons and vehicles, MP and REDSEC) at desktop and 390 px. Expect:
  no JS errors, `scrollWidth == clientWidth`, 0 em dashes, 0 middots, 0 site names in
  visible text, no element left in `.pre`, row counts equal to the data.
- Click test: open a build (height > 0), switch tabs and mode (content changes, no zone
  left at `.out`).
