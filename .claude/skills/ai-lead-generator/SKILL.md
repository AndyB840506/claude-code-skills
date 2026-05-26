---
name: ai-lead-generator
description: "Genera leads de negocio reales con IA buscando en Google y redes sociales. Busca empresas que necesitan lo que vendes, las puntúa 0-100, categoriza por PREMIUM/HOT/WARM/COLD, genera reporte HTML descargable como PDF y CSV. Triggers: 'buscar leads', 'generar leads', 'encontrar clientes', 'lead generation', 'prospección', 'find leads', 'find prospects'."
---

# AI Lead Generator — Find Real Business Leads

Busca leads reales en Google, los puntúa 0-100, y genera reportes HTML/CSV.

**Regla fundamental:** Nunca inventa leads. Cada lead proviene de una búsqueda real.

---

## Quick Start

```
/ai-lead-generator
```

Describe qué vendes y a quién le quieres vender.

---

## How It Works

Follow [Execution Workflow](workflows/execute.md):

1. Understand requirements (product, target market)
2. Execute real Google searches
3. Score each lead (0-100)
4. Categorize by probability (PREMIUM/HOT/WARM/COLD)
5. Generate HTML/PDF/CSV reports

---

## Output

✓ Real leads with verified info  
✓ Puntuación individual (0-100)  
✓ Probability categories  
✓ Reportes profesionales  
✓ CSV para CRM

---

## Documentation

- [Execution Workflow](workflows/execute.md) — Step-by-step process
- [Search Modes](docs/search-modes.md) — Nativo vs Serper vs Híbrido

---

## EXECUTION

Has invocado `/ai-lead-generator`. Ejecuta el flujo de 5 pasos:

1. **Entender requisitos** — Preguntar: ¿qué vendes?, ¿quién es tu cliente ideal? (industria, tamaño, ubicación)
2. **Buscar leads reales** — Usar WebSearch para encontrar empresas reales. Nunca inventar leads.
3. **Puntuar cada lead (0-100)** — Relevancia (0-30) + señales de intención (0-30) + accesibilidad (0-20) + fit (0-20)
4. **Categorizar** — PREMIUM (80-100) / HOT (60-79) / WARM (40-59) / COLD (0-39)
5. **Generar reporte** — HTML con tabla de leads, puntajes y próximos pasos. Exportar CSV para CRM.

Ver [Execution Workflow](workflows/execute.md) para instrucciones detalladas.

**Resultado:** Reporte HTML/CSV con leads reales verificados y puntuados.
