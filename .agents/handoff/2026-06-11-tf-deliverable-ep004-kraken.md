# Handoff: The Freelancer deliverable pipeline + EP.004 Kraken (Stage A)
**Date:** 2026-06-11
**Status:** Complete — sesión cerrada con ritual completo (retrospective + audit + handoff)
---
## What We Accomplished This Session

### The Freelancer (repo `the-freelancer`, andyfreelancer.com, DO App Platform)
- **Pipeline de deliverable automático E2E verificado:** confirmar pago en dashboard (select de status por orden) → PATCH `/order/:ref/status` → `generateDeliverable(ref)` con claude-opus-4-8 + web tools → email con draft HTML adjunto → orden a `en_revision`. Probado con orden real AB-20260527-852 (SEO Audit) — el correo con adjunto llegó.
- **7 prompts de servicio** en `freelancer/prompts/` (lead_generation, web_page, seo_audit, business_audit, social_to_web, meta_ads_audit, copywriting).
- **Transcripts durables** en tab `transcripts` del Sheet CRM (service accounts no tienen quota de Drive para subir archivos — workaround arquitectural).
- **SMTP arreglado:** causa raíz = env vars de DO en 2 niveles (componente gana sobre App-Level). App Password expuesta en chat fue **rotada y verificada** (correo de prueba 2026-06-11 20:55 ✅).
- **Bot con "chispa"** (sección Conversational craft, persona Andy, payload con country/formato) + **estimador** apuntando a `/estimador-quote` (fix del botón).
- Commits: 091a2d0…10f57d7 + 6636f24 (test-smtp.ps1 helper). Todo pusheado y en producción.

### Mr. Putrid's Den — EP.004 Kraken (repo `kit-skill-creator`)
- **Cambio de roadmap aprobado:** EP.004 = "Kraken: El Titán del Rock Colombiano" (regla de audiencia: ancla = banda reconocible, tras bajo rendimiento de EP.003). Grabación: **2026-06-12**.
- **Stage A completo:** guion ~3.500 palabras (`mrputridsden-production/scripts/EP004-kraken-el-titan-del-rock-colombiano.html`), artwork prompts (`episodios/artwork-ep004.md`), pipeline-state + bitácora.
- **Guion v2:** 11 bloques reescritos a estilo EP.002 tras feedback "Juan lee como un viejito" — la causa raíz era la propia regla de balance co-host que prescribía aperturas teatrales; regla corregida en `.claude/skills/mrputridsden/CLAUDE.md` + memoria `feedback_mpd_juan_voice`.

### Cierre de sesión (retrospective + audit aplicados)
- Rutas fantasma `E:\` corregidas en: `mrputridsden/CLAUDE.md`, `kit-skill-creator/CLAUDE.md`, `podcast-creator/workflows/01-episodio.md` (E: no existe post-wipe).
- Técnicas PS 5.1 añadidas al CLAUDE.md global (WriteAllText UTF-8 sin BOM, `git commit -F`, JS a archivo en vez de `node -e`).
- Gotcha DO env vars 2 niveles documentado en memoria `feedback_digitalocean_deploy`.
- Commits de cierre: f87cf35 (guion v2), fc01afb (retro), 2b6642b (audit). Clon global `~/.claude/skills` sincronizado a 2b6642b.

## Where We Paused
**Last action:** ritual de cierre completo; ambos repos limpios y pusheados.
**Next action:** grabación EP.004 (2026-06-12). Antes de grabar: Juan debe pasar **eventos reales** para `eventos.json` — el segmento de Promoción del guion es placeholder estructurado.
**Blockers:** eventos.json sigue con eventos EJEMPLO (depende de Juan).

## Files to Read First
- `mrputridsden-production/scripts/EP004-kraken-el-titan-del-rock-colombiano.html` — guion v2 listo para grabar
- `mrputridsden-production/pipeline-state-ep004.md` — Stage A complete; Stage B (post-grabación) y C pendientes
- `mrputridsden-production/roadmap-mpd.md` — regla de audiencia nueva + estado EP.003/004

## Notes / Gotchas
- **DO env vars:** existen en App-Level Y componente — el componente (Web Service) GANA. Editar siempre en el componente. Cada cambio de env var redeploya y mata jobs en vuelo.
- **Service accounts sin storage quota:** crear carpetas en Drive funciona, subir contenido NO. Persistencia → Sheets; entrega → email con adjunto.
- **PS 5.1:** editar archivos con acentos solo vía `[System.IO.File]::WriteAllText` + `UTF8Encoding($false)`; commits multilinea con `git commit -F`; nunca `node -e` (escribe .js dentro del proyecto).
- `test-smtp.ps1` (en the-freelancer) = diagnóstico local de App Password; pide la clave en pantalla, no la guarda.
- Dual-clone: editar en `repos\kit-skill-creator`, push, pull en `~/.claude\skills`.

## Questions to Answer
- ¿El draft del SEO Audit que generó Opus (adjunto en el correo de AB-20260527-852) tiene la calidad esperada? Revisarlo calibra los 7 prompts.
- ¿Rotar la Gmail App Password commiteada en el repo Burrous Brothers del estimador? (pendiente de sesión anterior, ver memoria `project_estimador_instances`).
- Stage B de EP.004 (show notes/metadata post-grabación) — correr el pipeline después de grabar.
