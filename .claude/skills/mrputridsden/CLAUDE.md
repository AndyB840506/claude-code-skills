# CLAUDE.md — Mr. Putrid's Den

Este workspace es exclusivo de **Mr. Putrid's Den**, el podcast de Andrés en solitario sobre rock, metal, jazz y géneros variados.

**Formato desde 2026-07-17:** Juan dejó el proyecto — Andrés continúa solo. Hasta EP.004 el show fue co-host (Andrés y Juan); EP.005 en adelante es formato solo. Toda la sección "Regla de balance co-host" más abajo describe el formato HISTÓRICO (EP.002-EP.004) — no aplica a episodios nuevos. Ver memoria `project_mpd_juan_departure`.

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
- **Production assets en mrputridsden-production, no en la skill** — Scripts HTML, propuestas, documentos y artefactos de producción se guardan en `C:\Users\andre\repos\kit-skill-creator\mrputridsden-production\`. La carpeta de la skill (`.claude\skills\mrputridsden\`) es solo instruction files. (Andres usa dos PCs: el escritorio SÍ tiene E: — ahí vive E:\Transcriptor; el portátil solo C:/D:.)
- **Skill activa:** `C:\Users\andre\repos\kit-skill-creator\.claude\skills\podcast-creator\SKILL.md` (project-scoped, en la raíz de `.claude/skills/`, no anidada dentro de esta carpeta)

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
3. Show Notes / Metadata  ⚠️ ep00X-metadata.md puede ya existir con estimados del script — actualizar, no crear nuevo
4. Artwork del episodio  (Spotify 1:1 + Stories 9:16 + YouTube 16:9)
5. Arte para redes       (cuando redes estén activas)
6. Social Media          (cuando redes estén activas)
7. Exportar HTML
── BACKUP ──
```

Usar `mrputridsden-production\templates\checklist-produccion-episodio.md` para trackear cada entregable.

**Episodio único de ~43 min (decisión Andy 2026-07-17, reemplaza el default de 2 partes):** desde EP.005, formato solo, target de duración 43 min — el sweet spot de retención para el show en su nueva etapa, dentro del mismo rango editorial 40-45 min ya fijado para BTQ/CCC. `word_count_target` del perfil (5543 palabras escritas) usa la calibración REAL propia de MPD desde EP.005 (primer episodio solo grabado, SRT real: 159 wpm + 23.5% de expansión en vivo — menor que el +35.5% de BTQ que se usó como estimado antes de grabar EP.005, lo que hizo que ese episodio saliera corto, ~35.8 min). Ver `mrputridsden-production/guion-style-mpd.md` para la tabla completa; recalibrar cada 2-3 episodios contra el SRT real (muestra actual: n=1).

**Regla histórica retirada — 2 partes por defecto (vigente EP.002-EP.004, decisión Andy 2026-06-17):** los episodios co-host se producían por defecto en 2 partes porque la investigación profunda + anécdotas ciertas poco conocidas pasaban la hora (EP.004 Kraken ~2h45; EP.005 Aterciopelados se había escrito como ~90 min/2 partes bajo formato co-host, guion descartado). Esa regla ya NO aplica a episodios nuevos — con formato solo y target 43 min, la profundidad de investigación debe caber en un episodio único; si algún tema puntual sigue sin caber, consultar con Andrés antes de partir en 2 (ya no es el default automático). Ver `01-episodio.md` (regla de 2 partes, referencia histórica) y memoria `project-mpd-episodes-two-parts` (retirada).

---

## Segmentos permanentes

### La Silla Pútrida
- **Antes de cualquier guion** preguntar: *"¿Esta semana hay Silla Pútrida?"*
- Si SÍ → episodio gira 100% en torno al invitado, formato presencial (los 3 en el mismo cuarto)
- Flujo Narval: Claude investiga al invitado → genera doc prep para hosts → carta simple al invitado → bio + temas + NO-list → guion
- Guardar ficha en `mrputridsden-production\fichas-invitados\[nombre].md`
- Templates: `mrputridsden-production\templates\silla-putrida-*.md`
- Perfiles de invitado: `mrputridsden-production\templates\preguntas-por-perfil.md`

### Segmento de Promoción — RETIRADO (2026-07-17)
Dependía del conocimiento insider de Juan como promotor de eventos underground; sin fuente de
reemplazo, Andrés decidió cortarlo en vez de reasignarlo. `eventos.json` queda deprecado (no
consultar). No incluir este segmento en ningún guion nuevo. Ver memoria `project_mpd_juan_departure`.

---

## Estructura de episodios

**Episodio normal (solo, EP.005 en adelante):**
```
1. Intro music (30 seg)
2. Bienvenida — Andrés
3. Tema principal — Bloque A
4. Tema principal — Bloque B
5. Takeaway / Reflexión final
6. Outro music (30 seg)
```
Sin Segmento de Promoción (retirado 2026-07-17, ver Segmentos permanentes).
Sin [INTERCAMBIO] entre hosts — es monólogo conversacional (Andrés se dirige directo al oyente, no a un co-host). Puede simular diálogo interno (pregunta retórica → respuesta) para mantener ritmo, pero no hay segunda voz real.

**Formato histórico (co-host, EP.002-EP.004) — archivado, no aplica a episodios nuevos:**
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
- Regla de balance co-host (Andrés ~70% de segmentos, Juan ~30% con entrega pausada/gravedad, nunca hype/exclamación) — conservada aquí como referencia de tono histórico de EP.002-EP.004, pero deja de aplicarse: no hay más bloques que asignarle a Juan.
- Referencia canónica de la voz de Juan (para consulta histórica, no para nuevos guiones): EP002-black-sabbath-genesis-heavy-metal.html.

**Reglas anti-repetición de guion (feedback 2026-06-12, derivado de comparar guiones vs. transcripción real EP.003):**
1. **Presupuesto de muletillas:** máximo 1 "imagínense" y 1 "me vuela la cabeza"/"les va a volar la cabeza" por episodio. No escribir "o sea", "básicamente", "totalmente", "agárrense de la silla" — los hosts ya los improvisan de sobra al aire.
2. **Prohibidas las líneas de pura validación** ("Eso es una locura", "Una locura total"): cada afirmación debe aportar un dato nuevo, una imagen o un contrapunto. Formato solo: usar el diálogo interno (pregunta retórica → matización, o "uno pensaría X, pero...") en vez de un segundo host, para no perder la tensión que antes daba el desacuerdo entre Andrés y Juan.
3. **Léxico propio del episodio:** Andrés habla en imágenes y escenas — evitar repetir la misma muletilla o expresión de firma entre bloques. *(Regla 3 histórica EP.002-EP.004: léxico firmado por host — Andrés imágenes/escenas, Juan números/venues/fechas — ya no aplica sin segundo host.)*
4. **No anunciar el hype — dejar que el dato aterrice solo:** "Y llegaron a Noruega" pega más que "el dato que les va a volar la cabeza es que llegaron a Noruega".
5. **Apertura:** no volcar la agenda completa del episodio ("hoy vamos a ver A, B, C, D"); un solo gancho. Variar el dispositivo de apertura entre episodios (cold open dentro de una escena es opción válida).
6. **Listas → una escena:** en vez de enumerar 5-7 nombres/hitos, elegir UNO y darle una escena vívida; el resto va a show notes. Nunca recitar la misma cadena/secuencia dos veces en un episodio.
7. **Transiciones de contenido, no meta-anuncios:** prohibido "nos vamos a recomendaciones" / "ya vamos a avanzar"; la última frase de un segmento contiene el gancho del siguiente.
8. **Turnos cortos:** bloques escritos largos invitan a rellenar con muletillas al improvisar — preferir turnos más cortos con interrupciones diseñadas.
9. **Lint al terminar el guion:** contar ocurrencias de muletillas (regla 1) y líneas de validación (regla 2) antes de entregar; reportar el conteo. *(El balance 70/30 co-host ya no aplica — formato solo desde EP.005.)*

**Formato HTML de scripts (EP.003 v2 en adelante):**
- Bloques de diálogo: sin fondo, solo borde izquierdo sutil (gris Andrés; azul claro Juan, ya no aplica en episodios solo — un solo color desde EP.005)
- Bloques info (dato, leyenda, recomendacion): tint muy claro, no fondos oscuros
- Container: 780px · Fuente base: 15px · Line-height: 1.85
- Referencia CSS canónica: `mrputridsden-production\scripts\EP003-raices-del-rock-sister-rosetta-tharpe.html`

**Episodio Silla Pútrida:**
```
1. Intro especial Silla Pútrida (30 seg)
2. Bienvenida + presentación del invitado
3. Bloque de preguntas — Bloque A
4. [INTERCAMBIO natural]
5. Bloque de preguntas — Bloque B
6. Cierre con el invitado (dónde encontrarlo)
7. Outro music (30 seg)
```

---

## Estructura de carpetas

**Skill (instrucciones — esta carpeta):**
```
mrputridsden/
├── podcast-profile.json          ← Estado central del sistema
├── glosario-cachaco.md           ← Consultar siempre antes de guiones
├── eventos.json                  ← Eventos para segmento de promo
├── SKILL.md
└── CLAUDE.md
```

**Skill compartida (workflows de producción, en la raíz de `.claude/skills/`, no anidada aquí):**
```
.claude/skills/podcast-creator/
├── SKILL.md
└── workflows/
    ├── 00-setup.md
    ├── 01-episodio.md
    ├── 02-grabacion.md
    ├── 03-artwork.md
    ├── 04-social-media.md
    ├── 05-show-notes.md
    ├── 06-html-export.md
    └── 07-youtube.md
```

**Producción (assets — carpeta propia, separada de la skill):**
```
C:\Users\andre\repos\kit-skill-creator\mrputridsden-production\
├── audio/                        ← Intro y outro del show
├── scripts/                      ← Guiones en HTML (EP.001, EP.002...)
├── episodios/                    ← Metadata, social y artwork por episodio (ep001-metadata.md, social-ep002.md...)
├── documents/                    ← Propuesta y documentos importantes
├── fichas-invitados/             ← Una ficha por invitado Silla Pútrida
├── templates/                    ← Templates: cuestionario, invitación, prep hosts
└── website/                      ← Sitio web (mrputridsden.com), incluye .vercel/
```

**Por qué están separadas:** producción anidada dentro de la carpeta de skill creó copias huérfanas del SKILL.md cuando se exportó/copió el proyecto (detectado y corregido 2026-06-07 — ver memoria `assets-on-e-drive`). La skill SOLO contiene instrucciones; los assets viven en su propia carpeta.

---

## Sitio web (mrputridsden.com)

### Estructura vigente (overhaul de Temporada 2, 2026-07-22)

El sitio se rehizo con el sistema visual "La Guarida". **La regla vieja del grid de 4 cards ya no
aplica**: `.episode-card` y `.episodes-grid` no existen en el HTML actual. Las secciones son:

- `#hero` — la escena oficial de T2 como telón fijo + la tarjeta de Expediente 01
- `#guarida` — qué es el show ahora
- `#expediente` — el episodio de estreno (portada + sinopsis)
- `#archivo` — **Temporada 1 completa**, filas `.arch-row`, de la más vieja a la más nueva
- `#residente`, `#escucha`, `#contacto`

**Al publicar un episodio nuevo de T2:** agregarlo como fila propia de temporada 2 (o promoverlo
desde el bloque de expediente), NO rotar el archivo de T1 — T1 está cerrada y se conserva entera.
La regla de rotación de BTQ ya no espeja acá.

**Nunca prometer fechas ni duración de un episodio sin grabar** (decisión de Andrés 2026-07-22):
la estimación de EP.005 falló por 6 minutos. El estado se expresa como "Expediente: Abierto".

### Deploy — NO usar `vercel --prod`

`vercel.json` tiene `"ignoreCommand": "exit 0"`, así que un `vercel --prod` normal genera un
deployment VACÍO y produccion devuelve 404. Hay que usar el **flujo prebuilt**, y el proyecto
correcto es `mr-putrids-den-web` (el viejo `v0-mr-putrids-den` quedó huérfano tras el renombre
del 2026-07-19; un `.vercel/project.json` stale apunta ahí y el deploy "funciona" sin cambiar nada).

Verificar el proyecto real antes de desplegar:
`vercel inspect https://www.mrputridsden.com --scope mrputridsden` → el campo `name`.

Pasos completos en `deploy-preflight` Paso 7 y en la memoria `reference_mpd_website_live`.

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
1. **Primero ofrecer:** `git restore mrputridsden-production/scripts/<archivo>` — recupera en segundos
2. Solo proponer regeneración completa si el usuario prefiere versión nueva o el archivo nunca fue commiteado

---

## Datos de contacto

- Web: www.mrputridsden.com
- General: hello@mrputridsden.com
- Andrés: Andres@mrputridsden.com
- Juan: Juan@mrputridsden.com — inactivo, Juan dejó el proyecto el 2026-07-17
- GitHub: https://github.com/AndyB840506/claude-code-skills.git
- Google Drive: drive.google.com/drive/folders/1_gblT3LGmOIyY5Ia7NllqrK7VYMJ2ikR

---

## Environment

- OS: Windows. Use PowerShell for all shell/file operations, NOT Bash/xcopy. PowerShell version is 5.1, so avoid backtick-quotes, Unicode chars, and inline if-expressions.
- Claude config and operational rules live in `~/.claude/`; project files live in `C:\Users\andre\repos\`. Do not propose junctions for `~/.claude/`.

## Verification

- When the user reports an error (e.g., JSON parse, BOM), do NOT claim it is fixed after a single edit—reproduce/test the fix and confirm the error is actually gone before reporting success.
- For env-var/ID issues, have the user copy IDs directly from the browser URL to avoid typos.

## Transcripts & Subtitles

- When generating timed transcript/subtitle output, use SRT format directly; do not post-process TXT output, which loses lines and timestamps.

## Approvals

- Present a plan and wait for explicit approval before executing multi-step work; respect 'no' on enrichment/bypass steps and never bypass private profiles.
