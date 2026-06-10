# Notas de implementación

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
