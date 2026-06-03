# CLAUDE.md — Mr. Putrid's Den

Este workspace es exclusivo de **Mr. Putrid's Den**, el podcast de Andrés y Juan sobre rock, metal, jazz y géneros variados.

## Al iniciar

Lee `podcast-profile.json` y responde en cachaco clásico bogotano:

> **Bienvenido de vuelta a la Guarida, sumerce.**
>
> ¿Qué producimos hoy?
>
> 1. **Guion** — script completo del próximo episodio
> 2. **Plan de grabación** — checklist para el día de grabación
> 3. **Show Notes / Metadata** — título, descripción SEO, temporada/episodio para Spotify
> 4. **Artwork del episodio** — prompts para portada Spotify (1:1) + Stories (9:16) + YouTube (16:9)
> 5. **Arte para redes** — material visual para lanzamiento en Instagram, Stories y más
> 6. **Social Media** — plan de lanzamiento 3 días con copy por plataforma
> 7. **Exportar HTML** — paquete de producción completo
> 8. **Actualizar perfil** — cambiar datos del podcast

---

## Reglas globales

- **Leer `podcast-profile.json` siempre** antes de cualquier workflow
- **Leer `glosario-cachaco.md` siempre** antes de generar cualquier guion (ahora contiene la guía de tono actualizada)
- **Consultar `eventos.json`** antes de generar el segmento de promoción
- **Lenguaje:** español colombiano casual — bogotano moderno, sin arcaísmos. Ver `glosario-cachaco.md`.
- **Formato documentos:** HTML optimizado para PDF vía IlovePDF
- **Backup:** después de cada guion/documento → git commit + push a GitHub + copia a G:\My Drive\ si está montado
- **Production assets en E:, no en C:** — Scripts HTML, propuestas, documentos y artefactos de producción se guardan en `e:\Claude Project\Claude Projects\kit-skill-creator\.claude\skills\mrputridsden\`. Los archivos en `C:\Users\andre\.claude\skills\mrputridsden\` son solo instruction files. Nunca guardar guiones o documentos en C:.
- **Skill activa:** `.claude/skills/podcast-creator/SKILL.md`

---

## Tono del show

- Consultar `glosario-cachaco.md` antes de generar cualquier guion (contiene guía de tono actualizada)
- **Español colombiano casual** — bogotano moderno, sin arcaísmos de los 40's
- Al oyente: "usted" o "ustedes" — nunca "tú"
- Entre hosts: tuteo natural
- **PROHIBIDO:** "sumerce", "ala", "chirriado", "cachifo", "caray", "carachas" (arcaísmos) + "parcero", "bacano" (muy coloquiales) + "vosotros", "vos", "ché", "tío" (otros regionalismos)
- Claude al hablar con Andrés: español colombiano moderno, casual y directo
- ⚠️ **EP001 usa el tono cachaco ANTIGUO** (sumerce, caray, chirriado, cachifo) — ese tono fue removido desde EP002. NUNCA modelar el tono de EP002+ desde EP001. La fuente canónica de tono es `glosario-cachaco.md`, no el script del EP001.

---

## Flujo completo por episodio (EP.002+)

```
1. Guion
2. Plan de grabación
── GRABACIÓN ──
3. Show Notes / Metadata
4. Artwork del episodio  (Spotify 1:1 + Stories 9:16 + YouTube 16:9)
5. Arte para redes       (cuando redes estén activas)
6. Social Media          (cuando redes estén activas)
7. Exportar HTML
── BACKUP ──
```

Usar `templates/checklist-produccion-episodio.md` para trackear cada entregable.

---

## Segmentos permanentes

### La Silla Pútrida
- **Antes de cualquier guion** preguntar: *"¿Esta semana hay Silla Pútrida?"*
- Si SÍ → episodio gira 100% en torno al invitado, formato presencial (los 3 en el mismo cuarto)
- Flujo Narval: Claude investiga al invitado → genera doc prep para hosts → carta simple al invitado → bio + temas + NO-list → guion
- Segmento de Promoción al FINAL en este formato
- Guardar ficha en `fichas-invitados/[nombre].md`
- Templates: `templates/silla-putrida-*.md`
- Perfiles de invitado: `templates/preguntas-por-perfil.md`

### Segmento de Promoción
- En **todos** los episodios sin excepción (Juan lo conduce)
- Episodio normal → bloque intermedio (antes del cierre)
- Episodio Silla Pútrida → al final (antes del outro)
- Consultar `eventos.json` para eventos reales

---

## Estructura de episodios

**Episodio normal (co-host):**
```
1. Intro music (30 seg)
2. Bienvenida — Andrés y Juan
3. Tema principal — Bloque A
4. [INTERCAMBIO]
5. Tema principal — Bloque B
6. Segmento de Promoción (Juan)
7. Takeaway / Reflexión final
8. Outro music (30 seg)
```

**Episodio Silla Pútrida:**
```
1. Intro especial Silla Pútrida (30 seg)
2. Bienvenida + presentación del invitado
3. Bloque de preguntas — Bloque A
4. [INTERCAMBIO natural]
5. Bloque de preguntas — Bloque B
6. Cierre con el invitado (dónde encontrarlo)
7. Segmento de Promoción (Juan) — AL FINAL
8. Outro music (30 seg)
```

---

## Estructura de carpetas

```
mrputridsden/
├── podcast-profile.json          ← Estado central del sistema
├── glosario-cachaco.md           ← Consultar siempre antes de guiones
├── eventos.json                  ← Eventos para segmento de promo
├── audio/                        ← Intro y outro del show
├── scripts/                      ← Guiones en HTML (EP.001, EP.002...)
├── documents/                    ← Propuesta y documentos importantes
├── fichas-invitados/             ← Una ficha por invitado Silla Pútrida
├── templates/                    ← Templates: cuestionario, invitación, prep hosts
└── .claude/skills/podcast-creator/
    ├── SKILL.md
    └── workflows/
        ├── 00-setup.md
        ├── 01-episodio.md
        ├── 02-grabacion.md
        ├── 03-artwork.md
        ├── 04-social-media.md
        ├── 05-show-notes.md
        └── 06-html-export.md
```

---

## Backup automático

Después de cada guion o documento generado:
```
git add [archivo]
git commit -m "EP.XXX — [título] — YYYY-MM-DD"
git push origin main
```
Si G: está montado → copiar también a `G:\My Drive\kit-podcast-creator\projects\mrputridsden\`

## Recovery de scripts

Si un guion aparece como `deleted` en `git status`:
1. **Primero ofrecer:** `git restore .claude/skills/mrputridsden/scripts/<archivo>` — recupera en segundos
2. Solo proponer regeneración completa si el usuario prefiere versión nueva o el archivo nunca fue commiteado

---

## Datos de contacto

- Web: www.mrputridsden.com
- General: hello@mrputridsden.com
- Andrés: Andres@mrputridsden.com
- Juan: Juan@mrputridsden.com
- GitHub: https://github.com/AndyB840506/claude-code-skills.git
- Google Drive: drive.google.com/drive/folders/1_gblT3LGmOIyY5Ia7NllqrK7VYMJ2ikR

---

## Environment

- OS: Windows. Use PowerShell for all shell/file operations, NOT Bash/xcopy. PowerShell version is 5.1, so avoid backtick-quotes, Unicode chars, and inline if-expressions.
- Claude config and operational rules live on C: (`~/.claude/`); project files live on E:. Do not propose junctions for `~/.claude/`.

## Verification

- When the user reports an error (e.g., JSON parse, BOM), do NOT claim it is fixed after a single edit—reproduce/test the fix and confirm the error is actually gone before reporting success.
- For env-var/ID issues, have the user copy IDs directly from the browser URL to avoid typos.

## Transcripts & Subtitles

- When generating timed transcript/subtitle output, use SRT format directly; do not post-process TXT output, which loses lines and timestamps.

## Approvals

- Present a plan and wait for explicit approval before executing multi-step work; respect 'no' on enrichment/bypass steps and never bypass private profiles.
