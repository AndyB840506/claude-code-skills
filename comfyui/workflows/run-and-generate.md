# Run and Generate (with verification)

1. **Check if server already up:** `curl -s http://127.0.0.1:8188/system_stats` — if it answers, skip launch.
2. **Launch** (background task): see launch command in `docs/stack-reference.md`. Wait for up with the curl retry pattern there.
3. **Confirm GPU:** `/system_stats` response must list `cuda:0 NVIDIA GeForce RTX 3080 Ti`.
4. **Queue:** POST API-format workflow JSON to `/prompt`. Minimal SDXL graph: CheckpointLoaderSimple → 2× CLIPTextEncode (pos/neg) → EmptyLatentImage → KSampler → VAEDecode → SaveImage(filename_prefix). Confirm response has empty `node_errors`.
5. **Poll** `GET /history/<prompt_id>` every ~5 s (PowerShell Start-Sleep loop; Bash foreground sleep is blocked). Done when body non-empty; require `status.status_str == "success"`.
6. **Verify by observation** (faja rule): file exists in `E:\AI\outputs\` AND Read the PNG to visually confirm it matches the prompt. Only then report done.
   - **For PIL-composited images** (programmatic text/footer/color blocks pasted next to or over AI-generated regions): a downscaled visual preview is NOT enough to catch small black-level mismatches (~8-10/255) between the AI's "pure black" and the brand's programmatic black constant — these are invisible at chat-preview resolution but visible in the full-res delivered file. Pixel-sample the seam boundaries with PIL (`img.getpixel(...)`) and confirm they match the brand black exactly, in addition to the visual check (bit 2026-07-15, BTQ EP.022 — the seam shipped past a visual review and was caught by the user, not by this check).

Notes:
- First generation after launch loads the checkpoint: 1–3 min is normal. Don't diagnose slowness before one full run.
- Test prompts from Claude are always SFW (landscape/portrait). Explicit content is user-side only.
- User-facing flow (browser UI) is documented in `E:\AI\manual.html` — point the user there instead of re-explaining.
