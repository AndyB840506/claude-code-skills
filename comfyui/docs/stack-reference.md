# Stack Reference (installed 2026-07-08)

Two installs with identical layout — paths below use `E:\AI`; on the laptop substitute `D:\AI`.

## Hardware
- Desktop: NVIDIA RTX 3080 Ti, 12 GB VRAM (cuda:0). System RAM 32 GB. Stack at `E:\AI`.
- Laptop: NVIDIA RTX 3060 Laptop, 6 GB VRAM (cuda:0). System RAM 16 GB. Stack at `D:\AI` (full replica, 2026-07-08; SDXL smoke test passed — 1024², 12 steps).
- 12 GB fits SDXL fully; Z-Image bf16 (11.46 GB) partially offloads to RAM — first gen slow, rest OK. On the laptop (6 GB / 16 GB) offload is heavier: SDXL verified OK; Z-Image untested, expect it slow or OOM-prone.
- iGPU (AMD Radeon) also present on the desktop — ignore it; ComfyUI uses cuda:0.

## Layout
| Thing | Path |
|---|---|
| ComfyUI v0.27.0 portable (own Python) | `E:\AI\ComfyUI_windows_portable\` |
| Launcher (server + output dir arg) | `E:\AI\run_comfyui.bat` |
| Shared models root | `E:\AI\models\` (checkpoints, diffusion_models, text_encoders, vae, loras, embeddings, controlnet, upscale_models) |
| Path mapping config | `E:\AI\ComfyUI_windows_portable\ComfyUI\extra_model_paths.yaml` — read at startup only |
| Generated images | `E:\AI\outputs\` |
| Offline user manual | `E:\AI\manual.html` |
| Backup repo (workflows, configs, RESTORE.md, MODELS.md) | `C:\Users\andre\repos\comfyui-setup` — re-snapshot con `backup.ps1` + commit; GitHub privado del usuario, branch `master` (no `main`) |
| ComfyUI's internal models dir (also valid) | `E:\AI\ComfyUI_windows_portable\ComfyUI\models\` |

## Installed models (as of 2026-07-08)
- `checkpoints/sd_xl_base_1.0.safetensors` (6.94 GB) — SFW verification model
- `diffusion_models/z_image_turbo_bf16.safetensors` (11.46 GB) + `text_encoders/qwen_3_4b.safetensors` (7.49 GB) + `vae/ae.safetensors` (320 MB) — Z-Image Turbo set, natural-language prompts
- `upscale_models/RealESRGAN_x4plus_anime_6B.pth` (18 MB) — for the "Pulir" refine workflow
- No anime/Illustrious checkpoint yet — user must pick on Civitai and verify license himself (his rule).

## User's saved workflows (also in backup repo)
`Desde Cero` (txt2img puro) · `Pipeline Limpio` (referencia → JoyCaption + términos + img2img) · `Pulir` (upscale 4x anime → rebaja a 2 MP → 2ª pasada denoise 0.4) · más los 3 legacy (Best/Joy/My Workflow).

## API (server default http://127.0.0.1:8188)
- `GET /system_stats` — up-check + GPU/VRAM info
- `GET /models/<folder>` — list files server sees (e.g. `/models/checkpoints`, `/models/vae`) — use to VERIFY placement
- `POST /prompt` — queue API-format workflow JSON `{"prompt": {nodes...}}`; returns `prompt_id`, check `node_errors` is empty
- `GET /history/<prompt_id>` — empty `{}` until done; then `status.status_str == "success"`
- Wait-for-up pattern: `curl -s --retry 40 --retry-delay 3 --retry-connrefused --retry-all-errors http://127.0.0.1:8188/system_stats`

## Launch (headless, from Claude)
```powershell
Set-Location E:\AI\ComfyUI_windows_portable; .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --output-directory E:\AI\outputs
```
Run as background task. Stop with TaskStop on its task id (or user closes console window).

## Gotchas learned during install
- Git Bash `tar` is GNU tar — cannot extract .7z. Use Windows bsdtar: `& "$env:WINDIR\System32\tar.exe" -xf file.7z -C dest`.
- ComfyUI repo moved: use `api.github.com/repositories/589831718/releases/latest` with `-L` (old comfyanonymous URL 301s).
- WMI `AdapterRAM` caps at 4 GB — use `nvidia-smi --query-gpu=memory.total` for real VRAM.
- In-app "Download" button saves to ComfyUI internal folders, not `E:\AI\models` — both work, models just end up in two places.
