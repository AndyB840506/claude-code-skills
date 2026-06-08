---
name: episode-launch
description: >
  BTQ Episode Launch Orchestrator — generates all publication assets for a single episode
  in one pass: Spotify SEO (description + preview), social plan 4-day calendar, YouTube
  title/description/tags/thumbnail/chapters, SafeCreative registration metadata,
  cover-art prompts (1:1 · 9:16 · 16:9), and git commit + push.
  Triggers: /episode-launch, lanzar episodio, launch EP, publicar episodio BTQ,
  generar assets episodio, metadata episodio, social plan BTQ, portada episodio.
---

# BTQ Episode Launch Orchestrator

You are **Laswell**. This skill generates every publication asset for a BTQ episode and
commits the result. It does NOT write the guión — for that use `btq-guion`.

---

## Step 1 — Collect inputs

Before asking, check `btq-production/pipeline-state-ep[NNN].md` — it usually already has
EP number, title, cultural ref, and Spotify URL confirmed. Ask only for what's still missing:

**Re-push caveat:** if the episode had to be re-uploaded to the podcast hosting/
distribution tool because it didn't appear live on Spotify on the first attempt,
treat any Spotify URL recorded before that re-upload as **unverified** — Spotify
can assign a new episode URL when a re-published feed item propagates. Confirmed
in EP.016 (`pipeline-state-ep016.md` recorded `episode/6GoODy...` as "confirmed",
but the live Spotify URL after the re-upload was `episode/3CNyTkA6...`). Ask the
user to paste the live URL from the Spotify browser page before propagating it
anywhere downstream (website, social posts, pipeline-state).

```
EP number:       EP.0XX
Title:           Full episode title
Cultural ref:    Character / film / song / game name
Closing TM:      "Y como diría [personaje]: [frase]"
Script path:     Relative path to the HTML script file (or "none")
Spotify URL:     Episode URL (or "pending" if not yet uploaded)
```

If the user says "same as handoff" or references a recent session, pull from memory.
Once all 6 fields are confirmed, proceed — no further questions.

---

## Step 2 — Generate all 4 assets in parallel

Generate all four blocks in a single response. Label each block clearly.

### A · Spotify SEO

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

### B · Social Plan — 4-Day Calendar

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

### C · YouTube Metadata

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
  3. `📋 CONTENIDO DEL EPISODIO` — timestamped chapter list (see Chapter timestamps below)
  4. `🔗 ENCUENTRA BTQ EN` — links block: 🌐 website · 🎵 Spotify · 📩 email · 💼 LinkedIn (full name) · 📸 Instagram
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

### D · Cover-Art Prompts (Nani Banana 2 / AI)

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

---

## Step 3 — Approval gate

After presenting all 4 asset blocks, ask:

> "Assets listos para EP.0XX. ¿Apruebas o ajustas algún bloque antes de hacer commit?"

Wait for explicit approval. If the user says "ajustar [bloque]" — revise only that block.
Once approved, proceed to Step 4.

---

## Step 4 — Git commit + push

Save generated assets as a markdown file at:
```
btq-production/launch-assets/EP0XX-[slug]-launch.md
```

Where `slug` = kebab-case of the cultural reference as confirmed in Step 1 — can be the
album/character/film title, not necessarily the artist (e.g., EP.016's cultural ref was
the album "The Wall", giving `EP016-the-wall-launch.md`).

Then run:
```
git add btq-production/launch-assets/EP0XX-[slug]-launch.md
git commit -m "feat(EP.0XX): launch assets — Spotify SEO, social plan, YouTube, artwork prompts

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

Confirm push output to user. If push fails (no remote / auth), report the error clearly
and do not retry destructively.

---

## Step 4a — SafeCreative Registration Metadata (on request, post-publish)

Generated separately — typically once the episode has a confirmed Spotify/YouTube URL,
NOT part of the Step 2 parallel batch. Format reference: EP.015 registration
(work ID 2605315837136).

- **Title:** `Behind the Queue · EP.0XX · [Cultural reference]: [hook]`
- **Work type:** Podcast
- **Summary** (one paragraph): `Episodio [N] del podcast Behind the Queue, conducido por
  Andrés Ricardo Bermúdez Rodríguez. En este episodio se analiza [cultural reference] como
  punto de entrada para explorar [organizational/leadership lesson] — y qué hace el líder
  que decide [actionable insight]. Producción original en español para audiencias de
  operaciones, servicio al cliente y liderazgo en BPO/contact center.`
- **Tags (~20–25, comma-separated):** mix of recurring brand tags (behind the queue,
  andrés bermúdez, liderazgo, bpo, español, podcast, latam, colombia, contact center,
  servicio al cliente, cultura, operaciones, información organizacional, experiencia)
  + episode-specific (cultural reference name, themes, named frameworks/authors)

---

## Step 4b — Update website episode grid (post-publish, once Spotify URL is live-verified)

The site at `behind-thequeue.com` (Vercel project `website`) shows the 4 most recently
published episodes in its `<div class="ep-list">` grid, oldest→newest (slot 1 = oldest,
slot 4 = newest — drop the oldest each time a new episode publishes).

1. Edit `btq-production/website/index.html` — the grid keeps the 4 most recent episodes
   ordered oldest→newest by EP number (slot 1 = lowest EP number = oldest, slot 4 = highest
   = newest; see the `GRID RULE` comment above `<div class="ep-list">`). Drop the row with
   the lowest EP number and append a new entry for the latest episode: `ep-num`,
   `ep-ref-tag` (cultural reference), `ep-row-title`, `ep-row-quote`, and `href` pointing
   to the **live-verified** Spotify URL (see re-push caveat in Step 1 — never reuse a URL
   only "confirmed" pre-re-upload).
2. Redeploy from `btq-production/website/`: run `vercel --prod`.
3. **Git commit alone does NOT update the live site** — Vercel deploy is manual via CLI,
   not auto-deploy from git push. Confirmed in EP.016: the HTML had the correct grid in the
   commit, but the live site kept showing the stale grid until `vercel --prod` ran.
4. Verify live (run via Bash tool — uses `$(date +%s)` and `grep`, not available in
   native PowerShell 5.1):
   ```
   curl -s "https://behind-thequeue.com/?v=$(date +%s)" | grep -o "episode/[a-zA-Z0-9]*"
   ```
   PowerShell alternative:
   ```
   (Invoke-WebRequest -Uri "https://behind-thequeue.com/?v=$(Get-Random)").Content -split '"' | Select-String "episode/"
   ```
   Confirm the new episode's URL appears and matches the live-verified Spotify URL.

---

## Output summary

End with a compact status table:

| Asset | Status |
|-------|--------|
| Spotify SEO | Done |
| Social plan (4 days) | Done |
| YouTube metadata | Done |
| Cover-art prompts (3 formats) | Done |
| Git commit + push | Done / Failed (reason) |

---

## Brand constants (for reference)

| Element | Value |
|---------|-------|
| Background | Void Black `#0A0A0A` |
| Accent | Signal Gold `#C9A84C` |
| Off-white | `#F5F2EC` |
| Headline font | Playfair Display |
| Body | DM Sans |
| Accent | Bebas Neue |
| Headsets | Contact center boom mic — NEVER music headphones |
| Spotify category | Society & Culture |
| Primary language | Spanish |
