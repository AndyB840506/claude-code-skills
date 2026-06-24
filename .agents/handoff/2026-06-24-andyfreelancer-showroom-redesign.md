# Handoff: Andyfreelancer Showroom Redesign + BTQ Premium Polish

**Date:** 2026-06-24
**Status:** In progress — showroom homepage built as preview (not live); other pages pending

---

## What We Accomplished This Session

**BTQ premium liner-notes page**
- Made the reactive background global (not hero-only), added click/tap feedback, prioritized touch fluidity.
- Captured the winning pattern into web-page-kit as a reusable **TECHNIQUE** (Rule 18), not a copy-paste look.
- Wired Canva key visuals: `og-image.png`, `btq-episodio-social.png`. Committed `95040c3`.

**Andyfreelancer.com ultra-premium redesign**
- Concept locked after ~13 iterations: **boutique-showroom that sells experiences, not products**. NOT pure engineering — that framing is reserved for the separate **Lucca Tech** brand.
- Visual system: charcoal `#0e1113` + brand red `#ff3d00` (logo-dominant) + cream `#f4efe7`; Fontshare **Cabinet Grotesk + Supreme + Martian Mono**.
- Signature element: **interactive SVG world map** background — full world, every country glows red + shows its name on hover/tap. Real Natural Earth geometry (world-atlas + d3-geo + topojson-client), `preserveAspectRatio="…meet"` (no crop), `position:fixed` + gentle GSAP scroll-pan.
- Built into `C:\Users\andre\repos\the-freelancer\one-pager\index-showroom.html`. Committed `ede1b74` to **master**.

**Session-close retrospective (this kit)**
- `web-page-kit/docs/design-guide.md`: added Rule 0 banned AI-tells (big-number stat row, em-dash overuse) + new Rule 18 subsection "Full-bleed reactive background — gotchas". Committed `1f1cedf`.
- Created 2 memory files: `feedback_named_concept_drives_render`, `project_andyfreelancer_redesign` + MEMORY.md index lines.

---

## Where We Paused

**Last action:** Committed retrospective edits to design-guide.md (`1f1cedf`); writing this handoff.
**Next action:** Continue redesigning the OTHER andyfreelancer pages in the same showroom direction (world-map field, same type/colors). Confirm with Andrés which page is next in the list.
**Blockers:** None. `index-showroom.html` is a **preview/demo file — NOT live**; production `index.html` is unchanged.

---

## Files to Read First
- `C:\Users\andre\repos\the-freelancer\one-pager\index-showroom.html` — the showroom WIP homepage (preview, not live)
- `c:\Users\andre\.claude\skills\.claude\skills\web-page-kit\docs\design-guide.md` — Rule 0, Rule 18 + new "Full-bleed reactive background — gotchas" subsection
- Memory: `project_andyfreelancer_redesign.md`, `feedback_named_concept_drives_render.md`

---

## Notes / Gotchas
- `index-showroom.html` preserves the original site's EN/ES/PT i18n (`setLang`), `/contact` form POST, `/widget.js`, and schema.org — keep these on every new page.
- DO App Platform auto-deploys on push to **master** (the-freelancer). The showroom is committed but does NOT change the live homepage until `index-showroom.html` is swapped to `index.html`.
- Do NOT clone the BTQ look onto Andyfreelancer — Rule 18 is a technique tier; re-run Rule 0 per page. The world map is Andyfreelancer's own field, not BTQ's gold shader.
- Apply the security hardening baseline to Andyfreelancer pages too (memory: security baseline for client sites).

---

## Questions to Answer
- Which andyfreelancer page is next in the list to redesign?
- Is the showroom homepage approved to swap `index-showroom.html` → `index.html` and deploy, or keep iterating first?
