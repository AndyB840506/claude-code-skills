# Handoff: MPD EP.02 (T2·E2) — pipeline post-grabación completo, listo para publicar

**Date:** 2026-08-06 (jueves)
**Machine:** desktop (E:\ existe, verificado; ComfyUI en E:\AI)
**Status:** In progress — todo lo que se puede hacer SIN el episodio en vivo está listo; falta el sábado (deploy + rotación de grid)

---

## What We Accomplished This Session

**Re-transcripción + verificación de fuentes**
- Segunda grabación completa detectada (`E:\Podcast\MPD\Temporada 2\EP 02\MPD EP 02.wav`, 2026-08-06 21:32-21:37) — reemplazó la toma corta del 08-05.
- Re-transcrita con WhisperX: `E:\Transcriptor\transcripciones\MPD EP 02.srt` (39:23). La toma corta vieja quedó respaldada como `MPD EP 02 (pre-fix backup).srt`.
- Verificados los 16 marcadores `.verificar` pendientes del guion contra fuentes reales (WebSearch): 15/16 confirmados. La única alerta — un incendio de Boleskine "1900" sin fuente encontrada (los documentados son 2015 y 2019) — ya está grabada en el audio (min 18:17); Andrés decidió dejarla tal cual ("no siempre tiene que ser 100% verificable"). Ver memoria `feedback_mpd_verification_debt_not_absolute`.

**Assets de publicación generados**
- `mrputridsden-production/shownotes-ep02.md` — título Spotify, descripción HTML, keywords SEO
- `mrputridsden-production/youtube-ep02.md` — metadata con 6 capítulos verificados contra el SRT real (no las estimaciones del guion)
- `mrputridsden-production/social-ep02.md` — plan de 3 días (jueves intriga / viernes contenido / sábado 00:00 lanzamiento), solo Instagram+Facebook

**Artwork nuevo, dirección propia**
- El workflow genérico de `podcast-creator/03-artwork.md` estaba desactualizado (dirección T1) — se verificó el artwork vigente y, por pedido de Andrés, se generó una escena fotorrealista integrando las 3 historias del episodio (cruce de caminos + disco de vinilo + casona/Boleskine al fondo) en vez de repetir el formato "numeral gigante" de EP.006.
- Generada en ComfyUI local (Z-Image Turbo 1536² → RealESRGAN 4x → 3000×3000), grading azul de marca (`night_grade` variante E).
- Nuevo compositor: `comfyui/templates/mpd-portada-ep02-t2.py`.
- 3 formatos finales aprobados por Andrés: `E:\Podcast\MPD\Temporada 2\EP 02\artwork\MPD-T2E02-PORTADA-3000.jpg` (1:1), `-16x9-FINAL.png`, `-9x16-FINAL.png`.

**Corrección de numeración (importante, tocó muchos archivos)**
- Andrés corrigió: el episodio es **EP.02**, no "EP.007" — T2 reinicia numeración pública por temporada. Esto también reveló que la política vieja del roadmap (número interno EP.006/EP.007 vs número público T2·E1/E2) quedó **retirada**: ahora todo usa el mismo número en archivos y en texto público.
- Renombrados: guion (`EP02-el-rock-y-el-diablo.html` + `.artifact.html`), show notes, YouTube, social, checkpoint del pipeline, compositor de artwork. Contenido corregido en `roadmap-mpd.md` (regla nueva documentada), `banco-expedientes.md`.
- Los handoffs viejos (`2026-08-03-mpd-banco-expedientes-y-ep007.md`, `2026-08-05-mpd-ep007-reescritura.md`) **NO se tocaron** — narran el estado a esa fecha, cuando el episodio sí se llamaba así.

**Spotify**
- URL recibida: `https://open.spotify.com/episode/46l6NpQVF9np4unotGT4KM?si=dscl0PsHSoWMLsIURGBNGQ` — Andrés avisó explícitamente que **no resuelve todavía**, el episodio publica el **sábado 2026-08-08 a las 00:00**.

**Retrospectiva aplicada** (3 fixes al kit de skills, ver commit de hoy):
1. `episode-pipeline/00-intake.md` — antes de fijar el número público de un episodio, verificar el roadmap del show (causa raíz del reproceso EP.007→EP.02).
2. `podcast-creator/03-artwork.md` — la dirección visual "CONGELADA" de MPD marcada SUPERADA para T2, apunta a `comfyui` skill como fuente vigente.
3. `episode-pipeline/02-assets.md` — nota de que MPD tiene compositor local propio (ComfyUI), no usar el flujo genérico de Flow sin verificar primero.

Auditoría de skills: 0 colisiones de triggers, 0 `SKILL.md` sobre 50 líneas, sin archivos sueltos.

---

## Where We Paused

**Last action:** checkpoint del pipeline actualizado con la URL de Spotify (no viva todavía).

**Next action (sábado 2026-08-08, ~00:00 o después):** confirmar que la URL ya resuelve, y retomar el pipeline desde `episode-pipeline/workflows/04-grid-rotation.md` → `05-deploy-verify.md`.

**Blockers:**
- El episodio no está en vivo en Spotify hasta el sábado — no se puede rotar el grid del sitio ni desplegar con ese link todavía (quedaría un href muerto).

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep02.md` — checkpoint completo, `stage_c: blocked_on_live`
- `mrputridsden-production/pipeline-audit-ep02.md` — bitácora detallada de todo lo hecho hoy
- `mrputridsden-production/roadmap-mpd.md` — política de numeración nueva (leer antes de tocar cualquier episodio de MPD)

---

## Notes / Gotchas

- **La política de numeración de MPD cambió hoy** — cualquier sesión futura que toque un episodio de MPD debe leer `roadmap-mpd.md` primero, no asumir el esquema viejo (interno vs público) que ya no aplica.
- **El grid del sitio y el deploy dependen de que Spotify esté realmente en vivo**, no solo de tener la URL — no hay forma de verificarlo antes del sábado, así que no lo intentes antes.
- **El compositor de artwork nuevo (`mpd-portada-ep02-t2.py`) es específico de este episodio** (título, tagline y ruta de escena hardcodeados) — para el próximo expediente, copiarlo y adaptar, no reusarlo tal cual (mismo patrón que `mpd-portada-ep-t2.py` para EP.006).
- **Expediente 03** (próximo tema, decidido 2026-08-05): Crowley y su huella musical más allá de Zeppelin — leads sin verificar en `banco-expedientes.md` #2. NO se anunció al aire en el cierre de este episodio (decisión editorial, no descuido).

---

## Questions to Answer

1. Sábado: ¿confirmar en vivo la URL de Spotify y arrancar `04-grid-rotation.md`, o prefieres hacerlo tú mismo y avisarme cuando esté publicado?
2. ¿Se arranca ya la investigación del Expediente 03 (Crowley), o se espera a cerrar el lanzamiento de EP.02 primero?
