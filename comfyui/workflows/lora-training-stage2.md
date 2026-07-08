# Stage 2 — LoRA Training (PLANNED, not installed)

Approved plan from 2026-07-08 session, deferred until the user has character designs to lock in. Build only when asked.

1. Install **OneTrainer** (preferred over kohya_ss for UI simplicity), wired to `E:\AI\models`.
2. Dataset-prep script: resize/dedupe images + **WD14 tagger** for booru-tag captions. Script lives in `C:\Users\andre\repos` (rule: code in repos, binaries/models in E:\AI).
3. Verify with a small SFW test dataset: training run completes on 12 GB VRAM without OOM (SDXL LoRA needs gradient checkpointing + 8-bit optimizer at this VRAM).
4. Output LoRAs → `E:\AI\models\loras\`.

Context: purpose is consistent characters for the user's adult-game project (bootstrapping trick: train on cherry-picked generations of the same character). Claude's boundary: environment, scripts, configs, debugging runs — not curating/captioning/evaluating explicit datasets. Training data must be all-adult, no real-person likenesses.

Rental fallback if 12 GB proves too tight: RunPod/Vast.ai — but check provider ToS for NSFW workloads before recommending.
