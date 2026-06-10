# El archivo de estado — cómo el pipeline retoma entre sesiones

Cada episodio tiene un `pipeline-state-ep[NNN].md` (creado en Stage A, junto al audit
log) que registra qué macro-stage se completó y valores clave resueltos
(`spotify_url`). **Al invocar el pipeline para un episodio, léelo primero** — define
en qué workflow arrancar:

| Estado del archivo | Arranca en |
|---|---|
| No existe | Pregunta primero si ya hay grabación + guion (episodios en curso antes de este checkpoint, ej. BTQ EP.16) — si sí, crea el archivo retroactivamente con `stage_a: complete` y sigue en `00-intake.md`; si no, `00-roadmap.md` (Macro-Stage A desde cero) |
| Existe pero incompleto (ej. `stage_a: in_progress` sin completar, o campos clave vacíos — sesión interrumpida a medias) | No asumas que se puede continuar a ciegas — pregunta: "El archivo de estado de EP.0XX quedó a medias en [stage] — ¿retomamos desde ahí o lo regeneramos?" |
| `stage_a: complete`, `stage_b: pending` | `00-intake.md` (Macro-Stage B — el audio ya existe) |
| `stage_b: complete`, `spotify_url: pending` | Se detiene a pedir la URL de Spotify — ver Paso 0 de `00-intake.md` |
| `stage_b: complete`, `spotify_url` resuelto | `03-image-validation.md` (Macro-Stage C) |
| `stage_c: complete` | Episodio cerrado — no hay nada que retomar |

Esto es lo que resuelve el caso real que motivó este rediseño: **BTQ EP.16** tiene
guion + grabación + metadata listos pero no está vivo en Spotify — su archivo de
estado mostraría `stage_b: complete, spotify_url: pending`, y el pipeline se detendría
ahí a pedir la URL en lugar de fallar más adelante en Stage 4/5 sin nada que verificar.
