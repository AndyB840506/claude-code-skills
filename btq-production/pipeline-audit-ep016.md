# Bitácora de auditoría — EP.016 (BTQ)

## Stage A — Roadmap y pre-producción
- Qué se hizo: archivo de estado creado retroactivamente — el episodio ya tenía
  grabación + guion listos antes de que existiera este checkpoint (caso motivador
  del rediseño del pipeline). No se generó guion ni prompts en esta sesión porque
  ya existían de antes.
- Archivos generados: pipeline-state-ep016.md, pipeline-audit-ep016.md
- Resultado: OK — pausa retroactiva resuelta, episodio listo para Stage B (intake)

## Stage 0 — Intake
- Qué se hizo: episode brief construido — show, número de episodio, título, referencia
  cultural, ausencia de invitado, fuentes/sources extraídas del guion v1.0 (Google
  Docs), closing TM provisto por el usuario, audio auto-descubierto y confirmado.
- Episode brief:
  - show: BTQ
  - ep_number: EP.016
  - title: The Wall — Pink Floyd / Roger Waters
  - cultural_ref: The Wall (Pink Floyd, 1979) / Roger Waters
  - guest: none
  - sources: "Comfortably Numb" (Pink Floyd) · "Steve Jobs" (2015, Danny Boyle/Aaron
    Sorkin) · "The Five Dysfunctions of a Team" (Patrick Lencioni, 2002) · Gallup
    State of the Global Workplace 2024 · Amy Edmondson (Harvard — seguridad
    psicológica) · McKinsey Global Survey 2024 · Google Project Aristotle · Brené
    Brown (Daring Greatly / Dare to Lead)
  - closing_tm: "Y como diría Pink Floyd: el muro que construiste para protegerte es
    el mismo que te impide conectar con los que más necesitas."
  - spotify_url: pending
  - audio_path: E:\Podcast\Behind The Queue Ep.16.mp3
  - language: es
  - speakers: multi
- Resultado: OK

## Stage 1 — Transcripción
- Qué se hizo: transcripción previa carecía de diarización (0 tags SPEAKER_) y traía
  alucinaciones en los bordes ("¡Suscríbete al canal...!", URL genérica). Se re-generó
  con whisperx --diarize (modelo large-v2, idioma es, nuevo token HF generado por el
  usuario tras revocar el expuesto).
- Verificación: 491 líneas con tags [SPEAKER_00]/[SPEAKER_01]/[SPEAKER_02]; apertura
  limpia (jingle + cold-open real, sin "suscríbete"); cierre incluye el closing TM
  completo y correcto ("Y como diría Pink Floyd...").
- Archivo generado: E:\Transcriptor\transcripciones\Behind The Queue Ep.16.srt
- Resultado: OK — diarización confirmada, listo para Stage 2 (assets)

## Stage 2 — Generación de assets
- **CORRECCIÓN (post-hoc):** la entrada original de esta sección decía que `episode-launch`
  "no existe en disco" — eso fue un FALSO NEGATIVO. La búsqueda solo cubrió
  `~/.claude/skills/` (global, en C:); el skill SÍ existe, project-scoped, en
  `e:\...\kit-skill-creator\.claude\skills\episode-launch\SKILL.md` (confirmado al releer
  memoria `feedback_assets_on_e_drive`, que lista `episode-launch` entre los 7 skills
  legítimamente project-scoped que sobrevivieron la limpieza de huérfanas). La referencia
  rota de `episode-pipeline/02-assets.md` apuntaba correctamente — el problema fue de
  búsqueda incompleta de mi parte, no de un workflow inexistente.
- Qué se hizo (registro original, contexto preservado): al no encontrar el skill en la
  búsqueda inicial, se generaron los assets manualmente. La lógica equivalente también
  vive, bajo otro nombre, en `btq-project/SKILL.md` §13 ("Episode Launch Orchestration —
  5 Parallel Agents"). **`episode-launch/SKILL.md` también documenta un calendario de 3
  días (Domingo intriga / Lunes lanzamiento / Miércoles refuerzo)** — un tercer punto de
  conflicto sobre el calendario de lanzamiento (suma a §10 vs §13 de btq-project). El
  usuario confirmó que la regla vigente real es: lanzamiento domingo 8PM Colombia, plan
  de 4 días (alineado con §10 de btq-project, NO con §13 ni con episode-launch/SKILL.md).
  Se generaron los assets manualmente con esa base: SEO/metadata de Spotify (preview +
  descripción completa + keywords), plan social de 4 días, y 3 prompts de cover-art
  (1:1/9:16/16:9 — paleta void black/signal gold/off-white, motivo de muro de ladrillos
  sin reproducir el arte original del álbum por tema de marca registrada).
- Archivos generados: btq-production/launch-assets/EP016-the-wall-launch.md
- Gate heredado: aprobado por el usuario (incluyendo corrección del bloque de contacto
  para incluir redes sociales completas, no solo correo)
- Checkpoint Spotify: URL confirmada — https://open.spotify.com/episode/3CNyTkA6OCLoCrmNEh0LVR
  (el usuario pasó primero un shortlink de spotifycreators-web.app.link; se resolvió el
  redirect y se le pidió el link público canónico desde Share → Copy link to episode)
- Resultado: OK — Macro-Stage B cerrada (stage_b: complete). Pendiente para después de
  esta sesión: NO hace falta corregir ninguna referencia rota (episode-launch sí existe,
  ver corrección arriba) — sí reconciliar el calendario de lanzamiento entre TRES fuentes
  en conflicto (§10 de btq-project vs §13 de btq-project vs episode-launch/SKILL.md) para
  que todas reflejen la regla real confirmada por el usuario: domingo 8PM Colombia, 4 días.

## Stage 3 — Validación de imágenes (en curso)
- Incidente: el usuario compartió 3 imágenes generadas en sesión anterior (4 de junio)
  que NO correspondían a los prompts de esta sesión — eran candidatos de una iteración
  previa (motivo: prisma + muro de ladrillos, con tipografía horneada). Al preguntar el
  motivo del prisma (referencia a *Dark Side of the Moon*, no a *The Wall*), el usuario
  explicó que fue una elección deliberada para dar contexto visual instantáneo de que el
  episodio es sobre Pink Floyd — razonamiento que NUNCA se guardó en memoria. Se creó
  `btq_artwork_pink_floyd_prism_choice` para no perder este criterio en el futuro.
- Pérdida de trabajo detectada: el usuario reveló que el prompt 1:1 original (con specs
  exactas — hex #C9A84C, tipografía, dimensiones 1080×1080px) se perdió durante la
  limpieza de carpetas huérfanas de esta sesión/sesiones recientes. El usuario lo pegó
  manualmente desde su propio historial. Se adoptó ese prompt como canónico y se generaron
  variantes 9:16/16:9 que replican exactamente su estilo, paleta y spec tipográfica —
  reemplazando los 2 intentos previos (brick-wall sin prisma, luego prisma con paleta/specs
  inventadas) que el usuario calificó como ir en círculos ("volvimos a lo mismo").
- Archivo actualizado: btq-production/launch-assets/EP016-the-wall-launch.md (sección C
  reescrita con el prompt canónico + variantes)
- Estado: prompts listos — pendiente que el usuario genere las 3 imágenes finales en
  Flow/Nano Banana 2 y comparta las rutas para correr la validación del subagente.

### Validación final — 3 candidatos confirmados
El usuario compartió 3 imágenes (1 de la tanda del 4 de junio + 2 nuevas generadas el 7
de junio con el prompt canónico recuperado) como el set final de cover-art. Validación
contra la regla de margen (tipografía en zonas muertas superior/inferior, sujeto focal
en banda central, sin iconos/texto extra):

| Formato | Archivo | Resultado |
|---|---|---|
| 1:1 (1080×1080) | D:\Downloads\Cinematic_4K_photograph._A_triangular_202606041715 (1).jpeg | OK — pasa regla de margen. Variación menor: "BEHIND THE QUEUE" sale en gold/tan en vez de blanco (spec original pedía blanco para esa línea, gold solo para "BTQ"). Cosmético, no rompe la marca (gold #C9A84C es el acento de BTQ). |
| 16:9 | D:\Downloads\Cinematic_4K_photograph._A_triangular_202606072006.jpeg | OK — pasa regla de margen. Tipografía y sujeto focal en zonas correctas. |
| 9:16 | D:\Downloads\Cinematic_4K_photograph._A_triangular_202606072006 (1).jpeg | OK — pasa regla de margen. Tipografía y sujeto focal en zonas correctas. |

- Resultado: OK — Stage 3 (validación de imágenes) cerrada. Trío de cover-art aprobado
  para EP.016. Continúa a Stage 3b (material de marketing — quote cards + plan social).

## Stage 3b — Material de marketing
- Plan social: ya generado en Stage 2 (4 días, lanzamiento domingo 8PM — ver sección B
  de EP016-the-wall-launch.md). No requiere regeneración.
- Quote cards: se extrajeron y presentaron los 14 [REMATE] del guión + closing TM (15
  candidatos) según `quote-cards.md`. El usuario indicó que ya las generó en la sesión
  previa (la misma en que se creó el artwork) y decidió **saltar este paso** esta vez —
  no se solicitaron rutas ni se corrió validación.
- Resultado: OK (skip explícito del usuario) — Stage 3b cerrada. Continúa a Stage 4
  (rotación de grid).

## Stage 4 — Rotación de grid
- Qué se hizo: grid de BTQ rotado de `012, 013, 014, 015` a `013, 014, 015, 016`
- Episodio que entra: EP.016 (ep-ref-tag "Pink Floyd — The Wall", quote "El primer
  ladrillo rara vez se siente como un muro. Se siente como sabiduría." — opción A
  confirmada por el usuario) | Episodio que sale: EP.012 (Bohemian Rhapsody)
- Archivo modificado: btq-production/website/index.html
- Resultado: OK

## Stage 5 — Deploy + verificación
- Qué se hizo: preflight (PASS — sin env vars, BOM/JSON limpios, Vercel autenticado como
  berandre2-7080) → gate de aprobación final (aprobado por el usuario: "Si") →
  `vercel --prod` desde btq-production/website/ → verificación HTTP → verificación
  Spotify (informativa)
- URL verificada: https://behind-thequeue.com → HTTP 200
- Verificación Spotify: INFO — EP.016 aún no visible en la página pública del show
  (https://open.spotify.com/show/5figtqa6zJxW1pE1sWJeEP); el listado más reciente
  muestra hasta EP.015. Posible lag de propagación — no indica problema con el deploy.
- Resultado: OK — episodio publicado y deploy verificado en vivo

## Post-pipeline — Reconciliación del calendario de lanzamiento
- Qué se hizo: se corrigieron las dos fuentes desactualizadas detectadas durante Stage 2
  (§13 de `btq-project/SKILL.md` y `episode-launch/SKILL.md`, ambas describían un
  calendario de 3 días Dom/Lun/Mié) para que reflejen la regla real confirmada por el
  usuario: lanzamiento domingo 8PM Colombia, plan de 4 días (Jueves intriga / Sábado
  calentamiento / Domingo 8PM lanzamiento / Martes refuerzo — fuente canónica: §10 de
  `btq-project/SKILL.md`). También se actualizaron las keywords de discovery (línea 11-12
  de btq-project/SKILL.md: "3 días redes BTQ" -> "4 días redes BTQ").
- Archivos modificados: C:\Users\andre\.claude\skills\btq-project\SKILL.md (línea 353,
  keywords), e:\...\kit-skill-creator\.claude\skills\episode-launch\SKILL.md (sección B —
  calendario reescrito de 3 a 4 días, con cita a §10 como fuente canónica)
- Nota: las entradas de estado por episodio (EP.013, EP.015, EP.016 — "Pending: ...
  redes 3/4 días", "Social plan: Completado ... Dom/Lun/Mié") se dejaron intactas por ser
  snapshots históricos de lo que se hizo en su momento, no la regla vigente.
- Resultado: OK — las tres fuentes ahora coinciden en la regla real (domingo 8PM, 4 días)

