# Creador de Skills para Claude Code

Este proyecto crea skills personalizadas para Claude Code. Una skill es un archivo que le enseña a Claude a hacer una tarea específica de forma repetible.

## Environment

Windows con PowerShell 5.1. Usar PowerShell (no Bash/xcopy) para operaciones de archivos. Evitar backtick-quotes, caracteres Unicode y expresiones if inline en scripts — PS 5.1 no los maneja correctamente.

**Excepción (escrituras byte-exactas):** para contenido que otras herramientas parsean (frontmatter de skills, JSON, restaurar archivos desde git), usar Bash con redirección (`git show X > file`) — `Set-Content -Encoding UTF8` en PS 5.1 escribe BOM y corrompe el archivo (mordió el 2026-07-06: el harness cargó una skill restaurada con el frontmatter ilegible). Y `-Encoding ASCII` destruye tildes/ñ/flechas (mordió el 2026-07-11: MODELS.md con `??`) — para editar archivos con contenido UTF-8, usar la herramienta Write o python, no Set-Content.

Config y reglas operativas en `~/.claude/`; proyectos y archivos de producción en `C:\Users\andre\repos\`. No proponer junctions para `~/.claude/`. Output de producción (imágenes, audios, transcripciones, cachés) va a `E:\` en el desktop y `D:\` en el portátil — nunca a `C:\`.

## Comportamiento al iniciar

**Antes de responder nada**, sigue este orden:

1. **Sincroniza con GitHub:** ejecuta `git pull origin main` Y TAMBIÉN `git -C "$env:USERPROFILE\.claude\skills" pull origin main` — son 2 clones del mismo repo y el global se desactualiza solo (mordió 2026-07-08: 1 mes stale en el portátil, una skill "no existía")
   - **Repos externos:** antes del primer edit **o de lanzar cualquier agente (Explore/executor) sobre otro repo** (hiresignal, kuma-talent-web, etc.): `git -C <repo> fetch origin` y verificar si está detrás — pull ANTES de editar o explorar, no al pushear (mordió 2026-07-08: clon de hiresignal 40 commits stale → merge de 4 conflictos; mordió 2026-07-10: exploradores lanzados pre-pull mapearon el árbol viejo y reportaron que un feature existente "no existía").
2. **Busca un handoff reciente:** revisa `.agents/handoff/` — abre el archivo con la fecha más reciente.
3. **Decide cómo continuar:**
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

**Configuración:** Habilitada en `.claude/settings.json`

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

## Workflows

Ritual de cierre de sesión: `/session-close` lo automatiza completo (retrospective → skill-kit-auditor → handoff). Equivale a ejecutar `/retrospective`, luego `skill-kit-auditor`, luego `/handoff` en ese orden. Aplicar los fixes aprobados del audit antes de generar el handoff.

## Regla de transición de modelo (vigente desde 2026-06-12)

Este proyecto fue calibrado con Fable 5, que infiere mucho desde contexto. Cualquier modelo que ejecute aquí (en especial Opus 4.8 después del 2026-06-22) debe compensar siguiendo lo escrito de forma literal:

1. **Seguir los checklists al pie de la letra.** El estándar de calidad por entregable vive en `docs/estandar-de-entregables.md` — correr el checklist de la sección que aplique ANTES de declarar algo listo. Si un ítem falla, corregir y re-verificar.
2. **Correr los lints de las skills antes de entregar** (greps de muletillas, conteos, fórmulas de título). Los criterios son verificables a propósito: verificarlos, no estimarlos.
3. **Consultar MEMORY.md y el handoff más reciente antes de actuar.** Las decisiones de juicio ya tomadas están escritas ahí y en `docs/roadmap-future-proofing.md`; no re-derivarlas ni contradecirlas sin preguntar.
4. **Si una tarea requiere juicio que no está escrito, preguntar al usuario** en vez de improvisar — y al resolverla, escribir la regla nueva donde corresponde.
