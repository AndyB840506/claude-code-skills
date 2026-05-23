---
name: prompt-reviewer
description: "Audita y mejora prompts, skills e instrucciones. Encuentra problemas de claridad, gaps de completitud e inefectividad. Propone fixes específicos con razonamiento. Para inglés, usar /prompt-reviewer-en. Triggers ES: revisar prompt, evaluar skill, mejorar instrucciones, auditar prompt, revisar skill, revisar instrucciones, esto no está claro, corregir mi prompt, mejorar mi prompt, auditar instrucciones, prompt no funciona."
---

# Prompt Reviewer — Audita y Mejora

Analiza prompts, skills e instrucciones para encontrar problemas de claridad, gaps e inefectividad. Propone fixes concretos y ejecutables.

**Regla principal:** Devuelve mejoras concretas — no crítica vaga. Cada hallazgo incluye el problema exacto, por qué importa y la solución.

**Siempre pide confirmación antes de aplicar cambios.**

---

## Inicio rápido

```
/prompt-reviewer
```

O especifica profundidad de análisis:

```
/prompt-reviewer quick
/prompt-reviewer thorough
```

---

## Cómo funciona

**Flujo de 4 pasos:**

1. **Elegir modo** — Quick (5 min) o Thorough (15 min)
2. **Auditar** — Encontrar problemas de claridad, gaps, patrones inefectivos
3. **Proponer** — Sugerir mejoras específicas con razonamiento
4. **Confirmar** — Aplicar solo si apruebas

---

## Resultado

Identificación de problemas + ejemplos antes/después + listo para aplicar o saltar

---

## Ver también

- [Qué encuentra](docs/findings.md) — Patrones y ejemplos
- [Flujo de ejecución](workflows/execute.md) — Paso a paso detallado

---

## EXECUTION

Has invocado `/prompt-reviewer`. Ahora ejecuta el flujo de auditoría de 4 pasos:

1. **Elegir modo** — Quick (5 min) o Thorough (15 min)
2. **Auditar** — Escanear problemas de claridad, gaps, inefectividad, violaciones de patrón
3. **Proponer** — Generar mejoras específicas con ejemplos antes/después
4. **Confirmar y aplicar** — Presentar hallazgos y aplicar solo si el usuario aprueba

Ver [Flujo completo](workflows/execute.md) para instrucciones detalladas paso a paso.

**Resultado:** Skills revisadas y mejoradas (si se aprueba).
