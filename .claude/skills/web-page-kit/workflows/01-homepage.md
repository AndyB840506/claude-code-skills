# Workflow 01 — Homepage: Hero + Core Sections

Create a professional homepage as a **single self-contained HTML file**. No external CSS files, no frameworks. Inline styles only (Google Fonts CDN is the one exception allowed).

> **No-Fabrication Rule:** Only use content the user explicitly provides. Mark missing info as `[PLACEHOLDER]`.  
> **Self-Contained Rule:** Output must be one `.html` file that works when opened directly in any browser.

See [docs/design-guide.md](../docs/design-guide.md) for animation patterns and visual design rules.

---

## Step 0: Load Config

**ACTION:** Read `website-config.json`. If missing → route to workflow 00-setup.

Extract: `site_name`, `site_type`, `tagline`, `description`, `primary_color`, `secondary_color`, `accent_color`, `owner_name`, `keywords`, `social_links`, `contact_email`.

---

## Step 1: Homepage Content

Ask in one message:

1. **Hero Headline** — The main statement visitors see first (e.g., "We build brands that stick")
2. **Hero Sub-headline** — Supporting line (e.g., "Strategy, identity, and web for bold businesses")
3. **Primary CTA Text** — Button text (e.g., "Work With Us", "View My Work", "Subscribe")
4. **Secondary CTA** *(optional)* — Second action (e.g., "See our work", "Learn more")

---

## Step 2: Hero Visual

**If `site_type` is `scroll`:** The scroll-video hero is automatically selected. Ask:
1. **Video file** — Path or URL to your hero video (MP4). No video? I'll use a cinematic gradient hero instead.
2. **Scroll speed** — Fast (300vh), Medium (500vh), Slow/cinematic (700vh)?

**For all other site types:** Ask:
1. **Background style** — Solid color, gradient, image, or pattern?
2. **Profile/Logo image** — Path or URL, or use CSS placeholder (initials + brand color)
3. **Hero height** — Full-screen, large, or standard

**Premium option (any site type):**
> "Want a cinematic scroll-video hero? (requires a video file)"
> If YES → collect video path + scroll speed → use scroll-video pattern from [docs/design-guide.md Rule 11](../docs/design-guide.md)
> If NO → standard hero

---

## Step 3: Sections to Include

Ask based on `site_type` from config — suggest relevant defaults:

| Site Type | Suggested Sections |
|---|---|
| Business | About, Services, Testimonials, Contact |
| Portfolio | About, Work/Projects, Skills, Contact |
| Blog | About, Recent Posts, Categories, Newsletter |
| E-commerce | Featured Products, Benefits, Reviews, CTA |
| Events | Upcoming Events, Speakers/Lineup, Schedule, Register |
| Podcast | About Show, Latest Episodes, Subscribe, Host |
| Personal Brand | Story, Services/Content, Social Proof, Contact |

User confirms or adjusts the list.

---

## Step 4: Conditional Sections by Site Type

Based on confirmed site type:

**B2B / Professional / Business:**
- Include **Career/Credibility Timeline** — Only if user provides real milestones. Each entry: year + achievement. Never invent.

**E-commerce:**
- Include **Product Grid** — Up to 6 featured products. Need: name, price (or price range), image path/placeholder.

**Events:**
- Include **Countdown Timer** — To event date. Need: actual event date.

**Blog:**
- Include **Recent Posts Preview** — 3 most recent. Need: titles + short descriptions.

**Podcast:**
- Include **Episode List/Player** — 3 featured episodes. Need: titles + platform links.

Ask only for the sections relevant to the site type.

---

## Step 5: Generate Homepage HTML

**FIRST — apply Rule 0 from [docs/design-guide.md](../docs/design-guide.md):** commit to a concept (tone + layout *architecture* + one signature idea), anchored to ONE real reference, BEFORE writing any HTML. The elements below are building blocks — the concept decides which appear and how they look. Do **not** emit the default skeleton (centered hero + 3 cards + alternating backgrounds + ring + parallax + counters) by reflex; that is a generic-page fail.

**ACTION:** Generate a complete `homepage.html` that expresses the chosen concept:

### Building blocks (the concept decides which to use and how they look):

**Navigation:**
- Fixed top navbar
- Logo/name + nav links
- On scroll: blur + semi-transparent background
- Mobile hamburger menu

**Hero Section:**
- Headline (H1) + sub-headline + CTA button(s)
- Background (from user choice)
- Profile photo or brand mark (the rotating gradient ring in Rule 9 is OPT-IN — only if it genuinely fits the concept)
- Immediately visible stats/highlights only if user provided them

**Core Sections** (from Step 3 confirmed list):
- Each section semantically structured with proper headings
- Section rhythm driven by the concept — vary type scale, full-bleed vs contained, dark/light breaks. Avoid the reflexive white / grey / white alternation.

**Conditional Section** (from Step 4):
- Only include if user provided the required data

**Footer:**
- Site name + tagline
- Navigation links
- Social media links (from config)
- Contact email
- Copyright year (auto-set with JS: `new Date().getFullYear()`)

### Technical Requirements:

- Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- All CSS inline in `<style>` tag (no external `.css` files)
- Google Fonts only CDN import allowed
- Mobile-responsive with CSS media queries
- Open Graph meta tags (title, description, image placeholder, url)
- Schema.org structured data matching `site_type`
- Scroll reveal animations via Intersection Observer (no libraries — see design-guide.md Rules 2-3)
- Hover effects on cards and buttons (Rule 6)
- Counter animation for stats — OPT-IN, only if the concept actually uses stats (Rule 4)
- Parallax / scroll-driven motion — OPT-IN, only when it serves the concept (Rule 5)
- Passive scroll listeners `{ passive: true }` (Rule 13)
- `@media (prefers-reduced-motion: reduce)` block — disables all animations (Rule 12)
- WCAG AA contrast, 16px min font, visible focus states, semantic HTML (Rule 14)

**Filename:** `homepage.html`

---

## Step 6: Auto-Open

**ACTION:** After saving, open the file in the default browser:

```powershell
Start-Process "homepage.html"
```

Or on Mac/Linux:
```bash
open homepage.html
```

---

## Step 7: Review & Data Sources

Show:
```
✅ Homepage generated: homepage.html

Sections included: [list]
Data sources:
- Hero headline: user-provided
- Profile photo: [path or CSS placeholder]
- Services: user-provided
- Testimonials: [user-provided / placeholder — add real ones later]

⚠️ Placeholders: [list any [PLACEHOLDER] items that need real content]

Want to adjust anything?
```

Ask: "Ready to publish?" → If yes, proceed to `workflows/05-deployment.md`.

---

**Homepage complete.** Single file, works offline, ready to deploy.
