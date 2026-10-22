# Handoff: HireSignal 3b-2b → 1.11.1 y kumatalent.com en 4 idiomas (sprint 5)
**Date:** 2026-10-22 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — sitio nuevo publicado en EN/FR/ES/PT; HireSignal 1.11.1 en producción
---
## What We Accomplished This Session
- HireSignal (repo `hiresignal`, master `8773edb`, prod 1.11.1):
  - 1.10.0 / 1.10.1: admin completo en el idioma de la cuenta (EN/FR/ES/PT), CSV traducido.
  - 1.11.0: demo en vivo (`api/demo-request.php` → link de un solo uso → `demo.php`; PDF al
    visitante + aviso a hello@; admin → Demos).
  - 1.11.1: arreglo de la reconexión del chat (msg_id por respuesta, `api/chat-turns.php`),
    probado en producción con celular emulado.
- kumatalent.com (repo `kuma-talent-web`, master = `70fa628`, publicado y medido en vivo):
  - Copy FR/ES/PT (`site/copy/*.json`), SEO (canonical, hreflang, OG por idioma, JSON-LD,
    sitemap, robots), 404 en 4 idiomas, `fr.html` → `/fr/`, variantes viejas borradas.
  - Publicar = `python site/build.py --root` + commit + push master (~45s).
  - Pruebas: `site/shots.py` 18/18, `/try` contra producción 4/4 + 1 en vivo con CORS real,
    "Book a demo" 4/4 con filas en el Sheet.

## Where We Paused
**Last action:** publicar `70fa628` en master y comparar el HTML en vivo contra el local (solo
difiere por la ofuscación de emails de Cloudflare).
**Next action:** lo que pida Andrés; candidatos abajo.
**Blockers:** el 404 real y los logs de DO piden un token de DO nuevo (el anterior se revocó).

## Files to Read First
- memoria `project_kumatalent_site_sprint5.md` — estado y pendientes del sitio
- memoria `reference_kumatalent_bilingual.md` — cómo se edita el copy y el registro por idioma
- `kuma-talent-web/site/build.py` — docstring con los tres modos (out, --root, --inline)
- `hiresignal/.agents/build-state/sprint4-demo.md` — demo en vivo y 1.11.1

## Notes / Gotchas
- El `diff` en vivo contra local siempre difiere en los `mailto:` (Cloudflare email obfuscation).
- DO sirve `index.html` con status 404 para URLs inexistentes; `404.html` no se usa.
- Capturas: usar reduced motion + recorrer la página (regla nueva en CLAUDE.md del kit).
- FR usa "score" como el producto; la regla vieja "pointage" se retiró de la memoria.
- Las solicitudes de demo de prueba usaron alias `berandre2+site5-*@gmail.com`; los links no se abrieron.

## Questions to Answer
- Andrés: borrar las filas 10–13 del Sheet "Kuma Talent Database" (pruebas "Site check … test, ignore").
- ¿Dar de alta el sitemap en Google Search Console? (no se hizo; nadie lo pidió).
- ¿Traducir el reporte de muestra (PDF) a FR/ES/PT? Hoy las páginas avisan que está en inglés.
- ¿Quitar `docs/migracion-do.md` del sitio público? (sin secretos, pero son notas internas).
- Opcional: token DO nuevo para confirmar que se fue el aviso `output_buffering` y poner `404.html` como error document.
