# Step 2 — Generate all 4 assets in parallel

Generate all four blocks in a single response. Label each block clearly.

**Fact-check real-world claims before finalizing (confirmed EP.019 — "Tim Collins" said
on air for the real author Jim Collins).** Verbatim-matching the transcript only confirms
the words were actually said; it doesn't confirm they're correct. Before publishing, scan
the transcript for named real-world entities the episode cites — authors, historical
figures, dates, attributed quotes — and verify each is accurate. If something said on air
is wrong, don't silently propagate it into public assets, and don't silently "correct" it
either: ask the user to confirm before using the corrected version.

## A · Spotify SEO

**Episode title (fórmula vigente — actualizada 2026-07-25 con el giro macro):**
`EP.XX — [Teórico o ley]: [frase llana con keyword de gestión]`
- **El teórico o la ley van primero**, no un referente pop: el roadmap es 100% pilar SEO desde
  2026-07-21 y el carril pop-culture está en pausa. Regla completa y precedentes en
  `btq-production/guion-style-btq.md` § Título.
- La keyword buscable NO es opcional, pero **ya no es «BPO / call center»**: el giro de alcance
  del 2026-07-25 sacó al show del techo de contact center. Usar keywords de gestión —
  *liderazgo, gestión de equipos, indicadores, calidad, medición del desempeño*. Ejemplo real
  aprobado (EP.023): `EP.23 — Efecto Hawthorne: por qué su equipo rinde distinto cuando lo miran`.
- **EP.020 no se retitula** — rankeó con la keyword vieja y se deja como está a propósito.
- Numeración `EP.XX` exacta (dos dígitos, mayúsculas). Nunca "Ep.X", "EP.0XX de tres
  dígitos" ni sufijo "| Behind the Queue" en Spotify.

**Preview (first 100 chars shown before "...more"):**
Punchy hook — use the cultural reference as the entry point. No quotes. No spoilers.

**Formato copy-safe (OBLIGATORIO):** la descripción de Spotify se entrega también en
**HTML markup** (Spotify acepta HTML en el campo descripción) — cada párrafo en `<p>…</p>`,
links en `<a href>`. Razón: al pegar texto con saltos manuales a mitad de párrafo, Spotify
los colapsa y pega palabras ("a que la\ncrisis" → "lacrisis"). Detectado en EP.017.
La versión texto plano se mantiene en una sola línea por párrafo (sin saltos manuales
internos) como fallback. YouTube NO acepta HTML — ahí va solo texto plano.

**Full description (250–400 words):**
- Opens with the cultural reference connection
- States the operational/leadership question the episode answers — keyword (BPO/liderazgo)
  dentro de las primeras 2 líneas
- Lists 3 concrete takeaways without numbering them
- Closes with the Closing TM phrase verbatim
- Antes del CTA: una **pregunta personal y comentable** dirigida al oyente (efecto
  EP.016 "The Wall" — 7 comentarios en un día porque el título lo interpelaba a él,
  no al personaje)
- Ends with: "Escúchalo ahora en Spotify."
- **Bloque de contacto OBLIGATORIO al final** (igual que YouTube — se omitió por error en EP.017):
  ```
  📩 andy@behind-thequeue.com | 🌐 behind-thequeue.com
  📸 Instagram: @behindthequeue84 | 🎵 TikTok: @behind.the.queue | 📘 Facebook: facebook.com/behindthequeue
  💼 LinkedIn: linkedin.com/company/behind-the-queue
  ```

**Tags (8–12):** Mix of Spanish-language operational + show + cultural + LATAM

**Word count check (OBLIGATORIO, verificar antes de entregar el bloque):** contar las
palabras reales de la "Full description" con una herramienta programática (no a ojo, no
confiar en un conteo autoreportado) y confirmar que cae entre 250 y 400. Lección de
Corporate Crime Confidential EP.001 (2026-07-04, ver `podcast-creator/workflows/01-episodio.md`
Paso 4): un script declaró un word count en su propio texto sin verificarlo nunca y quedó
a la mitad del target real. Si el conteo real cae fuera de 250–400, ajustar antes de
presentar el bloque para aprobación.

---

## B · Social Plan — 4-Day Calendar

Regla de producción: grabación los sábados, lanzamiento en Spotify los domingos a las
8:00 PM hora Colombia (la audiencia escucha el domingo de noche en modo "preparación
para la semana" — ver `btq-project/SKILL.md` §10, fuente canónica de este calendario).

| Day | Platform | Copy |
|-----|----------|------|
| Jueves (intriga) | LinkedIn | ... |
| Jueves (intriga) | Instagram / Facebook | ... |
| Jueves (intriga) | Story slides (3) | [slide 1] · [slide 2] · [slide 3] |
| Sábado (calentamiento) | Instagram / Facebook | behind the scenes mientras graba |
| Domingo 8:00 PM (lanzamiento) | LinkedIn | ... |
| Domingo 8:00 PM (lanzamiento) | Instagram / Facebook | ... |
| Lunes 7–8 AM (pico de escucha) | LinkedIn | "arrancando la semana" — el episodio como herramienta para la semana que empieza |
| Martes (refuerzo) | LinkedIn | ... |
| Martes (refuerzo) | Instagram / Facebook | ... |

**Rules:**
- Jueves: don't reveal the full topic — sembrar la pregunta, crear tensión
- Sábado: contenido orgánico, costo cero — detrás de cámaras de la grabación
- Domingo 8PM: lanzamiento — episodio disponible, CTA directo
- Lunes 7–8 AM Colombia: post de LinkedIn montado sobre el pico real de escucha
  (analytics EP.016: lunes = día récord de impresiones, 124; la audiencia escucha
  lunes-martes en el trabajo, no el domingo en la noche) — aprobado 2026-06-12
- Martes: refuerzo/herramienta — profundiza para quien ya escuchó, engancha a quien no
- LinkedIn: 5–8 hashtags · el link va en el PRIMER COMENTARIO, con su texto escrito
  aparte — **y qué link depende del día** (ver §B.1)
- Instagram/Facebook: 10–15 hashtags · día de lanzamiento termina con una pregunta
- TikTok copy: ultra short (2–3 lines) for all four days
- **LinkedIn es la plataforma prioritaria** — la audiencia núcleo es hombre 35–44
  supervisor/gerente BPO (43% del total), y 15% escucha en desktop en el trabajo.
  El copy de LinkedIn se escribe primero y con más cuidado; IG/FB derivan de él.
- **La pregunta del día de lanzamiento interpela al oyente, no al personaje** — "¿qué
  muro construiste tú?" funciona; "¿qué opinas de Pink Floyd?" no (efecto EP.016:
  7 comentarios). Aplicar el mismo principio en las 4 plataformas.
- **Clips/quotes para redes salen del episodio que el algoritmo ya empuja** (hoy:
  EP.012 Bohemian Rhapsody, 149 impresiones Home) — al promocionar el catálogo, usar
  ese como puerta de entrada, no el más reciente.

---

### B.1 · El artículo del episodio — destino y fuente de los cortes

Desde 2026-07-28 cada episodio tiene una página de texto en
`behind-thequeue.com/episodios/<slug>`. No es un extra del sitio: es **el destino
que le faltaba a LinkedIn**. Un gerente que ve el post el lunes a las 7 AM en la
oficina no puede darle play — puede leer. Ese es el hueco que tapa.

**Qué link va en el primer comentario, por día:**

| Día | Link | Por qué |
|-----|------|---------|
| Jueves (intriga) | **artículo** | el episodio todavía no existe; el artículo sí da a dónde ir |
| Domingo (lanzamiento) | **Spotify** | el objetivo del día es la reproducción, no la lectura |
| Lunes 7–8 AM | **artículo** | están en el trabajo, en desktop, sin audífonos |
| Martes (refuerzo) | **artículo** | va dirigido a quien ya escuchó: profundizar es leer |

El post del domingo puede llevar el artículo como **segundo** link dentro del mismo
comentario ("y si prefiere leerlo: ..."), nunca en lugar de Spotify.

**Los 4 posts se cortan del artículo, no del guion.** El artículo ya hizo el trabajo
de destilar el guion a tesis + cifras verificadas + aplicación; volver al guion para
cada post repite ese trabajo y abre la puerta a que un post afirme algo que el
artículo no sostiene. Orden: guion → artículo → posts.

> **Nota honesta sobre la regla del primer comentario.** La creencia de que LinkedIn
> penaliza los enlaces externos en el cuerpo del post está muy repetida en marketing
> pero **no tiene fuente primaria de la plataforma**. La regla se mantiene porque no
> cuesta nada, no porque esté verificada. Si alguien mide lo contrario, cámbiese.

**Imagen del preview (`og:image`):** cada artículo usa la **portada 16:9 de su propio
episodio** (`/og/btq-epNNN.png`), no la `og-image.png` genérica del sitio. En LinkedIn
la imagen del preview es lo que decide el clic, y con la genérica todos los episodios
se veían idénticos en el feed. Se usa la portada y **no** una quote card: la portada
nombra el episodio, la quote card arranca a mitad de frase y se lee mal debajo de un
titular. El archivo se copia desde `E:\AI\outputs\BTQ-EPNNN\BTQ-EPNNN-COVER-16x9.png`
al directorio de deploy; pesa ~50 KB, muy por debajo del límite de 500 KB.

---

**Core hashtags (always include):**
```
#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio
#BPO #ContactCenter #ServicioAlCliente #Operaciones #LATAM #Colombia #CustomerExperience
LinkedIn: #Liderazgo + topic-specific
Cultural: episode-specific tag
```

---

## C · YouTube Metadata — SÍ se genera. El RSS crea el episodio; Andy lo edita a mano.

> **Aclarado 2026-07-26 (corrige el retiro que se escribió ese mismo día).** El episodio
> **llega solo a YouTube por ingesta del RSS**, con la metadata de Spotify. Andy **entra a
> editarla manualmente** — así que esta sección sigue viva y los capítulos con timestamps
> siguen importando. Lo único que cambió respecto a antes del 2026-07-26 es **cómo nace el
> ítem**: ya no hay subida manual del archivo, y la metadata del RSS es el punto de partida
> que se sobrescribe, no una hoja en blanco.

**Before generating, check the most recently published episode's actual YouTube page**
(e.g. EP.015 — `https://youtu.be/DsRGtiimlAg`) — the format below reflects real production
practice, which may keep evolving past what's written here. If WebFetch can't render the
page (YouTube is a JS-heavy SPA and often returns unusable HTML), fall back to the format
documented here — it was captured directly from a YouTube Studio screenshot, not scraped.

- **Title:** Long, hook-style — `[Hook / cultural reference]: [punch line] | EP.0XX | Behind the Queue`.
  No hard 60-char limit in practice (EP.015's title runs ~95 chars). El punch line
  lleva al menos una keyword buscable (BPO / liderazgo / call center) — misma regla
  que el título de Spotify (§A).
- **Description structure** (matches EP.015 exactly — 5 blocks in this order):
  1. Hook paragraph (2–3 sentences, the "honest question")
  2. Episode summary paragraph (cultural reference as lens + leadership lesson)
  3. `CONTENIDO DEL EPISODIO` — timestamped chapter list (see Chapter timestamps below)
  4. `ENCUENTRA BTQ EN` — links block: website · Spotify · email · LinkedIn (full name) · Instagram
  5. Hashtags (space-separated `#Tag`, NOT comma-separated — see Tags vs. hashtags below)
- **Tags field** (YouTube Studio metadata box, separate from the description): 15–20
  keywords, comma-separated — see Tags vs. hashtags below
- **Thumbnail text:** 3–5 words max · high contrast · brand voice (Bebas Neue / uppercase style)

**If the audio gets re-transcribed after chapters/quote cards were already generated**
(e.g. Andy re-exported to fix an intro/outro timing bug — confirmed BTQ EP.020): don't
regenerate the assets from scratch. Recalculate only the timestamps against the new SRT —
the copy/text of every block stays the same, only where each quote/chapter anchors moves.

**Chapter timestamps:**
Before saying timestamps aren't available, check the diarized transcript at
`E:\Transcriptor\transcripciones\[Show] Ep.[N].srt` — note the show uses **no zero-padding**
(e.g. `Behind The Queue Ep.16.srt`, not `Ep.016.srt`). Locate section transitions by
searching for topic-keyword phrases (framework/author names, segment names like
"Aplicable Hoy", cultural references). Real timestamps from the transcript beat guessed ranges.

**Tags vs. hashtags — never conflate these, both belong in the metadata:**
- **Tags / keywords** (distinct SEO metadata fields: YouTube Studio Tags box, Spotify
  keyword/SEO tags — NOT the hashtags inside post copy) = comma-separated
  list. Format: `tag1, tag2, tag3, ...`
- **In-content hashtags** (inside YouTube/description text AND the §B social posts) = a
  separate, smaller set, space-separated with `#` prefix, for in-feed discoverability.
  Format: `#Tag1 #Tag2 #Tag3`
- Generate both where the platform has both — don't drop one in favor of the other.

---

## D · Portadas — NO se escriben prompts (v4, 2026-07-25)

> ⚠️ **Esta sección pedía prompts de IA hasta el 2026-07-25.** Toda la dirección v3 que
> describía —oro `#C9A84C`, negro `#0A0A0A`, siluetas a contraluz, estética fiel a la época del
> referente pop— **está retirada**. Si algo de eso reaparece en un asset, el asset está mal.

Las portadas de episodio **ya no se generan con un modelo**: se componen deterministas con PIL.
No hay prompt que redactar en este paso.

```
python comfyui/templates/portada-ep-compose.py @titulo.txt
```

- Recibe el **título publicado completo** y lo parsea; aborta si no cumple la fórmula del §A.
  Es a propósito: garantiza que portada y metadata no diverjan, y de paso hace de lint del título.
- Acepta `@archivo.txt` porque PowerShell 5.1 pierde los acentos al pasar por `argv`.
- Salidas: 1:1 · 16:9 · 9:16 + contrapruebas 300/96.

**Compuerta antes de aprobar:**

```
python scripts/verify_assets.py EP0XX --root E:\AI\outputs\BTQ-EP0XX --show btq
```

Más `--stage-a` si el episodio todavía no se ha grabado (sin audio no hay quote cards y la
compuerta falla por cards faltantes).

La dirección visual, la paleta y el checklist de aprobación viven en
`docs/brand-constants.md` § "Dirección de artwork v4" — **esa es la fuente, no esta sección.**
Las quote cards son también tipografía pura: ver § Quote Cards del mismo archivo.
