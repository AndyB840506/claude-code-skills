---
name: web-page-kit
description: "Create professional web pages for any business, brand, or content — scroll experience, business, portfolio, blog, e-commerce, events, personal brand, podcast. Guided step-by-step from setup to deployment. Bilingual EN/ES. Triggers: create website, web page generator, generate web page, build website, create landing page, make website, page builder, seo optimization, website from scratch, import website, adapt website, scroll experience, cinematic website, scroll animation, scroll video, portfolio site, business website, publish website, crear sitio web, crear página web, publicar sitio, página web."
---

# Web Page Kit — Professional Web Presence

Guided wizard: language → website type → build → publish.  
Works for any site type. Bilingual EN/ES. Creates self-contained HTML files, deploys to Netlify in minutes.

**No-Fabrication Rule: Never invent content. Only use real data the user provides. Mark missing info as [PLACEHOLDER].**

---

## On First Launch

**ACTION:** Always run `workflows/00-welcome.md` when no `website-config.json` exists.

The welcome workflow handles:
- Language selection (EN/ES)
- Website type selection (8 options)
- Start method (scratch or import)
- Full step-by-step progress map through deployment

---

## Routing (Mid-Session)

Once config exists, route based on user intent:

| User says... | Launch workflow |
|---|---|
| "welcome", "start over", "new site", "restart" | `workflows/00-welcome.md` |
| "import", "copy site", "adapt", "from URL" | `workflows/00-import.md` |
| "setup", "brand", "configure", "identity" | `workflows/00-setup.md` |
| "homepage", "hero", "home", "landing page" | `workflows/01-homepage.md` |
| "page", "content", "blog post", "product", "service", "portfolio item" | `workflows/02-content-pages.md` |
| "seo", "optimize", "meta", "keywords", "sitemap" | `workflows/03-seo-metadata.md` |
| "analyze", "audit", "check URL", "competitor" | `workflows/04-page-analysis.md` |
| "publish", "deploy", "go live", "netlify", "upload" | `workflows/05-deployment.md` |
| "export", "download", "package" | `workflows/06-html-export.md` |
| "scroll video", "cinematic", "scroll animation", "scroll effects" | `workflows/01-homepage.md` (Paso 2 scroll-video option) |

---

## Website Config (`website-config.json`)

Created by welcome + setup flows. Structure:

```json
{
  "language": "en | es",
  "site_name": "",
  "tagline": "",
  "description": "",
  "site_type": "scroll | business | portfolio | blog | ecommerce | events | personal | podcast",
  "industry": "",
  "owner_name": "",
  "owner_bio": "",
  "primary_color": "",
  "secondary_color": "",
  "accent_color": "",
  "logo_description": "",
  "keywords": [],
  "page_types": [],
  "social_links": {
    "instagram": "",
    "twitter": "",
    "linkedin": "",
    "youtube": "",
    "facebook": ""
  },
  "contact_email": "",
  "site_url": "",
  "import_source": null
}
```

---

## Site Type → Design Defaults

| site_type | Vibe | Key Sections |
|---|---|---|
| `scroll` | Cinematic, dark, full-screen, immersive | Scroll-video hero, sticky sections, animations |
| `business` | Professional, trust-building | Services, About, Testimonials, Contact |
| `portfolio` | Visual, minimal | Work, Skills, Bio, Hire Me |
| `blog` | Clean, readable | Posts, About, Subscribe |
| `ecommerce` | Conversion-focused | Products, Features, Reviews, Buy CTA |
| `events` | Energetic, urgent | Dates, Speakers, Register, Countdown |
| `personal` | Authentic, story-led | Story, Services, Content, Contact |
| `podcast` | Media-rich | Episodes, Subscribe, Host, Player |

---

## Design & Content References

- [docs/design-guide.md](docs/design-guide.md) — Animation patterns, scroll-video, self-contained HTML rules
- [docs/content-rules.md](docs/content-rules.md) — No-fabrication, graceful degradation, data sourcing

---

## EXECUTION

When `/web-page-kit` is invoked:

1. **Check for `website-config.json`**
   - NOT found → run `workflows/00-welcome.md` (guided wizard)
   - Found → greet returning user, show where they left off, ask where to continue

2. **Detect language from config** → respond in EN or ES throughout

3. **Detect intent** → route to matching workflow (routing table above)

4. **Before generating any HTML** → verify real data exists. If missing, ask — never invent. Then apply `frontend-design` principles: commit to a specific aesthetic direction (tone, typography, composition) before writing a single line of CSS. Never fall back to generic fonts or predictable layouts — every page must have a deliberate, context-specific design identity. If integration with an external tool is proposed (e.g. a search CLI, API, or library), verify the tool is installed first (glob for key files, check PATH) before designing any workflow around it — do not assume availability.

   **Redesign rule:** A redesign means structural/layout changes — different hero structure, different section order, different content patterns (e.g. cards → numbered list, centered → split). Changing only CSS variables or font families is NOT a redesign and will look identical to the user. If the user says "it looks the same": read both files, compare layout structure (hero type, grid columns, section count, content components), then ask the user which specific sections or patterns they want changed before generating anything.

5. **After each step** → show updated progress map (which steps are ✅ done, which are ⬜ next)

6. **End goal** → every session path leads to `workflows/05-deployment.md` (publish)
