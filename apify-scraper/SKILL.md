---
name: apify-scraper
description: "AI-driven web scraping via the Apify CLI for lead generation, contact enrichment, company research, competitive intel, and recruiting/job-market research (incl. Upwork monitoring). Requires an Apify account + APIFY_TOKEN. Adapted from Apify's official agent skill. Triggers: scrape leads, find leads on linkedin/instagram/google maps, apify scraper, enrich contacts, company research scrape, monitor upwork jobs, competitor scrape."
---

# Apify Scraper

Universal data extraction from ~100 Apify Actors across 15+ platforms
(Instagram, LinkedIn, Google Maps, Google Search, Reddit, generic web
crawling, and more). Requires an Apify account and `APIFY_TOKEN` — this is a
paid-per-result tool for most Actors, not free WebSearch.

Complements (does not replace) `kit-ai-lead-generator*`: those kits use plain
WebSearch with no real scraping infra. This skill adds actual platform-level
scraping when WebSearch isn't enough — e.g. LinkedIn profile search, Google
Maps business extraction with email enrichment, or Upwork job monitoring.

## Ethics gate — required before every run, not just self-hosted

Before running ANY Actor (paid or free, Apify-run or self-hosted) against a
target site, check that site's `robots.txt` for a blanket scraping/AI-use
prohibition or an AI-crawler-specific exclusion (`GPTBot`, `ClaudeBot`,
`anthropic-ai`, `DeepSeekBot`, etc.) — same check as step 1 in
`workflows/self-hosted-alternative.md`. This applies even though an Apify
Actor makes the actual request on your behalf: the Actor solving the
technical anti-bot problem doesn't waive the site owner's stated policy. If
the target disallows scraping/AI use, or blocks AI crawlers while allowing
general browsers/Googlebot, stop — don't spoof a browser User-Agent and don't
switch to a different Actor to route around it. Tell the user why and offer
only compliant alternatives.

## Workflow

Sigue `workflows/scrape.md` para el flujo general (elegir Actor, revisar
schema y costo, correr, entregar resultados). Para casos de uso específicos
con pipelines ya armados, usa el playbook correspondiente en `workflows/`:

- `workflows/lead-generation.md` — leads locales (Google Maps), B2B vía
  LinkedIn, Sales Navigator, SERP, Reddit
- `workflows/contact-enrichment.md` — emails/teléfonos desde sitios web,
  leads cálidos desde comentarios de LinkedIn
- `workflows/company-research.md` — perfiles de empresa para ABM, scouting
  de startups, prep de reuniones
- `workflows/competitive-intel.md` — ads de competencia, SEO/tráfico,
  cambios de precio/feature
- `workflows/job-market-and-recruitment.md` — research de empleos,
  sourcing de candidatos, **monitoreo de Upwork para freelance**

Antes de correr cualquier Actor de pago (la mayoría lo son), consulta
`docs/gotchas.md` — tiene el protocolo de estimación de costo y los
pitfalls más comunes. Para elegir el Actor correcto, consulta
`docs/actor-index.md`.

Si el usuario quiere evitar el costo de Apify para un sitio específico,
consulta `workflows/self-hosted-alternative.md` antes de descartar la opción
gratuita — no todos los sitios necesitan la infraestructura anti-bot de Apify.
