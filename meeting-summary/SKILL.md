---
name: meeting-summary
description: "Genera resumen estructurado de reuniones a partir de notas manuales o emails de note takers. Triggers: resume esta reunión, genera resumen de reunión, procesa mis notas, resumen de meeting, /meeting-summary"
---

# Meeting Summary

Convierte tus notas de reunión (escritas a mano o copiadas de un note taker como
Fireflies, Otter o Notion AI) en un resumen estructurado con dos versiones: una
personal (Markdown) y una lista para compartir con el equipo (texto limpio).

## Workflow

Sigue `workflows/summarize.md`:
1. Da la bienvenida y pide las notas (texto libre o email del note taker).
2. Detecta el tipo de input y pide los datos faltantes (nombre, fecha, participantes).
3. Extrae contexto, decisiones, deliverables (responsable + fecha), próximos pasos y
   pendientes. Usa `[por confirmar]` si falta un dato — nunca inventar.
4. Genera la Versión Personal (Markdown con checkboxes) y la Versión para Compartir
   (texto profesional listo para email/Slack/Notion).
5. Muestra el resumen final y ofrece ajustes.
