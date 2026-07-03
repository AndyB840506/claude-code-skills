# Workflow 02 — Content Pages: Generate Any Page Type

Create individual pages for your site — blog posts, product pages, service pages, portfolio items, events, landing pages, or custom pages. Each page is a **self-contained HTML file** matching your site's brand from `website-config.json`.

> **No-Fabrication Rule:** Only use real content the user provides. Never invent product descriptions, service features, prices, or any other details.  
> **Self-Contained Rule:** Each output is one `.html` file — all styles inline, works offline.

---

## Step 0: Load Config

**ACTION:** Read `website-config.json`. Extract brand colors, fonts, site type, and social links.
If missing → route to workflow 00-setup.

---

## Step 1: Page Type

Ask:

> "What kind of page do you want to create?"

Options:
1. **Blog Post / Article** — Editorial content, news, guide, tutorial
2. **Product Page** — Item for sale, with features, price, and buy CTA
3. **Service Page** — What you offer, how it works, pricing, CTA
4. **Portfolio Item** — Case study, project showcase, work sample
5. **Event Page** — Date, location, agenda, registration
6. **About Page** — Your story, team, mission
7. **Contact Page** — Form, address, map, social links
8. **Landing Page** — Focused conversion page for a campaign or offer
9. **Custom** — Describe what you need

Store selection as `page_type` for this session.

---

## Step 2: Page Content

Ask questions relevant to the selected page type:

### Blog Post / Article
1. **Title** — Headline
2. **Summary** — 1-2 sentence description
3. **Full Content** — Paste text, key points, or outline
4. **Author** — Name (default: owner from config)
5. **Publish Date** — (or today)
6. **Tags/Categories** — 3-5 topic tags
7. **Featured Image** — Path/URL, or use placeholder

### Product Page
1. **Product Name** — Exact name
2. **Description** — What it is and who it's for (user provides — no invention)
3. **Features/Benefits** — 3-6 real features the user lists
4. **Price** — Exact price or "Contact for pricing" (never invent)
5. **Images** — Paths/URLs to product photos
6. **CTA** — "Buy Now", "Add to Cart", "Request Quote", etc.

### Service Page
1. **Service Name** — What this service is called
2. **Description** — What the user gets, who it's for
3. **Process/How It Works** — Steps (user provides — 3-5 steps)
4. **Pricing** — Fixed, range, or "contact us" (never invent)
5. **Who It's For** — Ideal client description
6. **CTA** — "Book a Call", "Get Started", "Request Quote"

### Portfolio Item / Case Study
1. **Project Name** — What was built/done
2. **Client/Context** — Who it was for (or "Personal Project")
3. **Challenge** — What problem was being solved
4. **Solution** — What was done (user provides — don't embellish)
5. **Outcome** — Real results if available; otherwise omit
6. **Images/Screenshots** — Paths/URLs
7. **Tech Stack / Tools** — What was used (if relevant)

### Event Page
1. **Event Name** — Title
2. **Date & Time** — Exact date and time
3. **Location** — Address or "Online" + platform
4. **Description** — What the event is about
5. **Agenda/Schedule** — Sessions, speakers, times
6. **Speakers/Performers** — Real names + bios (user provides)
7. **Registration Link or CTA** — URL or "Contact to register"

### About Page
1. **Story** — The origin/mission in the owner's own words
2. **Team Members** — Names, roles, short bios, photo paths (user provides)
3. **Values or Mission Statement** — Real, user-provided
4. **Milestones** — Dates + achievements (only real ones)

### Contact Page
1. **Email** — From config or override
2. **Phone** *(optional)*
3. **Address** *(optional)*
4. **Form Fields** — Name, email, message (standard) or custom
5. **Map** — Address for embed, or skip

### Landing Page
1. **Goal** — What should the visitor do? (sign up, buy, download, book)
2. **Headline** — Main value proposition
3. **Benefits** — 3-5 real benefits the user lists
4. **Social Proof** — Real testimonials or numbers (user provides)
5. **CTA** — Button text + destination URL

---

## Step 3: Schema.org Selection

**ACTION:** Apply schema type matching `page_type`:

| Page Type | Schema.org Type |
|---|---|
| Blog Post | `Article` or `BlogPosting` |
| Product | `Product` |
| Service | `Service` |
| Portfolio | `CreativeWork` |
| Event | `Event` |
| About | `AboutPage` |
| Contact | `ContactPage` |
| Landing Page | `WebPage` |

---

## Step 4: Generate Page HTML

**ACTION:** Create self-contained HTML page:

- Brand colors, fonts, and style from `website-config.json`
- Semantic HTML5 structure
- Inline CSS only (no external files; Google Fonts CDN allowed)
- Open Graph meta tags
- Schema.org structured data matching page type
- Mobile-responsive
- Navigation back to homepage
- Footer with social links (from config)
- Scroll reveal animations (Intersection Observer)
- Relevant CTAs at appropriate points

**Filename:** `[page-type]-[slug].html`
Examples: `blog-how-to-design-logos.html`, `product-leather-wallet.html`, `service-brand-identity.html`

---

## Step 5: Batch Mode

Ask: "Create one page or multiple?"

- **Single:** current flow
- **Batch:** User provides a list (CSV or bullet list). Process each page in sequence, same brand styles.

---

## Step 6: Auto-Open

**ACTION:** Open the file in the browser:
```powershell
Start-Process "[filename].html"
```
Or on Mac/Linux:
```bash
open "[filename].html"
```

---

## Step 7: Review & Data Sources

Show:
```
✅ Page generated: [filename].html

Page type: [type]
Sections: [list]
Data sources:
- Title: user-provided
- Description: user-provided
- Price: [user-provided / placeholder]
- Images: [paths used / CSS placeholders]

⚠️ Placeholders: [list any [PLACEHOLDER] items]

Want to add another page, or publish now?
```

If publish → `workflows/05-deployment.md`

---

**Page complete.** Single file, brand-consistent, SEO-ready.
