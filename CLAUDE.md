# Creador de Skills para Claude Code

Este proyecto crea skills personalizadas para Claude Code. Una skill es un archivo que le enseña a Claude a hacer una tarea específica de forma repetible.

## Environment

Windows con PowerShell 5.1. Usar PowerShell (no Bash/xcopy) para operaciones de archivos. Evitar backtick-quotes, caracteres Unicode y expresiones if inline en scripts — PS 5.1 no los maneja correctamente.

Config y reglas operativas en C: (`~/.claude/`); archivos de producción en E:. No proponer junctions para `~/.claude/`.

## Comportamiento al iniciar

**Antes de responder nada**, sigue este orden:

1. **Sincroniza con GitHub:** ejecuta `git pull origin main`
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

No declarar un bug como corregido hasta haberlo verificado (re-ejecutar/reproducir). Para JSON parse errors, revisar específicamente BOM y respuestas API vacías.

## Workflows

Ritual de cierre de sesión: ejecutar `/retrospective`, luego `skill-kit-auditor`, luego `/handoff` en ese orden. Aplicar los fixes aprobados del audit antes de generar el handoff.
