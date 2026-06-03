# Production Workflow

## Tools & Roles

| Tool | Role |
|---|---|
| Claude ("Laswell") | Structure, scripts, image prompts, strategy, consistency, copy |
| Gemini / Nani Banana 2 | Episode artwork, quote cards, music creation |
| Kling AI | Animating static artwork |
| Google Flow / Veo 2 | Image-to-video for TikTok |
| TurboScribe | Episode transcription |
| CapCut | Final video assembly |
| Gamma | LinkedIn carousels |
| Reaper | Recording DAW (SU9 USB mic, 48000Hz) |
| Spotify for Podcasters | Primary distribution |
| Safe Creative | Copyright registration per episode |

## Website Update — Episode Grid

The homepage grid always shows the **4 most recently published** episodes. Rule: oldest → newest, slot 1 = oldest, slot 4 = newest. Drop the oldest card each time a new episode publishes.

**Worked example:**
| Published | Slot 1 | Slot 2 | Slot 3 | Slot 4 |
|-----------|--------|--------|--------|--------|
| EP.011–014 (current) | EP.011 | EP.012 | EP.013 | EP.014 |
| EP.015 publishes | EP.012 | EP.013 | EP.014 | EP.015 |
| EP.016 publishes | EP.013 | EP.014 | EP.015 | EP.016 |

**To update:** edit `.claude/skills/btq-project/website/index.html` → find the `ep-grid` section → remove the top card, add the new episode at the bottom → `vercel --prod` from the `website/` folder.

---

## Workflow Order

1. Script planning and research (Claude)
2. Draft script generation (Claude)
3. Artwork prompts (Gemini/Nani Banana)
4. Final script review and approval (Andy)
5. Recording (Andy + Reaper)
6. Transcription (TurboScribe)
7. Artwork generation (Gemini/Nani Banana)
8. Video creation (Google Flow/Kling) — opcional
9. Social media assets (Gamma carousels)
10. Copyright registration (Safe Creative)
11. Publishing to Spotify and social channels
