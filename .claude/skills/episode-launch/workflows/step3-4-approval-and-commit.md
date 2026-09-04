# Step 3 — Approval gate

**Antes de presentar, correr el gate de puntuación** (regla completa en
`step2-generate-assets.md` § Puntuación): grepear rayas (`—`) y comillas angulares (`«»`)
dentro de cada bloque copiable — descripción de Spotify, los posts del plan social, la
descripción de YouTube y el artículo de LinkedIn (.md y .artifact.html) — y confirmar 0
matches antes de mostrarlos para aprobar. No cuenta el artículo del sitio (ver la nota de
excepción en `step2-generate-assets.md`) ni las notas/instrucciones internas del propio
archivo de assets. Mordió en EP.027 (2026-08-20): el texto se escribió primero y se verificó
después, y hubo que reescribir 13 fragmentos en 4 archivos ya presentados como listos.

After presenting all 4 asset blocks, ask:

> "Assets listos para EP.0XX. ¿Apruebas o ajustas algún bloque antes de hacer commit?"

Wait for explicit approval. If the user says "ajustar [bloque]" — revise only that block.
Once approved, proceed to Step 4.

---

# Step 4 — Git commit + push

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
git commit -m "feat(EP.0XX): launch assets — Spotify SEO, social plan, YouTube, portadas y quote cards

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

Confirm push output to user. If push fails (no remote / auth), report the error clearly
and do not retry destructively.
