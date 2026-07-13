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

**Default de 2 partes (decisión Andy 2026-06-17):** los episodios MPD se producen por defecto en 2 partes, porque la investigación profunda + anécdotas ciertas poco conocidas pasan la hora (EP.004 Kraken ~2h45; EP.005 Aterciopelados escrito como ~90 min/2 partes). Estructurar el corte P1/P2 desde el guion, cada parte con apertura/cierre y recap de ~20 seg al abrir la P2. Metadata compartida; solo cambia el título "(Parte 1)"/"(Parte 2)". Ver `01-episodio.md` (regla de 2 partes) y memoria `project-mpd-episodes-two-parts`.

---

## Segmentos permanentes

### La Silla Pútrida
- **Antes de cualquier guion** preguntar: *"¿Esta semana hay Silla Pútrida?"*
- Si SÍ → episodio gira 100% en torno al invitado, formato presencial (los 3 en el mismo cuarto)
- Flujo Narval: Claude investiga al invitado → genera doc prep para hosts → carta simple al invitado → bio + temas + NO-list → guion
- Segmento de Promoción al FINAL en este formato
- Guardar ficha en `mrputridsden-production\fichas-invitados\[nombre].md`
- Templates: `mrputridsden-production\templates\silla-putrida-*.md`
- Perfiles de invitado: `mrputridsden-production\templates\preguntas-por-perfil.md`

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

**Regla de balance co-host (actualizada 2026-06-11):**
- **Andrés lidera ~70% de los segmentos de contenido** mientras Juan gana experiencia al micrófono (decisión de Andrés, EP.004). Juan NO debe quedar mudo: tiene reacciones cortas en todos los bloques.
- **Juan lidera:** su segmento de Promoción (siempre) + 1-2 bloques puntuales de su expertise como promotor (shows en vivo, escena local). NO darle los bloques emocionales pesados ni los de mayor carga narrativa. Abre con autoridad pero SIN fórmulas declarativas teatrales ("Yo quiero contar esta historia porque...", "el momento que me pone la piel de gallina", "y esto es lo bonito") — esas frases lo hacen sonar leyendo, como un viejito (feedback EP.004, 2026-06-11). Juan abre diciendo el hecho directamente, estilo EP.002: frases cortas, declarativas, sin anunciar lo que va a contar. Referencia canónica de voz de Juan: EP002-black-sabbath-genesis-heavy-metal.html.
- **Escribir PARA la entrega de Juan, no contra ella (feedback 2026-06-12):** Juan habla muy pausado, registro de narrador de documental. Cuando se le escriben líneas de hype o exclamación ("¡Eso es una locura!") intenta imitar los improvs de Andrés y se queda corto — suena plano. Darle las frases que MEJORAN con pausa y gravedad: remates secos, sentencias, datos con peso, silencios dramáticos. NUNCA escribirle exclamaciones de energía ni reacciones de asombro improvisado. El contraste de entregas (Andrés energía/improv · Juan gravedad/pausa) es el sello del show, no un defecto a corregir.
- **Andrés lidera:** hilo narrativo, historia musicológica, conectores de episodio a episodio, bloques emocionales.
- Verificar al terminar el guión: contar bloques donde cada host abre el segmento — proporción objetivo ~70/30 a favor de Andrés.

**Reglas anti-repetición de guion (feedback 2026-06-12, derivado de comparar guiones vs. transcripción real EP.003):**
1. **Presupuesto de muletillas:** máximo 1 "imagínense" y 1 "me vuela la cabeza"/"les va a volar la cabeza" por episodio. No escribir "o sea", "básicamente", "totalmente", "agárrense de la silla" — los hosts ya los improvisan de sobra al aire.
2. **Prohibidas las réplicas de pura validación** ("Eso es una locura", "Total", "Exactamente eso", "No, totalmente"): toda réplica debe aportar un dato nuevo, una imagen o un contrapunto. Mínimo un desacuerdo o corrección genuina entre hosts por episodio — sin tensión, todo suena plano.
3. **Léxico firmado por host:** Andrés habla en imágenes y escenas; Juan en números, plata, venues, fechas, aforos. No compartir muletillas ni expresiones de firma entre los dos.
4. **No anunciar el hype — dejar que el dato aterrice solo:** "Y llegaron a Noruega" pega más que "el dato que les va a volar la cabeza es que llegaron a Noruega".
5. **Apertura:** no volcar la agenda completa del episodio ("hoy vamos a ver A, B, C, D"); un solo gancho. Variar el dispositivo de apertura entre episodios (cold open dentro de una escena es opción válida).
6. **Listas → una escena:** en vez de enumerar 5-7 nombres/hitos, elegir UNO y darle una escena vívida; el resto va a show notes. Nunca recitar la misma cadena/secuencia dos veces en un episodio.
7. **Transiciones de contenido, no meta-anuncios:** prohibido "nos vamos a recomendaciones" / "ya vamos a avanzar"; la última frase de un segmento contiene el gancho del siguiente.
8. **Turnos cortos:** bloques escritos largos invitan a rellenar con muletillas al improvisar — preferir turnos más cortos con interrupciones diseñadas.
9. **Lint al terminar el guion:** contar ocurrencias de muletillas (regla 1) y réplicas de validación (regla 2) antes de entregar; reportar el conteo junto con el balance 70/30.

**Formato HTML de scripts (EP.003 v2 en adelante):**
- Bloques de diálogo: sin fondo, solo borde izquierdo sutil (gris Andrés, azul claro Juan)
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
7. Segmento de Promoción (Juan) — AL FINAL
8. Outro music (30 seg)
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

### Regla de actualización del grid "Episodios recientes" — espeja la regla de BTQ
- Siempre 4 cards (`<div class="episode-card" data-ep="0XX">` dentro de `.episodes-grid`), orden oldest -> newest
- Muestra los 4 episodios ANTERIORES al que está en circulación — **NO incluye el nuevo** (su propio link/embed ya lo cubre)
- Al lanzar nuevo EP: rotar — entra el anterior al nuevo, sale el más antiguo del grid
- **Visual propio de MPD** — la lógica de rotación espeja a BTQ pero NUNCA su tipografía ni estilo de card (ver memoria `feedback_mpd_vs_btq_typography`); usa siempre el componente `.episode-card` existente
- Documentado también como comentario HTML en `website/index.html` justo antes de `<div class="episodes-grid">`

### Deploy
Desde `mrputridsden-production/website/`: `$env:NODE_OPTIONS="--use-system-ca"; vercel --prod` (bypass Avast SSL, igual que BTQ)

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
- Juan: Juan@mrputridsden.com
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
