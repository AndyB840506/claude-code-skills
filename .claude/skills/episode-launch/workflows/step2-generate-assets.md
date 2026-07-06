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

**Episode title (formula obligatoria — analytics 2026-06-12):**
`EP.XX — [Referente]: [frase con keyword BPO / liderazgo / call center]`
- La keyword buscable NO es opcional: los títulos pop-culture sin keyword ganan algoritmo
  pero son invisibles en Search (EP.01 sigue #1 all-time por las búsquedas de "BPO").
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
- LinkedIn: 5–8 hashtags · Spotify link goes in FIRST COMMENT (write comment text separately)
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

**Core hashtags (always include):**
```
#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio
#BPO #ContactCenter #ServicioAlCliente #Operaciones #LATAM #Colombia #CustomerExperience
LinkedIn: #Liderazgo + topic-specific
Cultural: episode-specific tag
```

---

## C · YouTube Metadata

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
  keyword/SEO tags, SafeCreative tags — NOT the hashtags inside post copy) = comma-separated
  list. Format: `tag1, tag2, tag3, ...`
- **In-content hashtags** (inside YouTube/description text AND the §B social posts) = a
  separate, smaller set, space-separated with `#` prefix, for in-feed discoverability.
  Format: `#Tag1 #Tag2 #Tag3`
- Generate both where the platform has both — don't drop one in favor of the other.

---

## D · Cover-Art Prompts (Nani Banana 2 / AI)

**Dirección visual congelada (2026-06-12, validada con EP.017):** todo prompt de portada
arranca de los bloques verbatim en `docs/brand-constants.md` § "Dirección de artwork"
(atmósfera de póster gráfico con siluetas a contraluz + footer). Solo se redacta nuevo
el sujeto central del episodio. Seguir su checklist (conteo de figuras, texto letra por
letra, cero caras) antes de aprobar cualquier generación.

**Principio de nostalgia (analytics 2026-06-12):** la audiencia núcleo (hombre 35–44)
responde a la estética FIEL A LA ÉPOCA del referente — el visual debe gritar "su
adolescencia", no una reinterpretación moderna. Queen con estética 70s/80s real, no
Queen estilizado 2026.

**Título del episodio en la portada (OBLIGATORIO — feedback EP.018):** los formatos
**1:1 y 9:16** llevan un bloque de tipografía con el TÍTULO del episodio en el tercio
superior, aparte del footer — NO basta con el `EP.0XX` del footer. Patrón validado
(EP.017 / EP.018): Línea 1 = referente cultural en gold ultra-bold (ej. "SODA STEREO",
"EL MUNDIAL"); Línea 2 = tagline con la keyword buscable, en blanco a un tercio del
tamaño (ej. "EL LIDERAZGO QUE SIGUE SONANDO", "LIDERAZGO SIN TOCAR EL BALON"). El
formato **16:9** es la excepción: usa un hook de thumbnail de 3-5 palabras (ej. "LA GIRA
/ SIN CERATI", "EL BALON / NO ES TUYO"), no el título completo. Texto de imagen sin
tildes; la frase con tildes va en el caption.

Generate one density-first prompt for each format. Each prompt must:
- Name the character and exact visual canon (source, era, costume)
- State the mood / color palette
- Include BTQ brand: void black `#0A0A0A` background · signal gold `#C9A84C` accents
- Specify composition for the format (centered 1:1 / vertical hero 9:16 / wide scene 16:9)
- Include footer rule: "Behind the Queue" left · **EP.0XX gold CENTER** · icons right
- End with accuracy checklist: 3 bullet points Claude must verify before approving
- PCB/circuits: ONLY for AI/tech episodes — NEVER on general covers

**Format: 1:1 (Spotify cover / platform square)**
**Format: 9:16 (TikTok / Stories)**
**Format: 16:9 (LinkedIn / YouTube thumbnail)**
