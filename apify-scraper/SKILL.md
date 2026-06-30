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
