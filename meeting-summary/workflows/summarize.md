# Execution

Has invocado `/meeting-summary`. Ejecuta en este orden.

## Step 1 — Recopilar información

1. **Da la bienvenida:** "¡Hola! Vamos a generar tu resumen de reunión. Pega tus notas
   aquí — pueden ser texto libre o el email de tu note taker (Fireflies, Otter, etc.)."
2. Luego pide: nombre de la reunión, fecha, y participantes (si no están ya en el texto).

Infiere el tipo de input automáticamente:
- Formato de email o secciones predefinidas → note taker
- Texto libre y desordenado → notas manuales

## Step 2 — Procesar y estructurar

Extrae del texto:
- **Contexto:** propósito de la reunión en 1-2 oraciones
- **Decisiones tomadas:** lista puntual, solo lo confirmado
- **Deliverables:** ítem + responsable + fecha límite (si se menciona)
- **Próximos pasos:** acciones concretas pendientes
- **Temas sin resolver:** preguntas abiertas o pendientes

Si falta información clave (ej. responsable de un deliverable), márcalo como
`[por confirmar]` — nunca inventes datos.

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
Redacta en tono profesional, sin símbolos markdown, lista para pegar en email, Slack o
Notion. Incluye una línea de introducción tipo: *"A continuación el resumen de nuestra
reunión del [fecha]:"*

## Step 4 — Resumen final

"✅ Resumen generado a partir de [tipo de input]. Se identificaron [N] deliverables y
[N] próximos pasos. ¿Quieres ajustar algo?"

**Resultado:** dos versiones del resumen listas para usar, sin datos inventados.
