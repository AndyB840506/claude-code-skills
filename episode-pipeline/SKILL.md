---
name: episode-pipeline
description: >
  Master orchestration skill — drives an episode through its full lifecycle in 3
  macro-stages that each pause where a human must act: (A) pre-production (roadmap →
  script → artwork prompts → record), (B) post-recording (transcribe → assets/metadata →
  publish to Spotify), (C) launch (validate art & quote cards → marketing → grid rotation
  → deploy + verify). Persists a per-episode checkpoint to resume across sessions.
  Triggers: episode pipeline, pipeline de episodio, lanzar episodio completo, procesar
  episodio desde audio, full episode pipeline, orquestar episodio, automatizar
  lanzamiento, qué episodio sigue, próximo episodio del roadmap.
---

# Episode Pipeline — Del roadmap al episodio en vivo

Orquesta el ciclo completo de un episodio en **3 macro-stages**, cada una cerrando donde un humano debe actuar en el mundo real:

```
A — Pre-producción:    roadmap → guion → artwork prompts → ⏸ ve a grabar
B — Post-grabación:    intake → transcripción → assets/metadata → ⏸ Spotify
C — Lanzamiento:       validación de imágenes → marketing → grid → deploy + verificación
```

**No reimplementa nada que ya exista** — invoca y encadena `transcriptor`,
`episode-launch`, `podcast-creator`, `deploy-preflight`. ⚠️ `btq-project` y
`btq-guion` NO existen en disco (confirmado 2026-06-26) — no los busques como
skills; donde un workflow los cite, usa el fallback documentado ahí mismo
(típ. `guion-style-btq.md` o `episode-launch/docs/brand-constants.md`).

**Regla fundamental:** corre autónomo entre los puntos de pausa; si los datos
contradicen el checkpoint, detente y pregunta antes de sobreescribir. Routing
del Paso 0 en `docs/routing.md`.

## Workflows

| Stage | Workflow | Qué hace |
|---|---|---|
| A — Roadmap y pre-producción | `workflows/00-roadmap.md` | Confirma el próximo episodio, genera guion + prompts de artwork, pausa para grabar |
| B.0 — Intake | `workflows/00-intake.md` | Revisa el checkpoint, reúne show + audio + datos en un "episode brief" |
| B.1 — Transcripción | `workflows/01-transcription.md` | Invoca `transcriptor` sin preguntas (respuestas pre-cargadas) |
| B.2 — Assets | `workflows/02-assets.md` | BTQ: `episode-launch` · MPD: `podcast-creator` + checkpoint de publicación en Spotify |
| C.3 — Validación de imágenes | `workflows/03-image-validation.md` | Pausa para generación en Flow → subagent valida vs. reglas estándar |
| C.3b — Marketing | `workflows/03b-marketing.md` | Plan social + quote cards estáticas (BTQ/MPD) |
| C.4 — Rotación de grid | `workflows/04-grid-rotation.md` | Aplica la regla de 4 episodios al grid del sitio |
| C.5 — Deploy + verificación | `workflows/05-deploy-verify.md` | Preflight → gate final → deploy → verifica HTTP 200 + Spotify → cierra el checkpoint |

## Reference (`docs/`)

`routing.md` (Paso 0) · `state-file.md` (checkpoint + tabla de routing) · `pause-points.md`
(7 pausas) · `audit-log.md` (bitácora) · `implementation-notes.md` (directorios, episode brief, no-mezcla).
