---
name: web-page-kit
description: "Create professional web pages for any business, brand, or content — scroll experience, business, portfolio, blog, e-commerce, events, personal brand, podcast. Guided step-by-step from setup to deployment. Bilingual EN/ES. Triggers: create website, web page generator, generate web page, build website, create landing page, make website, page builder, seo optimization, website from scratch, import website, adapt website, scroll experience, cinematic website, scroll animation, scroll video, portfolio site, business website, publish website, crear sitio web, crear página web, publicar sitio, página web."
---

# Web Page Kit — Professional Web Presence

Guided wizard: language → website type → build → publish.
Works for any site type. Bilingual EN/ES. Creates self-contained HTML files, deploys to Netlify in minutes.

**No-Fabrication Rule: Never invent content. Only use real data the user provides. Mark missing info as [PLACEHOLDER].**

## On First Launch

**ACTION:** Always run `workflows/00-welcome.md` when no `website-config.json` exists.

The welcome workflow handles language selection (EN/ES), website type selection
(8 options), start method (scratch or import), and the full step-by-step progress
map through deployment.

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

## Execution

Follow `workflows/execution.md` for the full per-session flow (config check, language
detection, routing, design rules, progress map). Every session path leads to
`workflows/05-deployment.md` (publish).

## Reference

- `docs/website-config-schema.md` — `website-config.json` schema + site type → design defaults table
- `docs/design-guide.md` — Animation patterns, scroll-video, self-contained HTML rules
- `docs/content-rules.md` — No-fabrication, graceful degradation, data sourcing
