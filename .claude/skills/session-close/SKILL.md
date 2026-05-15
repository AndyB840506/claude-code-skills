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
4. **Handoff** — Crea documento + respalda a GitHub (git push)
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

### Paso 4: Handoff — Documento + GitHub Backup
Ejecuta handoff automáticamente con dos acciones:

**Acción 1: Crear documento de handoff**
- Escribe a `.agents/handoff/YYYY-MM-DD-session-close.md`
- Documenta qué se logró
- Documenta dónde pausamos
- Documenta blockers o próximos pasos

**Acción 2: GitHub Backup (Automático)**
- `git add -A` de todos los cambios
- `git commit -m "Session: session-close [timestamp]"`
- `git push origin main` a GitHub
- Confirmación con commit hash

**Output:** Documento de handoff + Confirmación de backup + commit hash

---

### Paso 5: Auto-sync to Google Drive
Sincronización automática (requiere Google Drive for Desktop instalado):
- Copia `.agents/handoff/` y `.claude/` a `G:\My Drive\kit-skill-creator\`
- Google Drive for Desktop detecta cambios y sincroniza automáticamente a la nube
- Sin intervención manual — la sincronización sucede automáticamente en background

**Output:** Confirmación que archivos fueron copiados a Google Drive

**Requisito:**
Google Drive for Desktop debe estar instalado y configurado en `G:\My Drive\`. Si no está instalado, el paso se salta (solo GitHub queda respaldado).

---

## Flujo Recomendado

**Fin de sesión productiva (recomendado):**
```
/session-close
  ↓ Paso 1: Retrospective (analiza learnings)
  ↓ Paso 2: Prompt Reviewer (revisa skills)
  ↓ Paso 3: Skill Management (organiza)
  ↓ Paso 4: Handoff (crea documento + git push)
  ↓ Paso 5: Auto-sync Google Drive (automático)
  
✓ Todo respaldado automáticamente
```

**Fin de sesión simple:**
```
Si no hiciste cambios en skills, solo ejecuta:
/handoff
  → Crea documento de continuidad
  → Git commit + push automáticamente
```

**Solo respaldo sin análisis:**
```
Si solo quieres respaldar sin retrospective/revision:
/handoff
```

---

## Tips

- **Ejecuta al final del día** — especialmente después de crear o modificar skills
- **No es obligatorio** — puedes ejecutar los pasos individuales en cualquier orden
- **Handoff = Documento + Git Push** — ambas acciones suceden en el Paso 4
- **Git push solo con cambios reales** — handoff solo pushea si hay cambios
- **Automatización completa** — 5 pasos se ejecutan en secuencia automáticamente
- **Triple respaldo** — después de `/session-close`: documento (.agents/), GitHub, Google Drive
- **Sin esperas** — Google Drive for Desktop sincroniza automáticamente a la nube
- **Limpieza de contexto** — después de session-close, puedes usar `/compact` para limpiar sesión
