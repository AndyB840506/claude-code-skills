# Workflow 03 — SEO Metadata: Optimize for Search Engines

Enhance all generated pages with SEO best practices — meta tags, structured data, sitemaps, robots.txt, and analytics setup. Schema.org type adapts to page content.

---

## Paso 0: Load Config & Inventory

**ACTION:** Read `website-config.json`. Identify all `.html` files in the working directory.

List pages found and ask: "Apply SEO to all pages, or a specific one?"

---

## Paso 1: Global SEO Settings

Ask:

1. **Site Keywords** — From config (confirm or update)
2. **Meta Description (site-wide)** — 155-160 chars for homepage / fallback
3. **Target Search Terms** — Top 5 terms you want to rank for
4. **Analytics** — Google Analytics, Plausible, Fathom, or none?
5. **Analytics ID** — Paste tracking ID (or leave blank)

---

## Paso 2: Per-Page SEO

For each page targeted, ask:

1. **Page Title** — Optimized (50-60 chars). Format: `[Page Topic] | [Site Name]`
2. **Meta Description** — (155-160 chars, summarizes the page value)
3. **URL Slug** — e.g., `about`, `blog/post-title`, `product/blue-wallet`
4. **Primary Keyword** — Main search term for this page
5. **Secondary Keywords** — 2-3 supporting terms

---

## Paso 3: Schema.org by Page Type

**ACTION:** Detect or ask the page type for each file, then inject the correct structured data:

| Page Type | Schema Applied |
|---|---|
| Homepage / Business | `Organization` + `WebSite` + `SiteNavigationElement` |
| Blog Post | `BlogPosting` — includes `author`, `datePublished`, `headline` |
| Product | `Product` — includes `name`, `description`, `offers` (price if provided) |
| Service | `Service` — includes `provider`, `description`, `areaServed` |
| Portfolio | `CreativeWork` — includes `author`, `dateCreated`, `name` |
| Event | `Event` — includes `name`, `startDate`, `location`, `organizer` |
| About | `AboutPage` + `Person` or `Organization` |
| Contact | `ContactPage` |
| Podcast Episode | `PodcastEpisode` — `partOfSeries`, `audio`, `datePublished` |

Always include at minimum: `@context`, `@type`, `name`, `description`, `url`.

---

## Paso 4: Open Graph & Twitter Cards

**ACTION:** Add to every page:

```html
<!-- Open Graph -->
<meta property="og:title" content="[Page Title]">
<meta property="og:description" content="[Meta Description]">
<meta property="og:type" content="website">
<meta property="og:url" content="[Page URL]">
<meta property="og:image" content="[Logo or page image]">
<meta property="og:site_name" content="[Site Name]">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Page Title]">
<meta name="twitter:description" content="[Meta Description]">
<meta name="twitter:image" content="[Image]">
```

---

## Paso 5: Technical SEO

**ACTION:** Verify and add to each page:

- `<meta charset="UTF-8">`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- `<html lang="en">` (or user's language)
- Canonical URL: `<link rel="canonical" href="[url]">`
- Alt text on all `<img>` tags (ask user if missing)
- `<title>` 50-60 chars ✅
- Analytics tracking code (if provided)

---

## Paso 6: Generate sitemap.xml + robots.txt

**ACTION:** Create:

`sitemap.xml` — Lists all pages:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://[site_url]/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <!-- one entry per page -->
</urlset>
```

`robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://[site_url]/sitemap.xml
```

If `site_url` is blank: use placeholder `https://example.com` with a note to update after deployment.

---

## Paso 7: SEO Report

**ACTION:** Generate audit for each page:

```
Page: [title]

✅ Title: "[text]" — 54 chars
✅ Meta Description: 157 chars
✅ Keywords: Primary + 2 secondary found in content
✅ Schema.org: [Type] applied
✅ OG Tags: Complete
✅ Canonical URL: Set
⚠️ Alt Text: 2 images missing alt text — [ask user to provide]

Overall: Ready for indexing
```

---

## Paso 8: Deliverables

- ✅ Updated HTML files (all with SEO applied)
- ✅ `sitemap.xml`
- ✅ `robots.txt`
- ✅ SEO audit report
- ✅ Google Search Console tip: "Submit sitemap at search.google.com/search-console after deploying"

---

**SEO complete.** All pages optimized for search engines. Next: deploy with workflow 05.
