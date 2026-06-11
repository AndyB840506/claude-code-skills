# Step 4a — SafeCreative Registration Metadata (on request, post-publish)

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

# Step 4b — Update website episode grid (post-publish, once Spotify URL is live-verified)

The site at `behind-thequeue.com` (Vercel project `website`) shows the 4 most recently
published episodes in its `<div class="ep-list">` grid, oldest→newest (slot 1 = oldest,
slot 4 = newest — drop the oldest each time a new episode publishes).

1. Edit `btq-production/website/index.html` — the grid keeps the 4 most recent episodes
   ordered oldest→newest by EP number (slot 1 = lowest EP number = oldest, slot 4 = highest
   = newest; see the `GRID RULE` comment above `<div class="ep-list">`). Drop the row with
   the lowest EP number and append a new entry for the latest episode: `ep-num`,
   `ep-ref-tag` (cultural reference), `ep-row-title`, `ep-row-quote`, and `href` pointing
   to the **live-verified** Spotify URL (see re-push caveat in step1-collect-inputs.md —
   never reuse a URL only "confirmed" pre-re-upload).
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
