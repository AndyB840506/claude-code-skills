# Workflow 02 — Generación de assets

Genera todos los assets de publicación. **La ruta depende del show** — cada uno tiene
su propio orquestador/conjunto de workflows ya construidos; este pipeline los invoca
sin duplicar su lógica.

---

## Episodio dividido en partes (grabación larga)

Si un episodio se grabó tan largo que se publica en 2+ partes (ej. MPD EP.004 Kraken,
~2h45m → Parte 1 / Parte 2), confirma con el usuario la numeración y trátalo así:

- **Mismo número de episodio**, sufijo de parte en el título: `EP.0NN — Título (Parte 1)`.
- **Una sola metadata compartida; lo único que cambia es el título** (descripción, tags,
  datos = iguales). Incluye **una línea** que avise la continuación (ej. "el episodio salió
  tan largo que lo partimos en dos; la Parte 2 sale el próximo sábado") — el oyente de la
  P1 no sabe que hay más si no se lo dices.
- **Transcribe cada parte por separado** (Stage 1) → capítulos + duración **por parte**.
- **Quote cards:** al dividir, la frase fuente de una card puede caer en la OTRA parte.
  Valida cada card contra el SRT de la parte donde realmente se dijo, no asumas P1.
- Un placeholder de URL de Spotify **por parte**; cada parte se publica/despliega por separado.

---

## Ruta BTQ — invoca `episode-launch`

`episode-launch` ya genera en un solo paso: SEO de Spotify, plan social de 4 días,
metadata de YouTube, prompts de cover-art (1:1/9:16/16:9), corre su propio gate de
aprobación, y hace commit + push del archivo consolidado.

**Invócalo directamente, supliendo sus 6 inputs desde el episode brief — sin que
vuelva a preguntarlos:**

| Input que pide `episode-launch` | Viene de |
|---|---|
| EP number | `ep_number` |
| Title | `title` |
| Cultural ref | `cultural_ref` |
| Closing TM | `closing_tm` |
| Script path | busca `episodio-[NNN]-*.md`; si no existe, usa el SRT de Stage 1 como fuente y pasa "none" |
| Spotify URL | `spotify_url` |

Una vez los 6 campos estén confirmados, `episode-launch` genera los 4 bloques de
assets y presenta **su propio gate**: *"Assets listos para EP.0XX. ¿Apruebas o ajustas
algún bloque antes de hacer commit?"* — **deja que aparezca con normalidad**, no es un
error del pipeline. Espera la aprobación del usuario igual que lo haría `episode-launch`
solo.

Tras la aprobación, `episode-launch` guarda `btq-production/launch-assets/EP0XX-[slug]-launch.md`
y hace commit + push. **El pipeline no repite ninguna de estas acciones.**

**Lo único que el pipeline extrae de la salida**: los 3 prompts de cover-art (sección D
del output de `episode-launch`) — son el insumo de Stage 3.

---

## Ruta MPD — invoca workflows individuales de `podcast-creator`

MPD no tiene un orquestador equivalente, así que se invocan tres workflows por
separado, alimentados con el episode brief + el SRT del Stage 1:

1. **`podcast-creator/workflows/05-show-notes.md`** ("show notes" / "metadatos")
   → genera `shownotes-ep[NNN].md` (Spotify + Apple + Amazon + SEO keywords)
2. **`podcast-creator/workflows/07-youtube.md`** ("youtube metadata")
   → genera `youtube-ep[NNN].md` (título, descripción, tags, capítulos, miniatura)
   — reutiliza la descripción de Spotify recién generada como base
3. **`podcast-creator/workflows/03-artwork.md`** ("artwork")
   → genera `artwork-ep[NNN].md` con los 3 prompts (1:1/9:16/16:9)
4. **`podcast-creator/workflows/04-social-media.md`** ("social media")
   → genera `social-ep[NNN].md` (plan de lanzamiento 3 días, copy por plataforma)
   — invócalo en esta misma etapa, junto con los otros tres, no lo dejes para después:
   el plan social debe existir apenas el episodio está grabado/transcrito, sin esperar
   a que esté en vivo en Spotify (aprendido en MPD EP.005, donde nadie lo generó hasta
   2 días después de publicado porque este paso faltaba en la ruta MPD del pipeline).

Para cada uno: si el episode brief ya tiene el dato que el Paso 1 del workflow pediría,
sáltalo — pasa directo al paso de generación. Solo pregunta lo que genuinamente falte
(ej. vibe del artwork, si no se especificó).

**Lo único que el pipeline extrae de la salida**: los 3 prompts de `artwork-ep[NNN].md`
— son el insumo de Stage 3, igual que en la ruta BTQ.

---

## Cierre de Macro-Stage B — checkpoint de publicación en Spotify

Ambas rutas convergen aquí: la metadata de Spotify (descripción, título, SEO) que
acabas de generar es justo lo que el usuario necesita para publicar el episodio. Este
es el momento de resolverlo — **antes** de seguir a Stage C, donde tanto la rotación
del grid como el deploy-verify necesitan una URL real, no "pending".

**Si `spotify_url` en el brief ya es una URL real** (el episodio se publicó antes de
correr el pipeline), salta este checkpoint por completo — actualiza
`pipeline-state-ep[NNN].md` a `stage_b: complete, spotify_url: [URL]` y continúa.

**Si sigue como "pending"**, presenta la metadata lista para copiar/pegar y pide:

> "Aquí está la metadata de Spotify para EP.0XX. Súbela junto con el audio a Spotify
> for Podcasters y publícalo — vale la pena hacerlo ya, porque Spotify puede tardar en
> procesar el episodio antes de que quede en vivo, y la necesitamos para rotar el grid
> y verificar el deploy. Avísame la URL pública (open.spotify.com/episode/...) cuando
> esté disponible — mientras tanto seguimos con la validación de imágenes en paralelo."

Esto dispara el pedido (potencialmente lento, por el tiempo de procesamiento de
Spotify) **lo antes posible**, justo junto con la pausa de generación de imágenes de
Stage 3 — así el tiempo de espera de Spotify se solapa con el trabajo de imágenes en
vez de bloquear en serie.

- Si el usuario entrega la URL ahora: actualiza el brief y
  `pipeline-state-ep[NNN].md` → `stage_b: complete, spotify_url: [URL]`.
- Si el usuario sigue sin tenerla: marca `stage_b: complete, spotify_url: pending` de
  todas formas (la metadata y los assets ya están generados — eso es lo que define el
  cierre de esta etapa) y continúa. El checkpoint del Paso 0 de `00-intake.md`
  detectará el `pending` la próxima vez que se invoque el pipeline para este episodio
  y se detendrá ahí a pedir la URL — exactamente el caso de BTQ EP.16.

---

## Chequeo de consistencia — título/tagline (ambas rutas)

Antes de cerrar Stage B, verifica que el título/tagline del episodio sea el MISMO en
los tres lugares donde vive independientemente: el guion/script, la metadata de show
notes, y el artwork. Cada uno se genera en un paso separado y puede terminar con una
frase distinta si cada uno se deriva de una fuente distinta (ej. el guion trae su
propio tagline en el header, pero el artwork puede venir de un brief visual anterior
con otra frase) — nadie los cruza automáticamente. Detectado en MPD EP.005: la
metadata usaba el tagline del guion ("una gomela, un punkero") mientras el artwork ya
aprobado usaba otro ("de un bar de Bogotá al continente"), y quedó así hasta que el
usuario lo notó después de cerrar ambos pasos.

**Regla:** al generar la metadata (show notes) DESPUÉS de que el artwork ya esté
aprobado, usa el título/tagline del artwork como fuente de verdad — es lo que el
oyente ve primero y ya pasó por aprobación. Si el artwork se genera después de la
metadata, es al revés. En cualquier orden, el segundo artefacto en completarse debe
leer el título ya fijado por el primero, no derivar el suyo propio.

---

## Al terminar (ambas rutas)

1. Confirma: "Assets generados — [N] archivos. Prompts de cover-art listos para
   generación de imagen. [Spotify: URL confirmada / pendiente — te la pido más tarde]."
   y continúa a `03-image-validation.md`.
2. **Publica el paquete de lanzamiento como Artifact** (precedente: BTQ EP.020,
   2026-07-04). Son archivos `.md` planos — pásalos directo a la tool `Artifact` sin
   stripping (soporta Markdown nativo). BTQ: un solo Artifact para
   `EP0XX-[slug]-launch.md`. MPD: uno por archivo (`shownotes-`, `youtube-`, `artwork-`)
   salvo que el usuario prefiera verlos combinados en uno solo.
3. Agrega a la bitácora:
   ```
   ## Stage 2 — Generación de assets
   - Qué se hizo: [episode-launch invocado | podcast-creator workflows 05/07/03 invocados]
   - Archivos generados: [rutas]
   - Gate heredado: [aprobado por el usuario / N-A]
   - Checkpoint Spotify: [URL confirmada: ... / pendiente — usuario va a publicar]
   - Resultado: OK — 3 prompts de cover-art listos para Stage 3
   ```
