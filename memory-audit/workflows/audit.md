# Memory Audit — Execution

## EXECUTION

Ejecuta el proceso en 5 pasos. Los pasos 1–3 corren sin pedir aprobación (son solo
lectura). El paso 4 sí requiere aprobación explícita antes de tocar cualquier archivo.

### Paso 1 — Inventario

1. Lee `MEMORY.md` completo (workspace: `C:\Users\andre\.claude\projects\<workspace>\memory\`).
2. Lista todos los `.md` en esa carpeta (Glob `*.md`, excluyendo `MEMORY.md`).
3. Para cada archivo, lee su frontmatter (`name`, `description`, `metadata.type`).
4. **Huérfanos:** compara la lista de archivos contra las líneas de `MEMORY.md`.
   - Archivo sin línea en `MEMORY.md` → huérfano tipo A.
   - Línea en `MEMORY.md` cuyo archivo referenciado no existe → huérfano tipo B.

### Paso 2 — Detectar duplicados y contradicciones

1. Agrupa los archivos por tema (mismo prefijo `project_`/`feedback_`/`reference_`/
   `user_` + subject similar en el `name`, o contenido que menciona el mismo repo/
   proyecto/skill).
2. Dentro de cada grupo de 2+ archivos sobre el mismo tema, lee el contenido completo
   y clasifica:
   - **Duplicado:** ambos afirman lo mismo, sin contradicción — candidato a fusión.
   - **Contradicción:** uno afirma X, el otro afirma lo contrario (o un estado que ya
     no puede ser cierto si el otro lo es) — necesita resolución, no solo fusión.
3. No inventes un grupo de contradicción sin releer ambos archivos completos — un
   parecido superficial en el `name` no basta.

### Paso 3 — Verificar una muestra contra el estado real

1. De todos los archivos, filtra los que hacen una **afirmación verificable de estado**
   (contienen palabras como "WIP", "live", "pendiente", "en vivo", "actualmente",
   "estado:", una fecha límite, un número de versión, un conteo) — las memorias de
   tipo `feedback` sobre preferencias durables normalmente NO aplican aquí.
2. Prioriza para verificar: (a) las involucradas en duplicados/contradicciones del
   Paso 2, (b) las más antiguas por fecha de `originSessionId`/mtime, (c) hasta un
   máximo razonable si hay muchas (no verifiques exhaustivamente decenas de memorias
   de preferencia que no decaen).
3. Para cada una, comprueba contra el estado real: `Read`/`Glob` el archivo o ruta que
   menciona, `git log`/`git show` el repo si aplica, `curl`/`WebFetch` si menciona una
   URL en vivo. Si la afirmación ya no es cierta, es un hallazgo de tipo **obsoleta**.
4. Aplica la regla de "teoría de la faja" (`~/.claude/CLAUDE.md` § Verification): no
   marques algo como vigente solo porque "suena consistente" — verifica de verdad.

### Paso 4 — Proponer y pedir aprobación

Presenta los hallazgos agrupados por tipo (duplicados / contradicciones / obsoletas /
huérfanos). Para cada uno: la evidencia concreta (qué archivos, qué dice cada uno, qué
verificaste) y UNA resolución propuesta:

| Tipo | Resolución propuesta |
|---|---|
| Duplicado | Fusionar en una sola entrada más completa; archivar la otra |
| Contradicción | Quedarse con la versión verificada como vigente; anotar qué se descartó y por qué |
| Obsoleta | Corregir el contenido con el estado real verificado, o eliminar si ya no aplica |
| Huérfano tipo A | Agregar la línea faltante en `MEMORY.md` |
| Huérfano tipo B | Eliminar la línea de `MEMORY.md` (el archivo no existe) |

Pregunta explícitamente: "¿Aplico estos cambios? (todos / seleccionar cuáles / ninguno)".
**No toques ningún archivo antes de esta aprobación** — ver Rules en `SKILL.md`.

### Paso 5 — Aplicar + actualizar línea base

1. Aplica solo lo aprobado (Edit/Write en los archivos de memoria + `MEMORY.md`).
2. Cuenta los `.md` actuales en la carpeta de memoria (excluyendo `MEMORY.md`).
3. Actualiza `memory/.audit-baseline.json` con
   `{"lastAuditFileCount": <conteo actual>, "lastAuditDate": "<fecha de hoy>"}`.
4. Cierra con una tabla resumen:

| Hallazgo | Acción |
|---|---|
| [duplicado X + Y] | Fusionado |
| [contradicción Z] | Resuelto a favor de [cuál], por qué |
| [obsoleta W] | Corregida / eliminada |
| Línea base | Actualizada a N archivos |

---

**¡Memory audit completado!**
