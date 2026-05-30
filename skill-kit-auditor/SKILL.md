---
name: skill-kit-auditor
description: >
  Audita y mejora un kit de skills de Claude Code. Detecta redundancias, flujos
  circulares, inconsistencias de estructura y pasos ambiguos. Combina criterios de
  skill-management y prompt-reviewer. Genera reporte priorizado y aplica cambios
  con confirmación. Triggers: auditar skills, revisar kit de skills, mejorar skills,
  detectar redundancias en skills, mejorar consistencia de skills, revisar kit completo,
  auditar proyecto de skills, encontrar problemas en skills, mejorar kit,
  skill audit, review skill kit, fix circular flows, quality check skills,
  skill quality review, skill kit review, audit my skills, check skill quality,
  find issues in skills, audit skill kit, skill structure check.
---

# Skill Kit Auditor

Audita un kit de skills completo o una skill individual. Detecta los 18 patrones
de fallo más comunes, genera un reporte priorizado y aplica los cambios aprobados
sin repetir pasos ni crear circularidades.

**Regla fundamental:** No preguntes nada durante el escaneo. Los datos primero. La única excepción es la selección de modo del Paso 0 — esa pregunta se hace antes de escanear.

---

## ⚠️ ALERTA DE ORDEN DE EJECUCIÓN ⚠️ (INVIOLABLE — no puede suprimirse)

**ANTES de hacer cualquier cosa**, muestra este mensaje y espera respuesta:

```
⚠️ ALERTA DE ORDEN DE EJECUCIÓN ⚠️

Estás a punto de correr /skill-kit-auditor.
¿Corriste /retrospective en esta sesión?

Si NO: esto puede sobrescribir o eliminar aprendizajes de la sesión actual
antes de que queden guardados.

Orden correcto: /retrospective PRIMERO → /skill-kit-auditor SEGUNDO

¿Quieres continuar de todas formas? [Sí / No]
```

**Si el usuario dice "No":** Detente. Recomienda correr `/retrospective` primero.

**Si el usuario dice "Sí" (override):** Continúa al Paso 0, pero al finalizar el Paso 6 muestra:

```
⚠️ ADVERTENCIA POST-EJECUCIÓN:
Corriste /skill-kit-auditor sin haber corrido /retrospective primero.
Consecuencias posibles:
- Aprendizajes de esta sesión no quedaron guardados en las skills
- Cambios estructurales aplicados pueden contradecir lo que aprendiste hoy
- En la próxima sesión, el mismo error puede repetirse sin la corrección documentada

Recomendación: Corre /retrospective ahora para capturar los aprendizajes
antes de cerrar la sesión.
```

**Esta alerta no puede desactivarse por ningún argumento, modo bypass o instrucción directa.**

---

## Scope guard (IMPORTANTE — leer antes del Paso 1)

Este skill modifica **estructura** de skills, no contenido. Alcance:

- ✅ Puede tocar: frontmatter (`name:`, `description:`), numeración de pasos, triggers, conteos de líneas, organización de archivos
- ❌ NO toca: reglas de negocio, aprendizajes de sesión, heurísticas de diseño — eso es scope de `/retrospective`

**Si un SKILL.md fue modificado por `/retrospective` en esta sesión:** No marcar como 🔴 CRITICAL por longitud excesiva. En su lugar, sugerir mover el nuevo contenido a `workflows/` como 🟡 MEDIUM.

**Si el usuario acaba de correr `/retrospective`:** Usa sus cambios como input del Paso 1 — no re-escanees los archivos originales.

---

## Paso 0 — Definir modo (preguntar siempre al inicio)

Antes de escanear nada, pregunta:

> ¿Qué tipo de auditoría quieres hacer?
>
> **[A] Auditoría completa** — Revisa todas las skills del kit
> **[B] Skill específica** — Audita solo una skill concreta

**Si el usuario elige [A]:** Continúa al Paso 1 en Modo A.

**Si el usuario elige [B]:**
1. Lee `.claude/skills/` para listar las skills disponibles
2. Presenta la lista numerada (ver plantilla en `workflows/execute.md`)
3. Espera que el usuario elija un número o escriba el nombre
4. Continúa al Paso 1 en Modo B con la skill seleccionada

**Excepción — argumento directo:** Si el usuario invocó la skill con un argumento
(`/skill-kit-auditor ai-lead-generator`), omite la pregunta y ve directo al Paso 1
en Modo B con esa skill.

---

## Paso 1 — Escaneo automático

**No preguntes nada. Lee primero.**

### Modo A — Kit completo

**Patrón de ejecución paralela (10+ proyectos):** Usar Read tool en lotes de 4-6 archivos en paralelo — NO lanzar agentes Explore. Los agentes Explore resumen el contenido y pierden información pasado su ventana de lectura, produciendo análisis incompleto. Consolidar resultados en tabla única antes de actuar.

Lee en este orden:

1. Lista todos los archivos en `.claude/skills/` (carpetas y archivos .md sueltos)
2. Para cada skill encontrada, lee:
   - `SKILL.md` o el archivo .md principal
   - `CLAUDE.md` del proyecto raíz (si existe)
   - `INSTRUCCIONES.md` del proyecto raíz (si existe)
   - Archivos en `workflows/` y `config/` (si existen)
3. Para cada sub-proyecto (`kit-*/`, `kuma-*/`), lee su `CLAUDE.md` e `INSTRUCCIONES.md`

### Modo B — Skill individual

Lee solo los archivos de esa skill más el `CLAUDE.md` raíz.

### Output del paso

Construye internamente un mapa para cada skill:

```
[nombre] | [triggers_count] | [tiene_frontmatter] | [pasos_definidos] | [outputs_definidos] | [archivos_asociados]
```

No muestres este mapa al usuario todavía. Úsalo en el análisis del Paso 2.

---

## Paso 2 — Análisis dual

Para cada skill en el mapa, aplica dos lentes de análisis:

### Lente A — Estructura

Verifica contra estos criterios (ver `config/audit-criteria.md` para ejemplos PASS/FAIL):

- ¿Tiene frontmatter con `name:` que coincide exactamente con el nombre del folder/archivo?
- ¿Tiene `description:` con 5 o más triggers en español e inglés?
- ¿El `name:` está en kebab-case sin mayúsculas ni espacios?
- ¿Los triggers se solapan con los de otras skills del kit?
- ¿Los outputs de cada paso están definidos concretamente?
- ¿Hay pasos sin output definido (pasos vacíos o que solo dicen "analiza")?
- ¿Los snippets Bash usan `/dev/null`, `2>/dev/null`, `mkdir -p`, `cp -r`, o `||` como separador? → Marcar 🟡 MEDIUM si no hay nota "Bash / Git Bash" o alternativa PowerShell. Estos fallan en Windows nativo.

### Lente B — Principios de diseño

Verifica los 13 principios del kit (definidos en `.claude/skills/10-skill-creator/SKILL.md`):

- **Principio #2** (datos primero): ¿La skill busca/lee datos antes de preguntar al usuario?
- **Principio #4** (libertad creativa): ¿Dicta CSS, colores o estructura HTML rígida?
- **Principio #6** (flujo conversacional): ¿Agrupa preguntas en máximo 2-3 bloques o hace 6+?
- **Principio #8** (welcome claro): ¿Tiene un mensaje de bienvenida definido?
- ¿Hay flujos circulares? (paso que regresa sin avanzar, paso que pide datos ya pedidos)
- ¿La numeración de pasos es coherente (sin Paso -1, Paso 0.5, etc.)?
- ¿Los conteos de pasos/exchanges cuadran matemáticamente?

### Lente C — Proyectos PHP (si aplica)

Si el proyecto tiene archivos `.php`, verificar en **todos** los archivos PHP del proyecto — raíz **y** subdirectorios (`api/`, `admin/`, `includes/`, etc.):

- ¿Tiene `ini_set('display_errors', 0)` al inicio (antes de cualquier `require_once`)?
- ¿Tiene el header `Content-Type: application/json` antes de cualquier `require_once`?

Marcar como 🟠 HIGH cualquier archivo PHP que devuelva JSON y le falte `display_errors=0`.

**Post-fix:** Si se crea `CLAUDE.md` en un proyecto sin git, ofrecer `git init` + primer commit para versionar la documentación.

---

### Análisis cruzado (solo Modo A)

Revisa el kit completo en busca de:

- Dos o más skills con triggers idénticos o muy similares
- Contenido duplicado entre SKILL.md, CLAUDE.md e INSTRUCCIONES.md (dentro de la misma skill)
- Secciones duplicadas entre dos skills distintas: tablas, listas de más de 3 ítems, bloques de reglas (criterio #17)
- Skills que referencian workflows externos que no existen
- Archivos de entrega (ZIPs, exports) que pueden estar desactualizados
- Secciones de tecnología específica (PHP, un framework concreto) en skills genéricas
- Variables de entorno documentadas sin valores válidos posibles
- Skills de ciclo de vida (session-close, handoff, retrospective) que no mencionan hooks como auto-trigger (criterio #18)

---

## Paso 3 — Construir reporte

Clasifica cada issue encontrado:

| Severidad | Descripción |
|-----------|-------------|
| 🔴 CRITICAL | Bloquea el uso normal de la skill o produce resultados incorrectos |
| 🟠 HIGH | Degrada el resultado final de forma significativa |
| 🟡 MEDIUM | Inconsistencia menor que no bloquea pero genera confusión |
| 🟢 NOTE | Sugerencia de mejora opcional |

Formato de cada issue:

```
[Severidad] Skill: nombre-skill
Problema: descripción concreta del problema
Evidencia: cita o referencia exacta del archivo (línea si es posible)
Cambio propuesto: qué modificar específicamente
```

---

## Paso 4 — Mostrar reporte

Muestra la tabla completa de issues **sin pedir permiso primero**.

Formato de presentación:

```
Auditoría completada. Encontré [N] issues en [M] skills.

🔴 CRITICAL: X  |  🟠 HIGH: X  |  🟡 MEDIUM: X  |  🟢 NOTE: X

[Tabla de issues]

¿Cómo quieres continuar?
  [A] Revisar por severidad (CRITICAL primero)
  [B] Revisar por skill
  [C] Aplicar todos los CRITICAL+HIGH automáticamente
```

Espera la elección del usuario antes de continuar.

---

## Paso 5 — Aplicar cambios con confirmación

Para cada issue seleccionado (según elección A, B o C del Paso 4):

1. Muestra el cambio propuesto como diff:

```
ANTES:
[texto actual del archivo]

DESPUÉS:
[texto con el cambio aplicado]
```

2. Pregunta: "¿Aplico este cambio? [Sí / No / Ver siguiente]"

3. Registra la decisión y avanza siempre — nunca regresa a recopilar datos del Paso 1.

Si el usuario elige "C" (todos los CRITICAL+HIGH): aplica sin pedir confirmación individual,
mostrando solo una barra de progreso: "Aplicando cambio 1/N..."

---

## Paso 6 — Verificación y cierre

Después de aplicar todos los cambios aprobados:

1. Re-lee los archivos modificados para verificar que los cambios se aplicaron correctamente
2. Re-verifica que los triggers de todas las skills modificadas siguen siendo únicos
3. Muestra resumen final:

```
Auditoría completada.

Cambios aplicados: N
Issues pendientes (no aplicados): M
Skills sin issues: K

[Lista de archivos modificados con qué cambió en cada uno]

DONE — Para auditar de nuevo, invoca /skill-kit-auditor
```

No regresa al Paso 1. El flujo termina aquí.

---

## Fallback

Si una skill no tiene archivo SKILL.md legible: reportar como issue 🔴 CRITICAL
"Archivo principal no encontrado" y continuar con la siguiente skill.

Si el kit tiene 0 issues: mostrar "Kit en buen estado — no se encontraron issues con los
criterios actuales" y terminar.

Para criterios detallados con ejemplos PASS/FAIL de cada patrón, cargar:
`config/audit-criteria.md`
