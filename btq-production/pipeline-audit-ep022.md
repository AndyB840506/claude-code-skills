# Pipeline Audit — BTQ EP.022

## Stage A — Roadmap y pre-producción

### Paso 1 — Confirmar episodio
- Andy confirmó el pilar SEO como dirección general en conversación (retomando el
  handoff de cierre de EP.021, que dejó el tema de EP.022 como pregunta abierta), y
  luego el ángulo P&L específico. Se presentaron 3 candidatos de métrica + teoría real
  citable (costo de rotación/Capital Humano de Becker, cost-to-serve/Service-Profit
  Chain de Heskett, costo de mala calidad/"Quality Is Free" de Crosby) vía
  AskUserQuestion — Andy eligió Crosby.
- Roadmap actualizado: fila EP.022 agregada a `roadmap-btq.md` con el tema confirmado,
  estado `en roadmap` → `guion listo` tras aprobación.

### Paso 2 — Guion
- Qué se hizo: `/btq-guion` no existe (confirmado, ver nota en `episode-pipeline`
  routing) — guion escrito directamente siguiendo `btq-production/guion-style-btq.md`.
  Investigación web previa para verificar todos los datos antes de escribir (regla 6):
  Philip Crosby / "Quality Is Free" (1979, ITT, costo de no conformidad ~20-25% de
  ventas), Samsung Galaxy Note 7 (2016, $5.300M, presión de cronograma vs. iPhone 7),
  SQM Group (costo de llamada repetida, ahorro por punto de FCR), PwC "Experience Is
  Everything" (2018, 32% abandona tras una mala experiencia, ~49% en LatAm), Peter
  Pronovost / Keystone Initiative Michigan (NEJM 2006, checklist de vía central),
  Boeing Model 299 / origen del checklist de vuelo (1935).
- Corrección durante la escritura: una primera versión incluía una cifra de horas de
  vuelo del B-17 en la Segunda Guerra Mundial sin verificar — se detectó antes de
  entregar y se reemplazó por el dato real y verificado (12.731 unidades construidas,
  tercer bombardero más producido de la historia).
- Publicado como Artifact (copia sin `<!DOCTYPE>/<html>/<head>/<body>`, mismo `<style>`
  + `<div class="container">`) para revisión de Andy — aprobado sin cambios.
- Lint aplicado: 4.674 palabras contadas (p.line + remate + dato + sub) → ~42.2 min a
  150 wpm + expansión 35.5%, dentro de 40-45 min. 3 REMATE (máx 3-4). Refrán central
  ("la calidad es gratis") 3 veces en el guion hablado, cada una con función narrativa
  distinta (tease en el Hook, cita del título del libro, cierre canónico) — dentro del
  máx 3. 0 "imagínense", 0 "me vuela la cabeza". Sin bloque "Mito o Realidad" aparte.
  Sin meta-anuncios de estructura.
- Archivos generados: `btq-production/launch-assets/EP022-costo-calidad-guion.html`
- Resultado: OK — aprobado por Andy 2026-07-14

### Paso 3 — Prompts de artwork
- Qué se hizo: mismo desafío que EP.020 (pilar SEO sin referente pop) — se buscó un
  símbolo literal del propio contenido del episodio en vez de un patrón decorativo
  desconectado, siguiendo el precedente documentado en
  `EP020-metricas-artwork-v3.md`. Elegido: un patrón de checklist/checkboxes dorados
  (el episodio gira en torno a checklists — Pronovost, Boeing, Aplicable Hoy #2), con
  un checkbox final deliberadamente sin marcar como el gancho visual. Figura: la
  supervisora de QA de la escena de apertura del guion (Ana), de espaldas, hombro con
  el monitor de revisión de llamadas. Se mantiene el veto de círculos/anillos/diana
  vigente desde EP.021 (brand-constants.md §3).
- Archivos generados: `btq-production/launch-assets/EP022-costo-calidad-artwork-v3.md`
  (prompts 1:1 y 16:9 completos; 9:16 queda para derivar del 1:1 aprobado, mismo patrón
  de adaptación de episodios previos — no generado en este documento)
- Resultado: OK — prompts listos, pendiente generación real en Flow por Andy (no
  bloqueante para cerrar Stage A, igual que el patrón de episodios anteriores)

### Paso 4 — Archivo de estado
- Qué se hizo: `pipeline-state-ep022.md` creado, `roadmap-btq.md` actualizado a
  `guion listo`.
- Resultado: OK — pausa natural, esperando grabación

### Extra — pruebas de artwork local (ComfyUI, adelantadas antes de la grabación)
- Qué se hizo: a pedido de Andy, se probó generar la portada 1:1 localmente (D:\AI,
  Z-Image Turbo) en vez de Flow, para validar la dirección visual antes de grabar.
  - v1 (escena completa con prompt customizado): quedó con tono cálido tipo "foto de
    oficina", lejos del void-black + rim light dorado que pide la marca. FAIL parcial.
  - v2 (prompt ajustado: cuarto en negro total, monitor en dark-mode con glow dorado,
    un checkbox final claramente vacío entre 4 marcados): PASS — validó la dirección
    conceptual (checklist como símbolo literal, mismo criterio que la diana de EP.020).
  - Prueba de tipografía completa en un solo prompt (bloque congelado con nombres de
    íconos, a pedido de Andy citando su experiencia en EP.21): los íconos de la fila 1
    (Facebook/Instagram/TikTok) salieron reconocibles y a color, pero TODO el texto
    horneado por el modelo salió con typos ("BEHIND THE QEQUE", "Behind the Queve",
    "Mada Calidad") y faltó la fila 2 de íconos. Confirmado y corregido según feedback
    de Andy.
  - Solución híbrida: íconos de plataforma generados en una imagen aparte (fondo negro
    puro, sin texto/escena) — 4/4 variantes del batch salieron limpias, ambas filas
    completas. Compuestos con PIL sobre la escena v2 junto con todo el texto (wordmark,
    BTQ, título, EP.22) vía plantilla nueva `comfyui/templates/portada-compose.py`
    (recorte automático por bounding-box del strip de íconos).
  - 2 rondas de ajuste de tamaño de tipografía dorada (BTQ/EP.22) a pedido de Andy —
    de ~0.022×H a ~0.040×H (BTQ) y ~0.050×H (EP.22).
  - Técnica documentada en memoria `btq_local_portada_hybrid_typography` para
    reutilizar en futuras portadas BTQ locales.
- Archivos finales copiados a `D:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\`:
  `BTQ-EP022-COVER-1x1-approved.png` (aprobada por Andy), `BTQ-EP022-COVER-1x1-scene-only.png`
  (escena sin tipografía, por si se necesita recomponer), `BTQ-icon-strip-source.png`
  (fuente de íconos recortable para reutilizar en 16:9/9:16 y futuras portadas).
- Pendiente: escalar a 3000×3000 real (test corrió a 1024×1024); derivar 16:9 y 9:16
  con el mismo criterio cuando se necesiten.
- Resultado: OK — Andy aprobó el resultado final ("Asi quedo perfecto")
