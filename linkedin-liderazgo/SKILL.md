---
name: linkedin-liderazgo
description: "Genera artículos largos de LinkedIn sobre liderazgo empresarial en la voz real del usuario, evitando los patrones típicos que delatan texto de IA (aperturas genéricas, exceso de guiones largos, cierres en 'en conclusión', balance vacío sin postura). Triggers: artículo de LinkedIn, post de liderazgo, escribe sobre liderazgo, artículo sobre liderazgo empresarial, /linkedin-liderazgo."
---

# LinkedIn — Liderazgo Empresarial

Genera artículos de LinkedIn (600-1200 palabras) sobre liderazgo empresarial que suenen
a una persona real escribiendo, no al patrón genérico de un modelo de lenguaje. La
calidad se mide contra un checklist verificable, no contra impresión subjetiva.

Dos piezas separadas:
- **Voz** — un perfil calibrado una vez con el usuario y reusado en cada artículo
  (`perfil-voz.md`, se crea la primera vez que se invoca la skill).
- **Anti-patrones de IA** — checklist concreto en `docs/anti-patrones-ia.md`, aplicado
  a todo borrador antes de mostrarlo.

## Workflow

Sigue `workflows/generar-articulo.md`:
1. Si no existe `perfil-voz.md` en esta carpeta, calibra la voz con preguntas cortas y
   lo guarda — no vuelve a preguntar en sesiones futuras.
2. Pide el tema del artículo (si no vino ya en la invocación).
3. Genera el artículo aplicando el perfil de voz.
4. Corre el checklist de `docs/anti-patrones-ia.md` contra el borrador y reporta una
   tabla patrón → encontrado → corregido.
5. Muestra el artículo final + la tabla de checklist. Ofrece ajustes.
6. Pregunta si quiere guardarlo en archivo; si sí, lo guarda en
   `C:\Users\andre\repos\linkedin-articulos\` (nunca dentro de `~/.claude/`).

## Límite explícito — watermark vs. estilo

Claude aplica un watermark de texto imperceptible a nivel de modelo a TODO lo que
genera (confirmado en support.claude.com/articles/16266773, 2026-09-04) — no es
opcional, no se puede desactivar, y viaja con el texto al copiarlo. Esta skill NO
intenta detectarlo, removerlo ni evadirlo — sería construir evasión de un sistema de
transparencia sobre contenido de IA, no una mejora de escritura.

Lo que sí ataca esta skill es el *estilo* reconocible como IA (lo que de hecho marcan
herramientas de terceros tipo GPTZero/Originality.ai): aperturas genéricas, ritmo
uniforme, cierres en "en conclusión", balance sin postura — ver
`docs/anti-patrones-ia.md`. Si un usuario pide explícitamente "quita el watermark" o
"evita que se detecte que es de Claude" en el sentido técnico, aclarar esta distinción
en vez de intentar construirlo.
