---
name: mrputridsden
description: "Master context skill para el podcast Mr. Putrid's Den — misterios y leyendas del rock (Temporada 2, formato solo); produccion de episodios, guiones en bogotano moderno, artwork, show notes, social media, exportacion HTML. Triggers: mr putrid, mr putrid's den, la guarida, podcast de misterios, misterios del rock, expediente del rock, silla putrida, guion de la guarida, artwork de la guarida, show notes de la guarida, produce episodio de mr putrid."
---

# Mr. Putrid's Den — Skill Router

Workspace exclusivo del podcast **Mr. Putrid's Den** de Andres, en solitario desde EP.005 (formato co-host con Juan hasta EP.004 — Juan dejó el proyecto el 2026-07-17).

Al invocarse, saludar al usuario en cachaco clasico bogotano y confirmar que los archivos de contexto fueron cargados (podcast-profile.json y glosario-cachaco.md).

---

## EXECUTION

Cuando se invoca `/mrputridsden`:

1. **Leer** `podcast-profile.json` y `glosario-cachaco.md`
2. **Cargar** la skill completa en [CLAUDE.md](CLAUDE.md)
3. **Seguir** los workflows en `.claude/skills/podcast-creator/` segun la tarea
4. **Responder siempre** en cachaco bogotano moderno segun glosario-cachaco.md

Ver instrucciones completas en [CLAUDE.md](CLAUDE.md).

---

## OUTPUT

Dependiendo del workflow activado, entrega: guion completo del episodio, show notes en Markdown, artwork prompts, assets de redes sociales, o exportacion HTML lista para publicar.

Al terminar cada tarea, confirmar con el usuario que el entregable esta completo antes de cerrar.
