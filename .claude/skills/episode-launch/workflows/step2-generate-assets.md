# Step 2 — Generate all 4 assets in parallel

Generate all four blocks in a single response. Label each block clearly.

## A · Spotify SEO

**Preview (first 100 chars shown before "...more"):**
Punchy hook — use the cultural reference as the entry point. No quotes. No spoilers.

**Full description (250–400 words):**
- Opens with the cultural reference connection
- States the operational/leadership question the episode answers
- Lists 3 concrete takeaways without numbering them
- Closes with the Closing TM phrase verbatim
- Ends with: "Escúchalo ahora en Spotify."

**Tags (8–12):** Mix of Spanish-language operational + show + cultural + LATAM

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
| Martes (refuerzo) | LinkedIn | ... |
| Martes (refuerzo) | Instagram / Facebook | ... |

**Rules:**
- Jueves: don't reveal the full topic — sembrar la pregunta, crear tensión
- Sábado: contenido orgánico, costo cero — detrás de cámaras de la grabación
- Domingo 8PM: lanzamiento — episodio disponible, CTA directo
- Martes: refuerzo/herramienta — profundiza para quien ya escuchó, engancha a quien no
- LinkedIn: 5–8 hashtags · Spotify link goes in FIRST COMMENT (write comment text separately)
- Instagram/Facebook: 10–15 hashtags · día de lanzamiento termina con una pregunta
- TikTok copy: ultra short (2–3 lines) for all four days

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
  No hard 60-char limit in practice (EP.015's title runs ~95 chars).
- **Description structure** (matches EP.015 exactly — 5 blocks in this order):
  1. Hook paragraph (2–3 sentences, the "honest question")
  2. Episode summary paragraph (cultural reference as lens + leadership lesson)
  3. `CONTENIDO DEL EPISODIO` — timestamped chapter list (see Chapter timestamps below)
  4. `ENCUENTRA BTQ EN` — links block: website · Spotify · email · LinkedIn (full name) · Instagram
  5. Hashtags (space-separated `#Tag`, NOT comma-separated — see Tags vs. hashtags below)
- **Tags field** (YouTube Studio metadata box, separate from the description): 15–20
  keywords, comma-separated — see Tags vs. hashtags below
- **Thumbnail text:** 3–5 words max · high contrast · brand voice (Bebas Neue / uppercase style)

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
