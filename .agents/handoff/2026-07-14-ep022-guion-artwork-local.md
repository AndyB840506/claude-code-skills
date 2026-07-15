# Handoff: BTQ EP.022 — guion aprobado + portada generada localmente

**Date:** 2026-07-14 (martes)
**Status:** Complete — Stage A del pipeline cerrada; portada 1:1 de prueba aprobada por
Andy; retrospectiva aplicada (5/5); auditoría del kit sin hallazgos.

---

## What We Accomplished This Session

- **EP.022 confirmado y guionizado.** Tema elegido por Andy tras un menú de 3 candidatos
  (rotación/Capital Humano, cost-to-serve/Service-Profit Chain, costo de mala
  calidad/Crosby) — ganó **costo de la mala calidad en call center**, anclado en Philip
  Crosby ("Quality Is Free", 1979), con ángulo P&L explícito a pedido de Andy (mismo
  patrón que EP.020: métrica + teoría real citable).
- **Guion completo y aprobado**: `btq-production/launch-assets/EP022-costo-calidad-guion.html`
  — 4.674 palabras, ~42.2 min medidos (dentro del estándar 40-45). Casos verificados por
  web antes de escribir: Crosby/ITT, Samsung Note 7 ($5.300M, presión de cronograma vs.
  iPhone 7), SQM Group (economía de la llamada repetida), PwC (32% se va tras una mala
  experiencia, ~49% en LatAm), Pronovost/Keystone Michigan, Boeing Model 299 (origen del
  checklist de vuelo, 1935). Se detectó y corrigió una cifra sin verificar (horas de vuelo
  del B-17) antes de entregar — reemplazada por el dato real (12.731 unidades).
- **Prompts de artwork v3 preparados**: `btq-production/launch-assets/EP022-costo-calidad-artwork-v3.md`
  — segundo episodio sin referente pop resuelto con un símbolo literal del contenido
  (checklist/checkboxes dorados, mismo criterio que la diana de EP.020, ahora confirmado
  2x).
- **Portada 1:1 generada y APROBADA localmente** (D:\AI, Z-Image Turbo, RTX 3060) — a
  pedido de Andy, adelantando pruebas de artwork antes de grabar. Iteración: escena sola
  (2 rondas hasta lograr void-black + rim light dorado + checkbox vacío legible) → intento
  de tipografía completa en un solo prompt (íconos fila 1 salieron bien, pero TODO el
  texto con typos: "BEHIND THE QEQUE") → **solución híbrida**: íconos de plataforma
  generados aislados (fondo negro, sin texto/escena, 4/4 limpios) + todo el texto
  compuesto con PIL. Plantilla nueva `comfyui/templates/portada-compose.py` (2 rondas de
  ajuste de tamaño de "BTQ"/"EP.22" a pedido de Andy). Archivos finales en
  `D:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\` (test a 1024×1024, falta escalar a 3000×3000
  real).
- **Retrospectiva aplicada (5/5)**: lección de íconos-aislados-vs-texto-mezclado
  documentada en `comfyui/docs/prompting.md` + sincronizada en
  `imagen-a-prompt/docs/prompt-formats.md`; técnica híbrida + fuente sustituta (Impact)
  documentada en `episode-launch/docs/brand-constants.md`; regla de verificación
  extendida a pasadas de expansión en `guion-style-btq.md`; nota de EP.020 actualizada a
  "confirmado 2x".
- **Auditoría del kit**: 28 SKILL.md, ninguno excede 50 líneas — sin hallazgos, nada que
  aplicar.
- **Roadmap actualizado**: EP.022 → estado `guion listo`.

## Where We Paused

**Last action:** retrospectiva aplicada, escribiendo este handoff.
**Next action:** nada de agente — Andy graba el episodio (previsto viernes
2026-07-17). Al retomar con el audio: "corre el pipeline para EP.022" → transcripción
(Stage B).
**Blockers:** ninguno de agente.

## Files to Read First

- `btq-production/launch-assets/EP022-costo-calidad-guion.html` — guion aprobado, leer
  antes de grabar.
- `btq-production/pipeline-state-ep022.md` — estado del episodio, incluye nota de la
  portada ya aprobada.
- `D:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\BTQ-EP022-COVER-1x1-approved.png` — portada
  aprobada (test 1024×1024, pendiente escalar a producción).
- `episode-launch/docs/brand-constants.md` §Generación LOCAL de portadas — flujo híbrido
  nuevo, seguirlo para 16:9/9:16 de EP.022 y futuras portadas locales.

## Notes / Gotchas

- La portada final de EP.022 quedó a **1024×1024** (resolución de prueba) — falta
  escalar/regenerar a 3000×3000 antes de considerarla lista para producción real. El
  archivo de escena sin tipografía (`BTQ-EP022-COVER-1x1-scene-only.png`) y la fuente de
  íconos (`BTQ-icon-strip-source.png`) quedaron guardados aparte para no tener que
  regenerar desde cero si se necesita rehacer a mayor resolución.
- El servidor de ComfyUI en el portátil se dejó **detenido** al cerrar (TaskStop) — hay
  que relanzarlo si se retoma el artwork.
- Sigue pendiente, de sesiones anteriores, un cambio sin commitear en
  `freelance-gig/docs/reuse-map.md` — no tocado esta sesión, no se sabe si es trabajo en
  progreso de Andy o un residual; revisar antes de descartarlo.

## Questions to Answer

- ¿Escalar la portada aprobada a 3000×3000 antes o después de la grabación? No es
  bloqueante para grabar.
- Tema de EP.023 — sin definir, próxima decisión después de que EP.022 se publique
  (patrón: alternar pilar SEO con pop-culture; candidatos pop-culture pendientes:
  Metallica, Matrix, Star Wars).
