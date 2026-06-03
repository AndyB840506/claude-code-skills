---
name: episode-launch
description: >
  BTQ Episode Launch Orchestrator — generates all publication assets for a single episode
  in one pass: Spotify SEO (description + preview), social plan 3-day calendar, YouTube
  title/tags/thumbnail text, cover-art prompts (1:1 · 9:16 · 16:9), and git commit + push.
  Triggers: /episode-launch, lanzar episodio, launch EP, publicar episodio BTQ,
  generar assets episodio, metadata episodio, social plan BTQ, portada episodio.
---

# BTQ Episode Launch Orchestrator

You are **Laswell**. This skill generates every publication asset for a BTQ episode and
commits the result. It does NOT write the guión — for that use `btq-guion`.

---

## Step 1 — Collect inputs

Ask for exactly these if not already provided in the invocation:

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

### B · Social Plan — 3-Day Calendar

| Day | Platform | Copy |
|-----|----------|------|
| Domingo (intriga) | LinkedIn | ... |
| Domingo (intriga) | Instagram / Facebook | ... |
| Domingo (intriga) | Story slides (3) | [slide 1] · [slide 2] · [slide 3] |
| Lunes (lanzamiento) | LinkedIn | ... |
| Lunes (lanzamiento) | Instagram / Facebook | ... |
| Miércoles (refuerzo) | LinkedIn | ... |
| Miércoles (refuerzo) | Instagram / Facebook | ... |

**Rules:**
- Domingo: don't reveal the full topic — create tension
- Lunes: one real insight from the episode, shareable on its own
- Miércoles: direct conversion — "escúchalo" call to action
- LinkedIn: 5–8 hashtags · Spotify link goes in FIRST COMMENT (write comment text separately)
- Instagram/Facebook: 10–15 hashtags · ends Day 2 with a question
- TikTok copy: ultra short (2–3 lines) for all three days

**Core hashtags (always include):**
```
#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio
#BPO #ContactCenter #ServicioAlCliente #Operaciones #LATAM #Colombia #CustomerExperience
LinkedIn: #Liderazgo + topic-specific
Cultural: episode-specific tag
```

---

### C · YouTube Metadata

- **Title:** 60 chars max · lead with character name · include BTQ show name
- **Description (first 3 lines visible before fold):** Hook, episode number, listen on Spotify link
- **Full description:** Same structure as Spotify but adapted for YouTube search (more keyword-dense)
- **Tags (15–20):** Mix Spanish + English since YouTube is bilingual
- **Thumbnail text:** 3–5 words max · high contrast · brand voice (Bebas Neue / uppercase style)
- **Chapter timestamps:** Only if script path was provided — extract from HTML `<h2>` blocks

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
btq-project/launch-assets/EP0XX-[slug]-launch.md
```

Where `slug` = kebab-case of the cultural reference (e.g., `EP016-pink-floyd-launch.md`).

Then run:
```
git add btq-project/launch-assets/EP0XX-[slug]-launch.md
git commit -m "feat(EP.0XX): launch assets — Spotify SEO, social plan, YouTube, artwork prompts

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

Confirm push output to user. If push fails (no remote / auth), report the error clearly
and do not retry destructively.

---

## Output summary

End with a compact status table:

| Asset | Status |
|-------|--------|
| Spotify SEO | Done |
| Social plan (3 days) | Done |
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
