# Add a Model File

User typically downloads to `E:\Downloads` (browser default — NOT `C:\Users\andre\Downloads`) and pastes the path.

1. **Verify the file**: exists, size matches the source page (a truncated download loads garbage or errors).
2. **Move** (PowerShell `Move-Item -LiteralPath`) to the right folder under `E:\AI\models\`:

| File kind | Clue | Destination |
|---|---|---|
| Checkpoint (all-in-one, Civitai) | 2–7 GB single file | `checkpoints\` |
| Diffusion model (model-only) | workflow panel says `diffusion_models` | `diffusion_models\` |
| Text encoder | `text_encoders` / clip name | `text_encoders\` |
| VAE | ~100–350 MB, `ae`/`vae` in name | `vae\` |
| LoRA | 10–500 MB | `loras\` |

3. **Refresh**: existing mapped folder → user presses `R` in browser tab. New folder mapping added to `extra_model_paths.yaml` → server restart required (TaskStop + relaunch).
4. **Verify via API**: `curl -s http://127.0.0.1:8188/models/<folder>` must list the filename. Report done only after seeing it listed.
5. Remind user to re-select the file in the workflow's dropdown if it showed "undefined".

License rule: for anything going into a commercial project, the USER reads the model's license page (Civitai/HF) — don't assert license terms from memory.
