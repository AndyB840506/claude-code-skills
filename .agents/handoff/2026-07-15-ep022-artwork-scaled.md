# Handoff: BTQ EP.022 — portada en 3 formatos, generada en el escritorio

**Date:** 2026-07-15 (miércoles)
**Status:** Complete — Stage A sigue cerrada; ahora las 3 variantes de portada (1:1,
16:9, 9:16) están generadas, aprobadas por Andy y en la carpeta de entrega. Retrospectiva
aplicada (6/6), auditoría del kit sin hallazgos.

---

## What We Accomplished This Session

- **Contexto de máquina:** la sesión empezó en el escritorio (E:\AI, RTX 3080 Ti), pero
  los archivos de prueba de la portada 1:1 aprobados el 2026-07-14 solo existían en
  D:\ del portátil. A pedido de Andy, se regeneró todo desde cero en vez de transferir
  archivos manualmente.
- **Portada 1:1 a 3000×3000 producción:** escena nativa Z-Image Turbo 1536×1536 (3
  iteraciones — v1 salió con figura masculina y checkbox final como cuadro sólido; v2
  corrigió género (mujer, coherente con "Ana" del guion) y contraste del checkbox; v3
  redujo un patrón de fondo tipo circuito que competía con el texto) → escalada con
  RealESRGAN_x4plus + resize exacto a 3000×3000. Tira de íconos de plataforma generada
  en batch de 4 (las 4 limpias). Compuesta con `portada-compose.py`.
- **Portada 16:9 (1920×1080, thumbnail):** escena nueva nativa (2 iteraciones — v1 con
  checklist en dos columnas y varios casilleros vacíos dispersos, diluía el chiste
  visual; v2 forzó una sola columna con solo el último casillero vacío). Tipografía
  compuesta con plantilla NUEVA `comfyui/templates/cover-16x9-compose.py` (título +
  subtítulo alineados a la izquierda, sin footer).
- **Portada 9:16 (1080×1920, historia):** 2 intentos de generar la escena de cero
  fallaron en controlar la composición extrema (figura en tercio superior, resto negro).
  Se cambió de estrategia: derivada por PIL de la escena 1:1 YA aprobada (recorte
  superior + relleno de negro de marca exacto, con margen para el wordmark) — 0 riesgo
  de reintroducir errores ya corregidos. Compuesta con la MISMA `portada-compose.py`.
- **Bug real encontrado y corregido** (lo detectó Andy, no la revisión visual): la tira
  de íconos se pegaba de forma opaca sobre el footer; su fondo `(0,0,0)` no coincidía
  con el negro del footer `(10,10,10)`, dejando una costura rectangular visible. Fix en
  `comfyui/templates/portada-compose.py`: máscara de alfa derivada de la diferencia
  contra negro puro. Verificado con muestreo de píxeles (footer y huecos entre íconos
  leen exactamente `10,10,10` tras el fix). Aplica retroactivamente a cualquier portada
  o quote card futura que reutilice la plantilla.
- **Retrospectiva aplicada (6/6):** recetas de resolución (3000×3000 vs nativo directo),
  límite de control por prompt en composiciones verticales extremas, regla general de
  compositing IA-sobre-negro-programático, refuerzo del paso de verificación (muestrear
  píxeles en costuras, no solo mirar el preview reducido), y referencias nuevas en
  `episode-launch/docs/brand-constants.md` para que EP.023+ reutilicen el flujo de
  16:9/9:16 sin reinventar nada. Detalle completo en
  `btq-production/pipeline-audit-ep022.md` §Extra 2.
- **Auditoría del kit:** 28 SKILL.md, ninguno excede 50 líneas, sin archivos sueltos —
  sin hallazgos.
- **Commit y push:** cambios de esta sesión (docs + plantilla nueva + fix) ya están en
  `main` (`675755b` + los de retrospectiva).

## Where We Paused

**Last action:** aplicando aprendizajes de retrospectiva y corriendo la auditoría del kit.
**Next action:** nada de agente — Andy graba EP.022 el viernes 2026-07-17. Al retomar
con el audio: "corre el pipeline para EP.022" → transcripción (Stage B).
**Blockers:** ninguno de agente.

## Files to Read First

- `btq-production/pipeline-state-ep022.md` — estado del episodio, las 3 portadas ya
  están marcadas como listas con sus rutas de archivo.
- `btq-production/pipeline-audit-ep022.md` §Extra 2 — detalle completo de las
  iteraciones, el bug y el fix.
- `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\` (D:\ en el portátil) — las 3 portadas finales
  (`-1x1-approved-3000.png`, `-16x9.png`, `-9x16.png`) + assets de respaldo (escena sin
  texto, tira de íconos).
- `episode-launch/docs/brand-constants.md` §Generación LOCAL de portadas — flujo
  actualizado con los 3 formatos y sus plantillas/técnicas.

## Notes / Gotchas

- El servidor de ComfyUI del **escritorio** quedó **corriendo** a pedido de Andy (no se
  detuvo al cerrar esta sesión) — si se retoma en el escritorio, ya está arriba; si se
  retoma en el portátil, hay que lanzar el suyo aparte.
- Las 3 portadas de producción viven en `E:\Podcast\BTQ\EP 22\...` (escritorio) — el
  portátil tendría que ver el mismo contenido en `D:\Podcast\BTQ\EP 22\...` solo si se
  copian manualmente; no hay sync automático entre las dos unidades de podcast.
- `comfyui/templates/portada-compose.py` cambió (fix de costura) — cualquier portada o
  quote card generada ANTES de este fix (ej. las de EP.021) no se revisó retroactivamente
  por esta costura específica; si se nota algo raro en el footer de esas, es la misma
  causa.

## Questions to Answer

- Tema de EP.023 — sin definir, próxima decisión después de que EP.022 se publique
  (patrón: alternar pilar SEO con pop-culture; candidatos pop-culture pendientes:
  Metallica, Matrix, Star Wars).
- ¿Revisar retroactivamente las quote cards de EP.021 por la misma costura de negro
  (footer vs asset IA)? No es bloqueante, esas ya están publicadas y aprobadas.
