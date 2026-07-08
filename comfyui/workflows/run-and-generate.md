# Run and Generate (with verification)

1. **Check if server already up:** `curl -s http://127.0.0.1:8188/system_stats` — if it answers, skip launch.
2. **Launch** (background task): see launch command in `docs/stack-reference.md`. Wait for up with the curl retry pattern there.
3. **Confirm GPU:** `/system_stats` response must list `cuda:0 NVIDIA GeForce RTX 3080 Ti`.
4. **Queue:** POST API-format workflow JSON to `/prompt`. Minimal SDXL graph: CheckpointLoaderSimple → 2× CLIPTextEncode (pos/neg) → EmptyLatentImage → KSampler → VAEDecode → SaveImage(filename_prefix). Confirm response has empty `node_errors`.
5. **Poll** `GET /history/<prompt_id>` every ~5 s (PowerShell Start-Sleep loop; Bash foreground sleep is blocked). Done when body non-empty; require `status.status_str == "success"`.
6. **Verify by observation** (faja rule): file exists in `E:\AI\outputs\` AND Read the PNG to visually confirm it matches the prompt. Only then report done.

Notes:
- First generation after launch loads the checkpoint: 1–3 min is normal. Don't diagnose slowness before one full run.
- Test prompts from Claude are always SFW (landscape/portrait). Explicit content is user-side only.
- User-facing flow (browser UI) is documented in `E:\AI\manual.html` — point the user there instead of re-explaining.
