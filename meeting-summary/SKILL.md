---
name: meeting-summary
description: "Genera resumen estructurado de reuniones a partir de notas manuales o emails de note takers. Triggers: resume esta reunión, genera resumen de reunión, procesa mis notas, resumen de meeting, /meeting-summary"
---

# Meeting Summary

Este skill convierte tus notas de reunión (escritas a mano o copiadas de un note taker como Fireflies, Otter o Notion AI) en un resumen estructurado con dos versiones: una personal y una lista para compartir con el equipo.

## Step 1 — Recopilar información

Pregunta al usuario:
1. "Pega tus notas aquí — pueden ser texto libre, desordenado, o el email completo de tu note taker."
2. Luego pregunta: nombre de la reunión, fecha, y participantes (si no están ya en el texto).

Infiere el tipo de input automáticamente:
- Si tiene formato de email o secciones predefinidas → es de un note taker
- Si es texto libre y desordenado → son notas manuales

## Step 2 — Procesar y estructurar

Extrae del texto:
- **Contexto:** propósito de la reunión en 1-2 oraciones
- **Decisiones tomadas:** lista puntual, solo lo que fue confirmado
- **Deliverables:** ítem + responsable + fecha límite (si se menciona)
- **Próximos pasos:** acciones concretas pendientes
- **Temas sin resolver:** preguntas abiertas o temas que quedaron pendientes

Si falta información clave (ej: responsable de un deliverable), márcalo como `[por confirmar]` — nunca inventes datos.

## Step 3 — Generar dos versiones

**Versión Personal (Markdown compacto):**
```
# [Nombre reunión] — [Fecha]
👥 [Participantes]

## Decisiones
- ...

## Deliverables
- [ ] [Ítem] → [Responsable] | [Fecha]

## Próximos pasos
- ...

## Pendientes
- ...
```

**Versión para compartir (texto limpio):**
Redacta en tono profesional, sin símbolos markdown, lista para pegar en email, Slack o Notion. Incluye una línea de introducción tipo: *"A continuación el resumen de nuestra reunión del [fecha]:"*

---

## EXECUTION

Has invocado `/meeting-summary`. Ejecuta en este orden:

1. **Da la bienvenida** con este mensaje: "¡Hola! Vamos a generar tu resumen de reunión. Pega tus notas aquí — pueden ser texto libre o el email de tu note taker (Fireflies, Otter, etc.)."

2. **Recibe el input** y detecta automáticamente si es nota manual o de note taker.

3. **Pregunta los datos faltantes** (solo si no están en el texto): "¿Cuál es el nombre de la reunión, la fecha y quiénes participaron?"

4. **Procesa el contenido** y extrae: contexto, decisiones, deliverables (con responsable y fecha), próximos pasos, y temas pendientes. Usa `[por confirmar]` si falta un dato — nunca lo inventes.

5. **Genera la Versión Personal** en Markdown con checkboxes para deliverables.

6. **Genera la Versión para Compartir** en texto limpio y profesional, lista para copiar a email/Slack/Notion.

7. **Muestra resumen final:** "✅ Resumen generado a partir de [tipo de input]. Se identificaron [N] deliverables y [N] próximos pasos. ¿Quieres ajustar algo?"

**Resultado:** Dos versiones del resumen listas para usar, sin datos inventados.