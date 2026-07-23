# Memory Audit — Execution

## EXECUTION

Ejecuta el proceso en 6 pasos (Paso 0 cubre el skill kit, 1–3 cubren memoria). Todos
menos el 4 corren sin pedir aprobación (son solo lectura). El paso 4 sí requiere
aprobación explícita antes de tocar cualquier archivo.

### Paso 0 — Integridad del skill kit

1. `Glob "**/SKILL.md"` desde `c:\Users\andre\.claude\skills` — dinámico, cualquier
   skill nuevo entra solo, no hay lista fija que mantener.
2. Para cada `SKILL.md`: lee el frontmatter. `name` o `description` vacío/faltante →
   hallazgo **frontmatter roto**.
3. Para cada referencia a `workflows/X.md` o `docs/Y.md` dentro del `SKILL.md`,
   confirma que el archivo existe (`Glob`/`Read`). No existe → hallazgo
   **referencia rota**.
4. Grep literal por `Ã` o `Â` (usar el tool Grep, NO `Get-Content` de PowerShell —
   verificado 2026-07-06: PowerShell puede mostrar mojibake que no existe en el
   archivo real por su propio manejo de encoding en consola/regex complejos; un
   patrón de rango Unicode `[\x{00C0}-\x{00FF}]` probó ser un falso negativo). Si
   hay match, confirma con `Read` (no con otro dump de PowerShell) que el byte
   realmente está mal antes de reportarlo como **texto corrupto** — de lo
   contrario es ruido de la herramienta, no del archivo.
5. **Prioridad de verificación real:** para skills que tocan producción en vivo
   (mínimo `freelance-gig` → repo `the-freelancer` / andyfreelancer.com — ver
   [[reference_the_freelancer_reuse]]), confirma que lo que el skill afirma sobre
   el repo (rutas, líneas, nombres de archivo) sigue siendo cierto (`git log`,
   `Read`) — mismo estándar que Paso 3, no lo trates distinto solo porque es un
   skill y no una memoria.

### Paso 1 — Inventario

1. Lee `MEMORY.md` completo (workspace: `C:\Users\andre\.claude\projects\<workspace>\memory\`).
2. Lista todos los `.md` en esa carpeta (Glob `*.md`, excluyendo `MEMORY.md`).
3. Para cada archivo, lee su frontmatter (`name`, `description`, `metadata.type`).
4. **Huérfanos:** compara la lista de archivos contra las líneas de `MEMORY.md`.
   - Archivo sin línea en `MEMORY.md` → huérfano tipo A.
   - Línea en `MEMORY.md` cuyo archivo referenciado no existe → huérfano tipo B.

### Paso 1b — Sobredimensionadas

Para cada archivo, cuenta sus líneas totales con **`wc -l`** (o `sum(1 for _ in fh)` en
Python). **NO uses `Measure-Object -Line`: no cuenta líneas en blanco y sub-reporta en
silencio** — ver `skills/CLAUDE.md` § Debugging, "Instrumentos que sub-reportan"
(2026-07-23: dio 28 donde `wc -l` daba 36). Cualquier archivo por encima de ~60 líneas es
un hallazgo tipo **sobredimensionada** — ver [[feedback_memory_file_discipline]]. No
requiere verificación adicional, solo el conteo.

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

**Tabla interna** (para saber qué resolución aplica a cada tipo — esto es
vocabulario de trabajo, NO lo que se le muestra a Andy):

| Tipo | Resolución propuesta |
|---|---|
| Frontmatter roto (skill) | Restaurar `name`/`description` a partir del contenido del archivo |
| Referencia rota (skill) | Corregir la ruta, o eliminar la referencia si el archivo ya no debe existir |
| Texto corrupto (skill o memoria) | Corregir la codificación/el corte de palabra |
| Duplicado | Fusionar en una sola entrada más completa; archivar la otra |
| Contradicción | Quedarse con la versión verificada como vigente; anotar qué se descartó y por qué |
| Obsoleta | Corregir el contenido con el estado real verificado, o eliminar si ya no aplica |
| Huérfano tipo A | Agregar la línea faltante en `MEMORY.md` |
| Huérfano tipo B | Eliminar la línea de `MEMORY.md` (el archivo no existe) |
| Sobredimensionada | Recortar a lo esencial, o dividir en memorias enlazadas |

**Tabla que ve Andy** (ver [[feedback_short_approval_asks]] — plana, visual, cero
párrafos): traduce cada fila de arriba a lenguaje de consecuencia, sin nombrar el
tipo técnico. Formato fijo: `Icono | Qué encontré (una frase) | Qué voy a hacer (una frase)`.
⚠ = algo se borra/elimina. ✅ = algo se arregla/restaura. Sin ícono = todo lo demás.

Ejemplo real (NO "Huérfano tipo B"): `⚠ | Una línea del índice apunta a un archivo
que ya no existe | La voy a borrar del índice`.
Ejemplo real (NO "Frontmatter roto"): `✅ | Este archivo de memoria quedó sin nombre
ni descripción, invisible para futuras búsquedas | Le devuelvo el nombre y la
descripción`.

Pregunta explícitamente: "¿Aplico estos cambios? (todos / seleccionar cuáles / ninguno)".
**No toques ningún archivo antes de esta aprobación.** Preferir fusionar sobre borrar
cuando dos memorias no se contradicen; verificar contra el estado real antes de marcar
algo obsoleto (no basta con que "suene" desactualizado).

### Paso 5 — Aplicar + actualizar línea base

1. Aplica solo lo aprobado (Edit/Write en los archivos de memoria + `MEMORY.md` +
   los `SKILL.md`/`workflows`/`docs` que hayan salido en el Paso 0).
2. Cuenta los `.md` actuales en la carpeta de memoria (excluyendo `MEMORY.md`) y los
   `SKILL.md` actuales en el skill kit (`Glob "**/SKILL.md"`).
3. Actualiza `memory/.audit-baseline.json` con
   `{"lastAuditFileCount": <conteo actual>, "lastSkillCount": <conteo actual>, "lastAuditDate": "<fecha de hoy>"}`.
4. Si el repo local de memoria (ver [[feedback_memory_file_discipline]]) tiene cambios,
   `git add -A && git commit -m "memory-audit: <fecha>"` dentro de la carpeta de memoria.
5. Cierra con una tabla resumen:

| Hallazgo | Acción |
|---|---|
| [frontmatter roto / referencia rota en skill] | Corregido |
| [duplicado X + Y] | Fusionado |
| [contradicción Z] | Resuelto a favor de [cuál], por qué |
| [obsoleta W] | Corregida / eliminada |
| Línea base | Actualizada a N archivos de memoria + M SKILL.md |

---

**¡Memory audit completado!**
