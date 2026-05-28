# Workflow 00 — Setup: Brand & Site Identity

Establishes brand identity, site type, colors, and SEO. All saved to `website-config.json`.

> **No-Fabrication Rule:** Only ask for real information the user has. Never fill in missing fields with invented content.

---

## Paso -1: Context Check

**If called from `00-welcome.md`:** `site_type` and `language` are already set. Skip Paso 1 (site type) entirely — go directly to Paso 2.

**If called directly:** Check for `website-config.json`:
- **Config exists** → Show current values. Ask (in config language): "Update anything, or proceed to workflow 01?"
- **No config** → Proceed to Paso 0.

---

## Paso 0: Orientation

Respond in the language from config (`language: "en"` or `"es"`).

**EN:** "Let's set up your site. A few questions about your brand, colors, and keywords — takes ~10 minutes. You can always update later."

**ES:** "Configuremos tu sitio. Unas preguntas sobre tu marca, colores y palabras clave — unos ~10 minutos. Puedes actualizar después."

---

## Paso 1: Site Type *(skip if pre-filled from welcome)*

**EN:** "What kind of site is this?"
**ES:** "¿Qué tipo de sitio es este?"

1. Scroll Experience / 2. Business / 3. Portfolio / 4. Blog / 5. E-commerce / 6. Events / 7. Personal Brand / 8. Podcast / 9. Other

Store as `site_type` in config.

---

## Paso 2: Brand Identity

Respond in the config language throughout. Ask in one block:

1. **Site/Business Name** — What's this site called?
2. **Tagline** — One line that captures what you do (e.g., "Design that converts")
3. **Description** — 2-3 sentences about what this site is for and who it serves
4. **Industry/Category** — Your field (e.g., Photography, SaaS, Fitness, Legal)
5. **Owner/Creator Name** — Your name or the person/company behind this site
6. **Owner Bio** *(optional)* — 1-2 sentences about you (for About sections)

---

## Paso 3: Visual Identity

Ask:

1. **Primary Color** — Main brand color (hex, e.g., #1A1A1A). Don't have one? I'll suggest options.
2. **Secondary Color** — Supporting color (#hex)
3. **Accent Color** — For CTAs and highlights (#hex)
4. **Logo/Mark Description** — Describe your logo or icon (for CSS placeholder if no image file)

**If user has no colors yet**, suggest palette options by site type:
- Business/Professional: `#1A1A2E` + `#16213E` + `#0F3460`
- Creative/Portfolio: `#2D3436` + `#636E72` + `#FDCB6E`
- Health/Wellness: `#2D6A4F` + `#52B788` + `#B7E4C7`
- Bold/Modern: `#D62828` + `#F77F00` + `#FCBF49`
- Minimal/Clean: `#222222` + `#555555` + `#EEEEEE`

---

## Paso 4: Keywords & Contact

Ask:

1. **Primary Keywords** — 5-7 terms your audience searches (comma-separated). E.g., "web designer, UI/UX, freelance, Bogotá"
2. **Target Site URL** — Where will this live? (e.g., mysite.com). Blank = skip for now.
3. **Contact Email** — Public contact email for forms/footer

---

## Paso 5: Social Links *(optional)*

Ask for any relevant social links:

- Instagram, Twitter/X, LinkedIn, YouTube, Facebook, TikTok, GitHub, Spotify, Apple Podcasts

Only ask for links relevant to the site type (e.g., GitHub for Portfolio/Dev, Spotify for Podcast).

---

## Paso 6: Site Structure

Ask based on site type:

> "What pages will your site have?"

Suggest defaults by type:
- **Business**: Homepage, Services, About, Contact
- **Portfolio**: Homepage, Work, About, Contact
- **Blog**: Homepage, Posts, About, Newsletter
- **E-commerce**: Homepage, Products, About, Contact
- **Events**: Homepage, Schedule, Speakers, Register
- **Podcast**: Homepage, Episodes, About, Subscribe

Store as `page_types` in config. User can add or remove pages.

---

## Paso 7: Generate Config & Summary

**ACTION:** Write `website-config.json` with all gathered data.

Show summary:
```
✅ Config Created!

Site: [name] — [site_type]
Industry: [industry]
Colors: [primary] | [secondary] | [accent]
Keywords: [list]
Pages: [page_types]
Social: [which links were provided]

Next steps:
- Run workflow 01 → Create homepage
- Run workflow 02 → Add content pages
```

**Optional:** "Want a visual brand guide?" → generate `brand-guidelines.md`

---

**Setup complete.** `website-config.json` is ready. Every other workflow reads from it.
