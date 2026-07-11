---
name: comfyui
description: Operate the local image-generation stack (ComfyUI v0.27.0) — E:\AI on the desktop (RTX 3080 Ti 12GB) and D:\AI on the laptop (RTX 3060 6GB) — launch the server, generate/verify via API, place downloaded models in the right folders, troubleshoot, and plan Stage 2 LoRA training. Triggers - comfyui, generate image, image generation, stable diffusion, sdxl, z-image, hidream, chroma, bigasp, noobai, illustrious, civitai, huggingface model, add model, place model, lora training, generar imagen, imagen local, modelo de imagen, E:\AI, D:\AI.
---

# ComfyUI — Local Image Generation Stack

Local, GPU-based image generation. Two installs, same layout: `E:\AI` on the desktop (built 2026-07-08) and `D:\AI` on the laptop (built 2026-07-08, full replica). Identify the machine first (`Get-PSDrive` — E: exists = desktop) and substitute the AI root accordingly; docs use `E:\AI` as the canonical example.
User manual: `<root>\manual.html` (offline copy) or https://claude.ai/code/artifact/79d37f6d-8fae-430f-a5fc-95cd287c61ba

## Workflows

| Task | File |
|---|---|
| Launch server + generate + verify via API | `workflows/run-and-generate.md` |
| Place a downloaded model file correctly | `workflows/add-model.md` |
| Image → prompt tags (WD14 tagger, installed) | `workflows/image-to-prompt.md` |
| Stage 2: LoRA training (planned, not built) | `workflows/lora-training-stage2.md` |

## Reference

- Paths, hardware, installed models, API endpoints: `docs/stack-reference.md`
- Known failures and fixes: `docs/troubleshooting.md`
- Prompt structure per model family + iteration method: `docs/prompting.md`

## Hard rules

- Models and outputs live in `<AI root>\models` / `<AI root>\outputs` (shared via `extra_model_paths.yaml`) — never in `~/.claude/` or repos. AI root = `E:\AI` desktop, `D:\AI` laptop.
- `extra_model_paths.yaml` loads at server startup; adding a *new folder mapping* needs a restart. New *files* in already-mapped folders only need `R` in the browser tab.
- Verify generations by observing output (API history status + file in `<AI root>\outputs`), never by "it should work".
- Content boundaries (user's adult-game project): Claude handles tooling/environment/scripts only — not curation, captioning, or evaluation of explicit content. All game characters must be unambiguously adult; no real-person likenesses; user personally verifies model licenses on Civitai before commercial use.
- Prompt style differs by model family: Z-Image/Qwen → natural-language sentences; Illustrious/SDXL-anime → booru tags.
- **Debugging order:** if output quality mysteriously degrades, FIRST verify every stage emits real content (PreviewAny node on text outputs; PNG-metadata inspection of executed graph) — only THEN tune parameters. Lesson: 2026-07-08, hours tuning "censorship" while the captioner silently returned empty strings on a swallowed load error.
- **Graph changes:** prefer authoring/fixing the workflow .json file (validate JSON, user opens it, eyeballs ~5 key values) over guiding manual canvas wiring via screenshots — the latter proved fragile (lost wires, reverted values); the former worked first-try 3×.
