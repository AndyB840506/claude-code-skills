---
name: session-close
description: "Complete session closing workflow: analyze learnings (retrospective), review skill quality (prompt-reviewer), organize skills (skill-management), backup to GitHub + auto-sync to Google Drive. Run at end of session to consolidate work and prepare for next session. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session, session complete, finish session, session review workflow."
---

# Session Close — Complete Closing Workflow

Guía completo de cierre de sesión. Ejecuta 5 pasos en orden: análisis de learnings → revisión de skills → organización → respaldo a GitHub → sincronización automática a Google Drive.

**Orden del flujo:**
1. **Retrospective** — Analiza la sesión y extrae learnings
2. **Prompt Reviewer** — Revisa y mejora los skills creados/modificados
3. **Skill Management** — Organiza la estructura de skills si es necesaria
4. **Handoff** — Respalda la sesión (git push a GitHub)
5. **Auto-sync to Google Drive** — Sincroniza automáticamente los cambios a G:\My Drive

---

## Cómo Usar

Simplemente escribe:

```
/session-close
```

O ejecuta manualmente en orden si prefieres:

```
/retrospective                    # Paso 1: Analizar aprendizajes
/prompt-reviewer                  # Paso 2: Revisar skills
/skill-management                 # Paso 3: Organizar estructura
/handoff                          # Paso 4: Respaldar a GitHub
                                  # Paso 5: Auto-sync a Google Drive (automático)
```

---

## Detalles de Cada Paso

### Paso 1: Retrospective
Analiza la sesión completa para extraer:
- Correcciones del usuario (cambios de enfoque, feedback)
- Trabajo que fue reiterativo (3+ versiones del mismo artifact)
- Pasos que se improvisaron pero no están en los skills
- Patrones que funcionaron bien

**Output:** Propuestas de cambios a skills con diffs listos para aplicar

---

### Paso 2: Prompt Reviewer
Revisa todos los skills modificados hoy:
- Claridad de instrucciones
- Completitud de triggers
- Consistencia de estructura
- Calidad de ejemplos

**Output:** Lista de mejoras sugeridas (es opcional aplicarlas)

---

### Paso 3: Skill Management
Verifica la organización:
- Todos los skills en estructura correcta (.claude/skills/nombre/SKILL.md)
- SKILL.md bajo 50 líneas con router claro
- Workflows, templates, docs en carpetas apropiadas
- No hay archivos .md sueltos interfiriendo

**Output:** Recomendaciones si algo necesita reorganización

---

### Paso 4: Handoff
Respalda todo:
- Git add/commit de cambios con timestamp
- Git push a GitHub
- Confirmación de respaldo completado

**Output:** Confirmación de backup + commit hash

---

### Paso 5: Auto-sync to Google Drive
Sincronización automática posterior:
- Copia todos los cambios a `G:\My Drive\kit-skill-creator\`
- Google Drive for Desktop sincroniza automáticamente a la nube
- Sin necesidad de intervención manual
- Confírma que la sincronización se completó

**Output:** Confirmación de sincronización + timestamp

**Automatización:**
Este paso se ejecuta automáticamente después de que `handoff` completa. No requiere acción manual.

---

## Flujo Recomendado

**Fin de sesión productiva:**
```
1. /session-close
2. Revisa las propuestas de retrospective
3. Aplica cambios de prompt-reviewer si necesita
4. Deja que handoff respaldes todo
```

**Fin de sesión simple:**
```
Si no hiciste cambios en skills, puedes saltar los pasos 1-3 y solo:
/handoff
```

**Desarrollo iterativo:**
```
Si estás refinando un skill continuamente:
/skill-management    # Solo organización
/handoff            # Respaldar cambios
```

---

## Tips

- **Ejecuta al final del día** — especialmente después de crear o modificar skills
- **No es obligatorio** — puedes ejecutar los pasos individuales en cualquier orden
- **Aplica solo lo que tenga sentido** — no todas las sugerencias aplican siempre
- **Git push solo con cambios reales** — handoff no hace push si no hay cambios
- **Automatización completa** — una vez termina handoff, Google Drive se sincroniza automáticamente
- **Doble respaldo** — después de `/session-close`, tu trabajo está en GitHub + Google Drive
- **Sin esperas** — la sincronización a Google Drive es instantánea (Google Drive for Desktop la sube automáticamente)
