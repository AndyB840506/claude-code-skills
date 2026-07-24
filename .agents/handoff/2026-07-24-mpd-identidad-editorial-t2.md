# Handoff: MPD T2 — identidad editorial definida (alcance, persona, tono, apertura fija)
**Date:** 2026-07-24 (viernes)
**Machine:** desktop (E:\)
**Status:** Complete — canonizado, commiteado y pusheado. EP.006 en modo "trabajar completo", NO se publica esta semana.

> Segundo handoff del 2026-07-24. El otro (`2026-07-24-compuerta-assets-y-deploy-gate.md`) es de OTRO tema (deploy gate), no de MPD.

---

## Qué se decidió y escribió esta sesión

Partió de una pregunta de formato ("¿mito y debunk tipo Scooby-Doo, o dejar el misterio abierto?") y terminó definiendo la identidad editorial completa de T2, apoyada en un **estudio de mercado** (artifact publicado, ver abajo) y en **feedback de un círculo cercano** que Andrés recogió por WhatsApp.

**Identidad T2 (ahora CANON, ya no provisional):**
- **Alcance: híbrido anclado en rock** — rock/música es la columna e identidad, pero abierto a otras leyendas e invitados; se amplía cuando haya base. Sigue siendo 100% misterios/leyendas (NO episodios de banda). Esto AFLOJA el "100% rock" que se había fijado el 07-23.
- **Persona: 3ª persona investigativa + viñetas dramatizadas** marcadas como reconstrucción. PROHIBIDO 1ª persona "como el artista" (inventa a un músico real, rompe el pilar dato-vs-leyenda).
- **Tono: serio e inmersivo (tipo Relatos de la Noche) + chispa seca.** NO comedia tipo Leyendas Legendarias (necesita trío, apaga lo eerie, choca con el terreno de LL).
- **Formato (ya venía del 07-24 AM):** mito en teaser → destape que reencuadra (o abierto si es irresoluble); narrativa única por episodio; no deificar artistas.
- **Apertura fija:** `logo sonoro (3–5 s) → disclaimer (voz grave) → intro music → Andrés`. Logo y disclaimer son bumpers fijos reutilizables (se producen una vez).

### Archivos tocados (commits `159ac18`, `7276c43`, `0c3f432`)
| Archivo | Cambio |
|---|---|
| `mrputridsden/CLAUDE.md` | § Formato canon; § Alcance/persona/tono; estructura con logo+disclaimer; § Feedback de audio (método ffmpeg) |
| `mrputridsden/glosario-cachaco.md` | Persona y tono narrativo T2 |
| `mrputridsden-production/audio/t2-disclaimer-e-intro.md` | NUEVO — disclaimer (v3/v2), ajustes ElevenLabs, brief logo sonoro, prompt de música |
| memoria `project_mpd_archivos_secretos_pillar` | Alcance híbrido + persona/tono + estado EP.006 |
| memoria `project_mpd_rebrand_cruce_de_caminos` | "100% rock" → híbrido; codename "Cruce de Caminos" ya estaba retirado |
| memoria `feedback_mpd_no_occult_symbols` | Corregido "El Cruce de Caminos" como nombre (era codename retirado) + límite hermano "no deificar" |
| `MEMORY.md` | Hooks de pilar y rebrand actualizados |

## Estudio de mercado (artifact)
- URL: https://claude.ai/code/artifact/2a895bfc-5a5e-41a8-b383-851e06dd0613 (privado)
- Hallazgos: los gigantes hispanos (Relatos de la Noche, Leyendas Legendarias, La Rosa de los Vientos) son AMPLIOS → un nuevo necesita gancho afilado primero. Nicho "misterio del rock" casi vacío = white space real, pero sin hit que pruebe escala. Intro: gana el logo sonoro corto (3–5 s), fijo, primer sonido (valida el feedback del pana).

## Estado EP.006 (Club de los 27 = T2·E1)
- **Audio GRABADO** (`E:\Podcast\MPD\Temporada 2\EP 01\MPD EP 01.mp3`, ~44 MB, grabado 07-24 07:58).
- En **ronda de feedback** con círculo cercano para validar el formato. **NO se publica esta semana** (decisión de Andrés — trabajarlo completo con el formato nuevo).
- Guion listo: `scripts/EP006-club-de-los-27.html`.

## Next Steps

**Producción de audio (Andrés — no lo puedo generar yo):**
1. **Logo sonoro (3–5 s)** — crear según brief en `mrputridsden-production/audio/t2-disclaimer-e-intro.md`.
2. **Disclaimer** — sacarlo en ElevenLabs (texto + ajustes ya en ese doc; voz grave, menos whisper).
3. **Música de intro** — generar con el prompt del doc (lúgubre-magnético, máx 45 s). Cuando haya 2–3 tomas, pasármelas: las comparo por espectrograma (método nuevo en CLAUDE.md § Feedback de audio). Fallback disponible: recortar `E:\Downloads\La_Grieta_del_Mito.mp3` a ~40 s.

**Post-recording de EP.006 (cuando el formato quede confirmado por el feedback):**
4. Transcripción (SRT, WhisperX en el desktop) → 5. Metadata/show-notes (`episodios/ep006-metadata.md`, no existe) → 6. Quote cards (validar contra audio real, no el guion) → 7. Plan de lanzamiento 3 días.

**Manual pendiente de antes (no de esta sesión):** subir la portada nueva de T2 a Spotify/Apple/Amazon (ver `reference_mpd_website_live` / rebrand memory).

**Decisión de marca aún ABIERTA:** con alcance híbrido + "invitar a quien sea", falta definir si los invitados siguen SOLO por La Silla Pútrida o si se abre el formato de invitados. No se tocó la estructura de La Silla esta sesión — es el próximo detalle a resolver cuando surja.

## Notes / Gotchas
- El disclaimer dice "los expedientes que la música dejó sin cerrar… y de vez en cuando, otros que el tiempo prefirió olvidar" — redacción abierta por el alcance híbrido (antes decía "el rock").
- Método reutilizable nuevo: para dar feedback de audio sin oírlo, renderizar espectrograma+waveform con ffmpeg y leerlos como imagen (estructura/frecuencia, NO timbre). Quedó en `mrputridsden/CLAUDE.md`.
