# Workflow 00 — Import: Analyze & Adapt Existing Website

Take any existing website design you like and adapt it to your brand. Analyze colors, layout, and structure — then regenerate with YOUR content.

> **No-Fabrication Rule:** Don't carry over the original site's content. Replace everything with real data from the user.

---

## Step -1: Context Check

**If called from `00-welcome.md`:** `site_type` and `language` are already set. Skip Step 3 (site info questions that duplicate setup) if config already exists.

**If called directly:** Note language from config (`language: "en"` or `"es"`). Use that language throughout.

---

## Step 0: What This Does & Target URL

> "Give me a URL of any website you like — a competitor, a template, anything. I'll analyze the design, extract the style, and recreate it with YOUR content and brand.
>
> You keep the look and feel. Everything else becomes yours."

Ask:

1. **Website URL** — Which site to import? (full URL)
2. **What do you like about it?** — Design? Layout? Colors? Sections?

**ACTION:** Fetch using WebFetch. Analyze HTML and CSS.

---

## Step 1: Design Extraction

**ACTION:** Extract and report:

- **Colors** — Primary, secondary, accent (from CSS or visual inspection)
- **Typography** — Font families and sizes used
- **Layout Style** — Hero type, grid layout, single-column, multi-column
- **Navigation** — Top bar, sidebar, hamburger, sticky?
- **Sections Found** — List all major sections on the page
- **Design Vibe** — Minimal, bold, playful, corporate, editorial, etc.
- **Animation patterns** — Any visible scroll effects or transitions

Show findings:
```
✅ Design Analysis

Colors:
  Primary: #1A1A1A (dark charcoal)
  Secondary: #F5F5F5 (light grey)
  Accent: #FF6B35 (orange)

Fonts: "Inter" + "Playfair Display"
Layout: Full-width hero, 3-column features, 2-column about
Style: Modern, minimal, professional

Sections: Hero → Features → About → Testimonials → CTA → Footer
Animations: Fade-in on scroll, hover lift on cards
```

---

## Step 2: What to Keep vs. Replace

Ask:

1. **Keep colors?** — Use extracted colors, or provide your own?
2. **Keep layout?** — Same section structure, or adjust?
3. **Keep fonts?** — Same typography, or specify yours?
4. **Remove any sections?** — Anything that doesn't apply?
5. **Add any sections?** — Anything missing for your site?

---

## Step 3: Your Site Information

Ask for the user's actual content (run Step 1 from workflow 00-setup if no config exists):

1. **Site/Business Name**
2. **Tagline**
3. **Description**
4. **Site Type** — business | portfolio | blog | ecommerce | events | podcast | personal
5. **Owner Name** *(optional)*
6. **Keywords** — 5-7 SEO terms
7. **Social links** — relevant platforms

**ACTION:** Create or update `website-config.json` with `import_source` set to the analyzed URL.

---

## Step 4: Section Content Mapping

For each section being kept, collect real content:

**Hero:**
- Headline, sub-headline, CTA button text

**Features/Services/Benefits:**
- 3-6 real items the user provides. Each: title + description. Never invent.

**About:**
- User's own bio or company description

**Testimonials:**
- Real testimonials only. If none available: skip section or mark as `[Add testimonials here]`

**CTA Section:**
- What action? (book, subscribe, buy, contact) + real link or email

---

## Step 5: Generate Adapted Homepage

**ACTION:** Recreate the site as a self-contained HTML file:

- Design aesthetic from the imported site (colors, fonts, layout, animations)
- All content from the user's real data
- Self-contained HTML (inline CSS, no external dependencies except Google Fonts)
- Mobile-responsive
- Open Graph tags + Schema.org
- Scroll reveal animations matching original site's style

**Filename:** `homepage.html`

---

## Step 6: Auto-Open

**ACTION:** Open in browser:
```powershell
Start-Process "homepage.html"
```

---

## Step 7: Review & Sources

Show:
```
✅ Adapted site generated: homepage.html

Imported design from: [original URL]
Colors: [kept / replaced with: #hex]
Fonts: [kept / replaced with: Font]
Sections: [list]

Content sources:
- Hero: user-provided
- Services: user-provided
- Testimonials: [user-provided / placeholder added]

⚠️ Placeholders that need real content: [list]

Want to adjust anything? Or ready to add more pages?
```

If more pages → `workflows/02-content-pages.md`
If ready to publish → `workflows/05-deployment.md`

---

**Import complete.** Professional design, your content.
