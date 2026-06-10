---
name: episode-pipeline
description: >
  Master orchestration skill — drives an episode through its full lifecycle in 3
  macro-stages, each ending where a human must act in the real world: (A) pre-production
  — pick the next episode from the roadmap, write its script, prep artwork prompts,
  pause for recording; (B) post-recording — transcribe with diarization, generate all
  publication assets and metadata, pause for the user to publish to Spotify; (C)
  launch — validate generated cover art and quote cards against standing rules,
  generate marketing material, rotate the website's recent-episodes grid, deploy and
  confirm the live URL + Spotify page. Persists a per-episode checkpoint file so work
  can resume cleanly across sessions/days. Stops only where a human is structurally
  required (script approval, image generation in Flow, recording, Spotify publishing)
  and at the final pre-deploy approval gate.
  Triggers: episode pipeline, pipeline de episodio, lanzar episodio completo,
  procesar episodio desde audio, from raw audio to deployed, full episode pipeline,
  orquestar episodio, automatizar lanzamiento, episode from scratch to live,
  qué episodio sigue, próximo episodio del roadmap.
---

# Episode Pipeline — Del roadmap al episodio en vivo

Orquesta el ciclo completo de un episodio en **3 macro-stages**, cada una cerrando en
el punto donde un humano debe actuar en el mundo real:

```
A — Pre-producción:    roadmap → guion → artwork prompts → ⏸ ve a grabar
B — Post-grabación:    intake → transcripción → assets/metadata → ⏸ Spotify
C — Lanzamiento:       validación de imágenes → marketing → grid → deploy + verificación
```

**No reimplementa nada que ya exista** — invoca y encadena `transcriptor`,
`episode-launch`, `podcast-creator`, `btq-project`, `btq-guion`, `deploy-preflight`.

## Regla fundamental

Corre de forma autónoma entre los puntos de pausa (`docs/pause-points.md`) — no
preguntes nada fuera de ellos. Si los datos del usuario contradicen
`pipeline-state-ep[NNN].md` o el episode brief, detente y pregunta antes de
sobreescribir el checkpoint.

## Routing — Paso 0

Solo preguntan por el roadmap ("qué episodio sigue") → responde desde
`roadmap-[show].md`, no dispares Stage A. Piden ejecutar el pipeline → lee
`pipeline-state-ep[NNN].md` y enrútate según `docs/state-file.md`. Mencionan un stage
explícito → salta a ese workflow, confirmando que hay un episode brief en contexto.

## Workflows

| Stage | Workflow | Qué hace |
|---|---|---|
| A — Roadmap y pre-producción | `workflows/00-roadmap.md` | Confirma el próximo episodio, genera guion + prompts de artwork, pausa para grabar |
| B.0 — Intake | `workflows/00-intake.md` | Revisa el checkpoint, reúne show + audio + datos en un "episode brief" |
| B.1 — Transcripción | `workflows/01-transcription.md` | Invoca `transcriptor` sin preguntas (respuestas pre-cargadas) |
| B.2 — Assets | `workflows/02-assets.md` | BTQ: `episode-launch` · MPD: `podcast-creator` (show notes + YouTube + artwork) + checkpoint de publicación en Spotify |
| C.3 — Validación de imágenes | `workflows/03-image-validation.md` | Pausa para generación en Flow → subagent valida vs. reglas estándar |
| C.3b — Marketing | `workflows/03b-marketing.md` | Plan social + quote cards estáticas (BTQ: `btq-project/quote-cards`, MPD: equivalente) |
| C.4 — Rotación de grid | `workflows/04-grid-rotation.md` | Aplica la regla de 4 episodios al grid del sitio (BTQ + MPD) |
| C.5 — Deploy + verificación | `workflows/05-deploy-verify.md` | Preflight → gate final → deploy → verifica HTTP 200 + Spotify → cierra el checkpoint |

## Reference

- `docs/state-file.md` — formato del checkpoint por episodio y tabla de routing
- `docs/pause-points.md` — los 7 puntos de pausa estructurales
- `docs/audit-log.md` — formato de la bitácora de auditoría
- `docs/implementation-notes.md` — dependencias de directorio, episode brief, reglas de no-mezcla
