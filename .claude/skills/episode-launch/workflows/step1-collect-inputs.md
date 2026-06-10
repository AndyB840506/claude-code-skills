# Step 1 — Collect inputs

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
