# Workflow: Ejecutar auditoría completa

Procedimiento detallado para la ejecución de `/skill-kit-auditor`.
Complementa el flujo de SKILL.md con comandos concretos y plantillas.

---

## Paso 1 — Comandos de lectura por tipo de archivo

### Listar todas las skills

```
Glob: .claude/skills/**/*.md
Glob: .claude/skills/**/*.md (archivos sueltos como handoff.md)
```

### Leer cada skill

Para skills en carpeta:

```
Read: .claude/skills/[nombre]/SKILL.md
Read: .claude/skills/[nombre]/workflows/*.md (si existen)
Read: .claude/skills/[nombre]/config/*.md (si existen)
```

Para skills sueltas (archivo .md sin carpeta):

```
Read: .claude/skills/[nombre].md
```

### Leer documentación del proyecto raíz

```
Read: CLAUDE.md
Read: INSTRUCCIONES.md
Read: README.md (si existe)
```

### Leer sub-proyectos generados

```
Glob: kit-*/ → Read cada CLAUDE.md e INSTRUCCIONES.md
Glob: kuma-*/ → Read cada CLAUDE.md e INSTRUCCIONES.md
Glob: ENTREGA_*/ → listar archivos para detectar ZIPs desactualizados
```

---

## Paso 2 — Plantilla de tabla de reporte

Usar esta plantilla para presentar el reporte al usuario:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  REPORTE DE AUDITORÍA — kit-skill-creator                               │
│  Skills analizadas: N  |  Issues encontrados: M                         │
│  🔴 CRITICAL: X  |  🟠 HIGH: X  |  🟡 MEDIUM: X  |  🟢 NOTE: X        │
└─────────────────────────────────────────────────────────────────────────┘

ID   SEV        SKILL                 PROBLEMA
─────────────────────────────────────────────────────────────────────────
A-01 🔴 CRITICAL smart-recruiter      Sin frontmatter name: en archivo principal
A-02 🔴 CRITICAL kit-smart-recruiter  CLAUDE.md inglés / INSTRUCCIONES.md español
B-01 🟠 HIGH     ai-lead-generator    6 preguntas seguidas en Paso 1 (viola P#6)
B-02 🟠 HIGH     ai-lead-generator    CSS hardcodeado viola principio #4
B-03 🟠 HIGH     10-skill-creator     Principios en 3 archivos distintos
C-01 🟡 MEDIUM   smart-recruiter      Exchange count declarado (10-14) ≠ real (11-18)
C-02 🟡 MEDIUM   leracom-mcp-builder  HIRESIGNAL_MODE sin valores válidos documentados
D-01 🟢 NOTE     10-skill-creator     Sección PHP en skill genérica
```

---

## Paso 3 — Árbol de decisión por issue

Para cada issue, determina la acción correctiva:

```
¿El problema está en la estructura/frontmatter?
  → Editar SKILL.md: corregir name:, description:, formato
  
¿El problema es contenido duplicado entre archivos?
  → Eliminar de los archivos secundarios, dejar en SKILL.md como fuente de verdad
  
¿El problema es un principio violado?
  → Editar la sección problemática en SKILL.md
  → Si es diseño (P#4): eliminar CSS/colores y reemplazar con guías de contenido
  → Si es flujo (P#6): agrupar preguntas en bloques de máximo 3
  → Si es datos primero (P#2): añadir paso de lectura automática antes del primer bloque de preguntas
  
¿El problema es un flujo circular?
  → Identificar el paso que regresa sin avanzar
  → Agregar output concreto a ese paso o eliminar el regreso
  
¿El problema es de dos skills solapadas?
  → Evaluar merge vs. especialización:
    - Si hacen >70% de lo mismo: merge (mantener la más completa)
    - Si tienen dominios distintos: diferenciar triggers, no hacer merge
    
¿El problema es un archivo desactualizado (ZIP, export)?
  → Opción A: regenerar el archivo
  → Opción B: agregar aviso en README de que es un snapshot
  → Opción C: eliminar si no se usa
```

---

## Paso 4 — Presentación de diffs

Para cada cambio propuesto, mostrar exactamente:

```
─── CAMBIO PROPUESTO ─────────────────────────────────────────────────────
Archivo: .claude/skills/smart-recruiter.md
Issue:   A-01 🔴 CRITICAL — Sin frontmatter name:

ANTES (primeras 3 líneas del archivo):
# Smart Recruiter
AI-powered candidate screening...

DESPUÉS:
---
name: smart-recruiter
description: >
  Entrevistador de IA para reclutadores. Conduce entrevistas estructuradas...
---

# Smart Recruiter
AI-powered candidate screening...
──────────────────────────────────────────────────────────────────────────
¿Aplico este cambio? [Sí / No / Ver siguiente]
```

---

## Paso 5 — Checklist de verificación post-cambio

Después de aplicar todos los cambios aprobados, verificar:

- [ ] Todos los `name:` en frontmatter coinciden con el nombre del folder/archivo
- [ ] No hay dos skills con el mismo trigger exacto
- [ ] Las skills modificadas siguen siendo legibles (no se corrompió el YAML del frontmatter)
- [ ] Los archivos de documentación modificados no perdieron contenido valioso
- [ ] El conteo de skills en `.claude/skills/` es el mismo que antes de la auditoría (no se eliminó nada accidentalmente)

Si algún check falla: mostrar el error específico y proponer corrección antes de cerrar.

---

## Paso 0 — Presentación de lista de skills (Modo B)

Cuando el usuario elige auditar una skill específica, leer `.claude/skills/` dinámicamente
y presentar la lista con este formato:

```text
Skills disponibles en el kit:

 1. 10-skill-creator
 2. ai-lead-generator
 3. bf6-meta-configurator
 4. handoff
 5. hiresignal-scoring
 6. leracom-mcp-builder
 7. on-call-handoff-patterns
 8. prompt-reviewer
 9. retrospective
10. session-close
11. skill-kit-auditor
12. skill-management

¿Cuál quieres auditar? (número o nombre)
```

La lista se genera leyendo las carpetas y archivos `.md` sueltos en `.claude/skills/`
en el momento de invocar — no hardcodeada. Ordenar alfabéticamente.
El usuario puede responder con el número o escribir el nombre directamente.

---

## Notas de implementación

**Sobre el frontmatter YAML:**
El delimitador `---` debe estar en la primera línea del archivo, sin espacios antes. Si hay contenido antes del `---`, Claude Code no lo reconocerá como frontmatter.

**Sobre los triggers:**
Claude Code hace matching parcial (substring), no exacto. "revisar skill" activará tanto "revisar skill" como "revisar skills". Tener esto en cuenta al evaluar solapamientos.

**Sobre archivos sueltos vs carpetas:**
Una skill puede ser un archivo `.md` suelto (como `handoff.md`) o una carpeta con `SKILL.md`. Ambos formatos son válidos. La carpeta se usa cuando la skill necesita archivos auxiliares (config, workflows).
