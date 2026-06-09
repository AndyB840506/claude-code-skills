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
el punto exacto donde un humano (no Claude) debe actuar en el mundo real:

```
Macro-Stage A — Pre-producción
  roadmap → guion → prompts de artwork
  ⏸ pausa natural: "ve a grabar"

Macro-Stage B — Post-grabación → Spotify
  intake (auto-descubre el audio) → transcripción → assets/metadata
  ⏸ pausa natural: "publica en Spotify, dame la URL en vivo"

Macro-Stage C — Lanzamiento
  validación de imágenes → marketing (social + quote cards) →
  rotación de grid → deploy + verificación (web + Spotify)
```

**No reimplementa nada que ya exista.** Este skill invoca y encadena skills/workflows
existentes (`transcriptor`, `episode-launch`, `podcast-creator`, `btq-project`,
`btq-guion`, `deploy-preflight`) y solo construye las piezas que genuinamente faltaban:
roadmap + checkpoints entre sesiones, validación de imágenes generadas, material de
marketing orquestado, rotación de grid en MPD, y verificación post-deploy.

---

## Regla fundamental

**Corre de forma autónoma entre los puntos de pausa listados abajo — no preguntes nada
fuera de ellos.** Si un workflow invocado normalmente haría preguntas pero los datos ya
están en el "episode brief" o en `pipeline-state-ep[NNN].md`, sáltalas y sigue.

Si los datos que el usuario da al invocar el pipeline contradicen lo que ya está en
`pipeline-state-ep[NNN].md` o el episode brief (ej. número de episodio distinto, show
distinto), detente y pregunta cuál es correcto antes de continuar — no asumas que el
dato más reciente gana ni sobreescribas el checkpoint silenciosamente.

---

## El archivo de estado — cómo el pipeline retoma entre sesiones

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

---

## Flujo de stages

```
00-roadmap          → [Stage A] roadmap → guion → artwork prompts → ⏸ ve a grabar
00-intake           → [Stage B] episode brief (auto-descubre el audio ya grabado)
01-transcription    → invoca transcriptor (headless, SRT + diarización)
02-assets           → BTQ: episode-launch | MPD: podcast-creator workflows
   ⏸ [gate heredado] episode-launch trae su propio gate de aprobación (BTQ)
   ⏸ checkpoint Spotify: pide URL en vivo, dispara en paralelo con Stage 3
03-image-validation → [Stage C] ⏸ PAUSA: generar en Flow → subagent valida → loop
03b-marketing       → plan social + quote cards estáticas (reusa artwork validado)
04-grid-rotation    → rota el grid de "episodios recientes" (BTQ existente / MPD nuevo)
05-deploy-verify    → ⏸ GATE FINAL → vercel --prod → curl HTTP 200 → chequeo Spotify
```

---

## Routing — Paso 0

**Primero distingue pregunta vs. ejecución.** Si el usuario solo pregunta por el estado
del roadmap o "qué episodio sigue" sin pedir que se corra el pipeline (ej. "¿qué
episodio sigue para BTQ?" vs. "corre el pipeline para el próximo episodio de BTQ"),
responde con la fila correspondiente de `roadmap-[show].md` directamente — **no
dispares Stage A ni crees archivos de estado** solo por una consulta informativa.

Si el usuario sí pide ejecutar el pipeline, **primero busca `pipeline-state-ep[NNN].md`**
para el episodio mencionado (o pregunta cuál episodio si no lo dijo) y enrútate según la
tabla de arriba — no asumas que arranca en `00-intake.md`.

Si el usuario menciona explícitamente un stage ("solo valida las imágenes del EP.017",
"rota el grid de BTQ"), salta directamente al workflow correspondiente — pero primero
confirma que existe un "episode brief" reciente en contexto o pídelo mínimamente.

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

---

## Puntos de pausa (los únicos donde el flujo se detiene)

1. **Stage A — confirmación del episodio + aprobación del guion**: inevitable, el
   roadmap y el guion son decisiones del usuario, no del pipeline
2. **Cierre de Stage A — "ve a grabar"**: pausa estructural más larga del ciclo —
   el episodio queda en `stage_a: complete` esperando que exista un audio grabado
3. **Stage B.0 — Intake**: inevitable, necesita los datos crudos del episodio recién
   grabado (a menos que ya vengan del checkpoint)
4. **Stage B.2 (ruta BTQ) — gate de `episode-launch`**: heredado del skill que
   invocamos, no es un bug del pipeline — déjalo aparecer con normalidad
5. **Cierre de Stage B — checkpoint de Spotify**: pausa estructural — no existe API de
   publicación; el usuario debe subir el episodio a Spotify for Podcasters y reportar
   la URL en vivo. Si el pipeline se invoca de nuevo antes de que esto se resuelva, el
   Paso 0 de `00-intake.md` lo detecta y se detiene aquí mismo (este es el punto que
   habría atrapado el caso de BTQ EP.16)
6. **Stage C.3 / C.3b — Pausa(s) de generación de imagen**: estructural, no existe API
   de generación automática; el usuario debe generar en Flow/Nani Banana y reportar
   rutas (cover-art en C.3, quote cards en C.3b)
7. **Stage C.5 — Gate final de aprobación**: el único gate explícitamente pedido por
   el usuario — muestra el resumen completo de lo que está por publicarse antes de
   `vercel --prod`

Fuera de estos puntos, el pipeline corre sin interrupciones — y entre macro-stages,
siempre puede cerrarse y retomarse en una sesión distinta gracias al archivo de estado.

---

## Bitácora de auditoría y archivo de estado

Stage A crea ambos archivos por episodio, guardados en la carpeta de producción del
show correspondiente (`btq-production/` o `mrputridsden-production/episodios/`):

- **`pipeline-audit-ep[NNN].md`** — registro auditable; cada stage agrega su entrada
  documentando regla verificada, qué se inspeccionó, resultado (pass/fail) y notas
- **`pipeline-state-ep[NNN].md`** — checkpoint vivo; cada macro-stage lo actualiza al
  cerrar (`stage_a/b/c: complete` + `spotify_url`) — es lo que el Routing — Paso 0 lee
  para saber dónde retomar

Formato de entrada:
```
## Stage N — [nombre]
- Qué se hizo: [resumen]
- Archivos generados/modificados: [rutas]
- Validaciones (si aplica):
  - [regla] → [pass/fail] → [detalle]
- Resultado: [OK / pendiente de aprobación / bloqueado]
```

---

## Notas de implementación

- **Dependencia de directorio activo**: `episode-pipeline` es una skill global (vive en
  `C:\Users\andre\.claude\skills\`), pero `episode-launch` y `podcast-creator` son
  skills de **proyecto** — solo se cargan cuando el directorio de trabajo activo es
  `kit-skill-creator` (donde viven en `.claude\skills\episode-launch\` y
  `.claude\skills\podcast-creator\`, este último movido ahí el 2026-06-07 tras
  detectarse anidado dentro de `mrputridsden` y por tanto no descubrible). **Corre
  el pipeline siempre desde ese directorio** — si se invoca desde otro proyecto, estas
  dos dependencias no estarán disponibles y los pasos de assets/guion fallarán al
  intentar invocarlas.
- **El "episode brief"** construido en Stage B.0 (`00-intake.md`) es el objeto que
  Stage B/C leen — evita repetir preguntas que `transcriptor`, `episode-launch` o
  `podcast-creator` normalmente harían. **El "archivo de estado"** (`pipeline-state-
  ep[NNN].md`, creado en Stage A) es lo que conecta las 3 macro-stages entre sí y
  entre sesiones.
- **Nunca declarar el deploy exitoso sin el chequeo HTTP 200** (Stage C.5) — ver
  memoria `feedback_verify_before_done`.
- **Nunca mezclar sistemas tipográficos entre shows** — MPD tiene su propio sistema
  visual; la rotación de grid en Stage C.4 usa la lógica de BTQ pero NUNCA su tipografía
  (ver memoria `feedback_mpd_vs_btq_typography`).
