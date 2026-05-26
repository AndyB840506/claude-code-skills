---
name: mrputridsden
description: "Master context skill para el podcast Mr. Putrid's Den — producción de episodios, guiones en cachaco clásico bogotano, artwork, show notes, social media, exportación HTML. Triggers: mr putrid, mr putrid's den, la guarida, podcast metal, podcast rock, guion episodio, episodio gurida, silla putrida, silla pútrida, artwork podcast, show notes, produce episode, podcast script, cachaco podcast."
---

# Mr. Putrid's Den — Skill Router

Workspace exclusivo del podcast **Mr. Putrid's Den** de Andrés y Juan.

---

## EXECUTION

Cuando se invoca `/mrputridsden`:

1. **Leer** `podcast-profile.json` y `glosario-cachaco.md`
2. **Cargar** la skill completa en [CLAUDE.md](CLAUDE.md)
3. **Seguir** los workflows en `.claude/skills/podcast-creator/` según la tarea
4. **Responder siempre** en cachaco clásico bogotano de los 40's

Ver instrucciones completas en [CLAUDE.md](CLAUDE.md).
