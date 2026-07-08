# Image → Prompt (WD14 Tagger + JoyCaption)

## JoyCaption (installed 2026-07-08 via Manager, user-clicked: ComfyUI-JoyCaption / AILab pack)
Natural-language captioner, uncensored, preferred over WD14 for sentence-prompt models (Z-Image). Node keys: `JC` (simple), `JC_adv`, `JC_ExtraOptions`, plus `ImageBatchPath` + `CaptionSaver` (folder batch-captioning — reuse for Stage 2 LoRA dataset prep). Settings for 12 GB (verified 2026-07-08): model **`joycaption-beta-one`** + quantization **`Maximum Savings (4-bit)`**, memory_management `Clear After Run`. prompt_style `Descriptive` (also has Danbooru/Rule34 tag modes — better fit for Z-Image, which obeys tags over prose). Wire: image → JC_adv → **slot 1 (STRING)** = caption; slot 0 (PROMPT) = instruction sent to the VLM (and where LOAD ERRORS appear as text — empty caption means read slot 0).

**TRAP:** `joycaption-beta-one-fp8` in the dropdown is really alpha-two FP8-Dynamic (JKCHSTR repo, mislabeled in jc_data.json) — compressed-tensors DECOMPRESSES it to bf16 at load (~18.6 GB) → OOM on 12 GB. Never use the fp8 option on this card.
**Local patches applied to JC.py (lost if node updates):** (1) SizeDict resize fix ~line 128; (2) unmasked error handler ~line 200 (`getattr(self,'model',None)`). `compressed-tensors` pip-installed. New pip packages need a server RESTART — transformers caches availability flags at import.
**ComfyUI cache gotcha:** identical re-runs replay cached outputs (history shows empty outputs) — nudge any input (e.g. temperature 0.60→0.61) to force re-execution when debugging.


Installed 2026-07-08 (user-approved clones): `custom_nodes/comfyui-manager` + `custom_nodes/ComfyUI-WD14-Tagger` (needs `onnxruntime` in the embedded python — already installed).

## Via API (Claude-driven)
1. Copy the image into `E:\AI\ComfyUI_windows_portable\ComfyUI\input\`.
2. Queue: `LoadImage` → `WD14Tagger|pysssss` (defaults: threshold 0.35, character_threshold 0.85; model `wd-eva02-large-tagger-v3` = best quality, auto-downloads on first use).
3. Tags come back in history: `outputs.<node_id>.tags` (list of strings). Verified working 2026-07-08.

## Via UI (user-driven)
Double-click canvas → search "WD14" → wire Load Image → WD14 Tagger → Run. Tags display on the node. Output can be wired straight into a prompt input for "more like this image".

## Full img2prompt+img2img pipeline (user's saved workflow, built 2026-07-08)
Load Image → Scale Image to Total Pixels (1.0 MP) → feeds BOTH: (a) WD14 Tagger (eva02-v3, thr 0.50, exclude `letterboxed, english_text`) and (b) VAE Encode (vae from Load VAE) → KSampler latent_image. Text: Tagger STRING → Concatenate string_a; Text String (Multiline) [user's style terms] → string_b; delimiter ", "; result → positive CLIP Text Encode text input. KSampler denoise = fidelity dial (0.5 close copy / 0.7 loose / 1.0 ignores reference). Z-Image turbo settings: steps 8, cfg 1.0, res_multistep/simple — do not "fix" these. Reference images must be cropped of UI/letterbox first. Saved in ComfyUI as workflow `img2prompt`.

## Notes
- Booru tags → directly usable on Illustrious/anime checkpoints. For Z-Image, convert tags into a sentence (Claude can do this from the tag list without seeing the image — works for any content).
- ComfyUI Manager is now installed: user can install future extensions from the UI (Manager button). Prefer high-install-count nodes — custom nodes are the ecosystem's malware vector.
- Claude must NOT clone new custom nodes without the user explicitly approving the specific repos (auto-mode guardrail fired 2026-07-08; correct flow = name repos, get approval, or user runs the commands).
