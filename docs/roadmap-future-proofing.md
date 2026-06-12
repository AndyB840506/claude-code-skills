# Roadmap — Future-proofing (transición Fable 5 → Opus 4.8)

**Contexto:** después del 2026-06-22, Fable 5 sale del plan actual de Claude
(pasa a pay-as-you-go). El plan es destilar el juicio implícito de las sesiones
con Fable en checklists explícitos y verificables, porque Opus 4.8 ejecuta
instrucciones explícitas de forma excelente pero infiere menos desde contexto
ambiguo.

**Principio rector:** todo lo que hoy "se sabe" tiene que quedar escrito como
regla con condición de disparo explícita ("cuando X, hacer Y, verificar con Z").
Si una regla no se puede verificar con grep/conteo/lectura, reescribirla hasta
que se pueda.

**Hecho el 2026-06-12 (esta sesión):**
- ✅ `docs/estandar-de-entregables.md` — estándar de calidad por tipo de entregable
- ✅ Regla de transición de modelo en CLAUDE.md del proyecto
- ✅ Reglas anti-repetición + regla de entrega de Juan en mrputridsden/CLAUDE.md
- ✅ Estrategia editorial BTQ data-driven en roadmap-btq.md + episode-launch

---

## Sesiones dedicadas (ventana 15–19 junio)

### Sesión 1 — Auditoría de conocimiento implícito: skills de producción
Revisar skill por skill preguntando: "¿qué hace falta saber que NO está escrito
aquí para ejecutar esto bien?" y escribirlo.

- [ ] `mrputridsden` (guiones MPD) — ¿el checklist anti-repetición es autosuficiente?
      ¿Las voces de Andrés y Juan están descritas con ejemplos de turnos buenos/malos?
- [ ] `episode-launch` (assets BTQ) — ¿los 4 bloques (SEO/social/YouTube/artwork)
      tienen criterios de done verificables?
- [ ] `episode-pipeline` — ¿los handoffs entre stages dicen exactamente qué archivo
      leer y qué estado verificar?
- [ ] `/btq-guion` (vive en otro repo) — pasarle los 3 requisitos nuevos
      (re-enganche ~60%, cierre comentable, checklist anti-repetición) si aún no los tiene.

### Sesión 2 — Auditoría: skills de sistema y rituales
- [ ] `crear-skill` — ¿produce skills que cumplen el estándar de verificabilidad?
- [ ] `/retrospective`, `skill-kit-auditor`, `/handoff` — ¿el ritual de cierre captura
      lo aprendido en formato regla-explícita o en prosa vaga?
- [ ] MEMORY.md — revisar que cada memoria tenga condición de uso clara y siga vigente.
- [ ] Handoffs viejos en `.agents/handoff/` — extraer reglas que quedaron solo ahí.

### Sesión 3 — Prueba de fuego + pendientes
- [ ] **Dry-run con Opus 4.8:** tomar una tarea real (ej. assets de EP.018 Mundial)
      y ejecutarla con Opus 4.8 siguiendo solo los docs escritos. Donde se quede corto,
      esa es una regla que falta — escribirla.
- [ ] **Re-evaluar graphify bajo el lente future-proofing.** Fue descartado antes
      ("herramienta dev, escala incorrecta, quema tokens") pero la intención de Andrés
      era este panorama: grafo de conocimiento del proyecto como respaldo externo al
      modelo. Decidir: ¿aporta algo que MEMORY.md + docs + handoffs no cubren ya?
- [ ] Verificar que el estándar de entregables cubre todos los tipos que se producen
      de verdad (¿faltó alguno? ej. propuestas, informes HTML).

## Continuo hasta el 22 de junio
- En cada cierre de sesión, el ritual (/retrospective → skill-kit-auditor → /handoff)
  pregunta además: "¿qué decidí hoy por juicio propio que debería ser una regla escrita?"
- EP.018 El Mundial se produce con el formato nuevo — sirve de validación del sistema.
