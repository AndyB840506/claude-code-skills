# Creador de Skills para Claude Code

Este proyecto crea skills personalizadas para Claude Code. Una skill es un archivo que le enseña a Claude a hacer una tarea específica de forma repetible.

## Verify Before Claiming

Los principios viven en `~/.claude/CLAUDE.md`: **§ Verification** (la faja — gobierna la SALIDA, no declarar hecho sin evidencia) y **§ Procedencia** (gobierna la ENTRADA, no usar un artefacto guardado como hecho). El **procedimiento** operativo — tabla de evidencia, recibos, las dos secciones de cierre — vive en la skill `verify`.

**No re-declarar esas reglas aquí.** Estaban escritas en 4 sitios el 2026-07-23 y el fallo siguió ocurriendo: el problema no es que falte la regla, es que falta el enforcement. Agregar una quinta copia diluye, no refuerza.

## Environment

Windows con PowerShell 5.1. Usar PowerShell (no Bash/xcopy) para operaciones de archivos. Evitar backtick-quotes, caracteres Unicode y expresiones if inline en scripts — PS 5.1 no los maneja correctamente.

**Excepción (escrituras byte-exactas):** para contenido que otras herramientas parsean (frontmatter de skills, JSON, restaurar archivos desde git), usar Bash con redirección (`git show X > file`) — `Set-Content -Encoding UTF8` en PS 5.1 escribe BOM y corrompe el archivo (mordió el 2026-07-06: el harness cargó una skill restaurada con el frontmatter ilegible). Y `-Encoding ASCII` destruye tildes/ñ/flechas (mordió el 2026-07-11: MODELS.md con `??`) — para editar archivos con contenido UTF-8, usar la herramienta Write o python, no Set-Content.

Config y reglas operativas en `~/.claude/`; proyectos y archivos de producción en `C:\Users\andre\repos\`. No proponer junctions para `~/.claude/`. Output de producción (imágenes, audios, transcripciones, cachés) va a `E:\` en el desktop y `D:\` en el portátil — nunca a `C:\`.

### Windows — shell

- El shell por defecto es PowerShell. **NO** usar heredocs de bash ni here-strings de PowerShell para contenido multilínea — escribir archivos con la herramienta Write. (No contradice la excepción de arriba: eso es redirección `>`, no heredoc.)
- Git Bash mangla rutas absolutas de Windows; usar PowerShell para cualquier cosa que pase rutas a ComfyUI u otros binarios de Windows.

## Comportamiento al iniciar

**Antes de responder nada**, sigue este orden:

1. **Sincroniza con GitHub:** ejecuta `git pull origin main` Y TAMBIÉN `git -C "$env:USERPROFILE\.claude\skills" pull origin main` — son 2 clones del mismo repo y el global se desactualiza solo (mordió 2026-07-08: 1 mes stale en el portátil, una skill "no existía")
   - **Repos externos:** antes del primer edit **o de lanzar cualquier agente (Explore/executor) sobre otro repo** (hiresignal, kuma-talent-web, etc.): `git -C <repo> fetch origin` y verificar si está detrás — pull ANTES de editar o explorar, no al pushear (mordió 2026-07-08: clon de hiresignal 40 commits stale → merge de 4 conflictos; mordió 2026-07-10: exploradores lanzados pre-pull mapearon el árbol viejo y reportaron que un feature existente "no existía").
   - **Trazabilidad del SHA (antes de lanzar subagentes):** correr `git pull --rebase --autostash` en CADA repo que los agentes vayan a leer (`--autostash` porque un working tree sucio aborta el rebase), e **imprimir el HEAD sha resultante de cada uno**. Pasarle ese sha a cada agente en su prompt y exigir que lo **cite en su reporte** — un sha que no coincide delata una lectura stale. **Un agente por workstream** — un *workstream* es un entregable independiente que no comparte archivos de salida con otro (ej.: metadata de Spotify vs rotación del grid). Si dos tareas escriben el mismo archivo, son UN solo workstream.
   - **En plan mode (no se puede hacer pull):** verificar staleness read-only con `git ls-remote origin` vs HEAD local, y poner el pull como primer paso de ejecución del plan (funcionó 2026-07-16 con hiresignal desactualizado).
2. **Busca un handoff reciente:** revisa `.agents/handoff/` — abre el archivo con la fecha más reciente.
3. **Decide cómo continuar:**
   - **Antes de resumirlo, verificarlo.** Producir una tabla `afirmación del handoff | estado real | discrepancia`, con evidencia real por fila: `Get-Date` para cualquier afirmación temporal (nunca inferir la fecha), `git log --oneline -10` + `git status` de cada repo tocado, y listado del directorio de assets del episodio. Lo que no se pueda comprobar se marca **NO VERIFICADA** en vez de omitirse. Nunca presentar lo que dice el handoff como estado actual — el 2026-07-23 un handoff de 27 minutos de antigüedad ya traía una ruta equivocada (`mrputridsden/` cuando el real era `.claude/skills/mrputridsden/`), y el `skill-kit-auditor` llevaba 45 días roto detrás de un handoff que se declaraba "verified across all 11 repos".
   - Si existe uno: resúmelo en 2-3 líneas (qué se hizo, dónde pausó, qué sigue) y pregunta si quiere continuar desde ahí. No asumas que sí.
   - Si no hay ninguno: sigue con el mensaje de bienvenida normal.

Cuando el usuario abra esta carpeta y escriba cualquier cosa (y no hay handoff), responde:

> **Bienvenido al creador de skills**
>
> Voy a ayudarte a crear una skill personalizada para Claude Code. Una skill es como un "modo experto" que le enseña a Claude a hacer algo específico.
>
> **¿Qué proceso quieres automatizar?**
>
> Puede ser cualquier cosa: generar informes, analizar datos, crear documentos, auditar webs, procesar archivos... Si lo haces de forma repetitiva, puede ser una skill.

Después usa la skill `crear-skill` automáticamente.

## Auto-compactación de contexto

**IMPORTANTE:** Cuando el contexto llegue al **50%**, compacta automáticamente:

```
/compact
```

Esto:
- ✓ Resume el contexto anterior
- ✓ Mantiene el historial importante
- ✓ Continúa la sesión sin desconexión
- ✓ Prepara espacio para nueva conversación

**Configuración:** manual — el auto-compact del harness está **desactivado** (`"autoCompactEnabled": false` en `~/.claude/settings.json`) y este proyecto no tiene `.claude/settings.json`. Compactar al 50% es responsabilidad del modelo, nadie lo dispara solo (verificado 2026-07-23).

## Qué genera

- Un archivo `.md` con las instrucciones completas de la skill
- Opcionalmente: un kit completo con CLAUDE.md e INSTRUCCIONES.md para compartir

## Los 10 principios de una buena skill

1. No inventa datos — pregunta lo que necesita
2. Obtiene datos automáticamente cuando puede
3. Auto-instala dependencias si las necesita
4. Libertad creativa en diseño (no CSS rígido)
5. Se adapta al contexto del usuario
6. Flujo conversacional (no interrogatorio)
7. Fallbacks amigables si algo falla
8. Mensaje de bienvenida claro
9. Sin precios sugeridos ni consejos de venta
10. Resumen claro de lo generado al terminar

## Debugging

Para cualquier ID, API key o valor de env var (ej. Google Drive/Sheet IDs), pedir al usuario que los pegue directamente desde la URL del browser o la fuente original — no retipear. Verificar el string exacto antes de depurar.

No declarar un bug como corregido hasta haberlo verificado (re-ejecutar/reproducir). Para JSON parse errors, revisar específicamente BOM y respuestas API vacías. Si una API LLM devuelve 400 "not valid JSON / zero-length document", sospechar de `json_encode` devolviendo `false` por UTF-8 inválido en el input (típico: texto extraído de PDF) — en PHP usar `JSON_INVALID_UTF8_SUBSTITUTE` y loguear `json_last_error_msg()` (mordió el 2026-07-07 en HireSignal).

Con `curl -L` no forzar `-X POST`: tras un redirect 302 curl reenvía el POST sin body (Google responde 411). Omitir `-X` y dejar que curl convierta a GET después del redirect (mordió 2 veces el 2026-07-06 probando el Apps Script de Kuma).

**Instrumentos que sub-reportan en silencio** — no dan error, solo devuelven de menos, así que producen "sin hallazgos" falsos (los dos mordieron el 2026-07-23):
- `Get-Content X | Measure-Object -Line` **no cuenta líneas en blanco** (dio 28 donde `wc -l` daba 36). Para contar líneas usar `wc -l`.
- `glob.glob('**/x', recursive=True)` de Python **omite directorios que empiezan con punto** — leyó 18 de 28 `SKILL.md` porque se saltó todo `.claude/`. Usar `os.walk`.
Antes de reportar un conteo o un "cero hallazgos", cruzar el total con una segunda herramienta. Ver §Procedencia en `~/.claude/CLAUDE.md`.

## Límites de lo publicable (medir, no estimar)

- Descripción del show en Spotify: límite duro de **600 caracteres** — contarlos antes de enviar.
- Cualquier copy publicado con límite de plataforma: **imprimir el conteo de caracteres** en la respuesta.
- Imágenes embebidas en HTML: toda `<img>` con regla de `width` debe llevar `height: auto` en la MISMA regla. **Verificación:** revisar cada `<img>` una por una — NO un grep del archivo: `width:\s*\d` también matchea divs, y un solo `height: auto` en cualquier parte enmascara al resto (comprobado 2026-07-23).
- Negro de marca: **no lo redeclares aquí** — la fuente es `.claude/skills/episode-launch/docs/brand-constants.md`. Lo único que se afirma acá: un asset generado que renderiza negro puro `#000000` está mal y se corrige antes de componer.

## Artwork (reglas de generación — persisten entre sesiones)

**Fuente canónica de las reglas de artwork BTQ:** `.claude/skills/episode-launch/docs/brand-constants.md` § "Dirección de artwork" (**CONGELADA v3**, 2026-07-04). Esta sección NO la reemplaza — agrega lo que no está allí. Si chocan, gana el archivo congelado.

- **Motivos vetados:**
  - **Círculos concéntricos / anillos / diana: VETADOS en TODAS las imágenes** — portadas **Y** quote cards. Decisión de Andy del **2026-07-10 (EP.021)**; antes el motivo estaba "reservado para la portada" y por eso reaparecía. Única excepción: cuando la diana **ES el sujeto central** de la escena (ej. Q2 de EP.020). La línea `DO NOT render any concentric ring, circle, halo, or archery-target pattern anywhere in this image.` va en **todo** prompt desde el primer intento: el modelo los reinserta solo (Flow en EP.020; Z-Image local en EP.022) y **pueden colarse disfrazados de textura** — en EP.022 una tela salió cubierta de mini-círculos, invisible a tamaño completo y detectada solo al hacer zoom a una esquina.
  - *cualquier asset:* proporciones chibi; personas en cards marcadas "sin personas".
  - ⚠️ **`btq-production/artwork-general-v3.md` contradice esto** — pide "concentric circles… like the grooves of a vinyl record" para la og-image. Ese archivo quedó **desactualizado** (el veto es posterior, del 07-10) y **no se usa tal cual** hasta corregirlo.
- Confirmar el aspect ratio destino por tipo de asset (portada vs quote card vs tile de grid) ANTES de generar.
- Renderizar e inspeccionar visualmente **todas** las variantes de aspect ratio antes de declarar un set completo.

## Long-running jobs (descargas y renders > 2 min)

Antes de arrancar cualquier descarga o render que se espere que pase de 2 minutos:

- **Estimar y decirlo primero:** duración estimada y, si es descarga, bytes totales. Para un render los bytes no dicen nada — la estimación es `steps x it/s` **nombrando la máquina** (3080 Ti 12GB en el desktop vs 3060 6GB en el portátil dan números distintos).
- **Baseline más simple primero:** proponer el workflow mínimo que podría funcionar, **correrlo y mostrar su output** antes de agregar nodos o etapas. Instancia de las reglas #14/#15 globales.
- **Progreso:** lanzar en background escribiendo a un log; reportar en cada frontera de etapa y al terminar, con tiempo transcurrido. El log se puede leer a demanda. **No prometer una cadencia fija de 60s** — el harness no da un timer propio durante una tarea: un comando en foreground bloquea hasta que retorna y uno en background solo avisa al completarse.

## Principios de tooling — lean y reactivo

- No agregar hooks de `SessionStart` ni ningún costo fijo de arranque. Los hooks deben ser dirigidos por evento (`PreToolUse`/`PostToolUse`) y dispararse solo cuando ocurre el evento relevante.
- **`PostToolUse` corre DESPUÉS de la herramienta — no puede bloquear nada.** Para impedir que algo se ejecute hay que usar `PreToolUse` con `hookSpecificOutput.permissionDecision: "deny"` (verificado 2026-07-23 contra el schema de settings).

## Workflows

Ritual de cierre de sesión: `/session-close` lo automatiza completo (retrospective → skill-management → handoff). Equivale a ejecutar `/retrospective`, luego `skill-management`, luego `/handoff` en ese orden. Aplicar los fixes aprobados del audit antes de generar el handoff.

## Regla de transición de modelo (vigente desde 2026-06-12)

Este proyecto fue calibrado con Fable 5, que infiere mucho desde contexto. Cualquier modelo que ejecute aquí (en especial Opus 4.8 después del 2026-06-22) debe compensar siguiendo lo escrito de forma literal:

1. **Seguir los checklists al pie de la letra.** El estándar de calidad por entregable vive en `docs/estandar-de-entregables.md` — correr el checklist de la sección que aplique ANTES de declarar algo listo. Si un ítem falla, corregir y re-verificar.
2. **Correr los lints de las skills antes de entregar** (greps de muletillas, conteos, fórmulas de título). Los criterios son verificables a propósito: verificarlos, no estimarlos.
3. **Consultar MEMORY.md y el handoff más reciente antes de actuar.** Las decisiones de juicio ya tomadas están escritas ahí y en `docs/roadmap-future-proofing.md`; no re-derivarlas ni contradecirlas sin preguntar.
4. **Si una tarea requiere juicio que no está escrito, preguntar al usuario** en vez de improvisar — y al resolverla, escribir la regla nueva donde corresponde.
