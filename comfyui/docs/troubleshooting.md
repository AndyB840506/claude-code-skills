# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Connection refused on :8188 | Server not running | Launch per `stack-reference.md`; wait with curl retry pattern |
| "Missing Models (N)" panel in UI | Workflow needs files not present | Download each, place per `add-model.md`, press `R`, re-select in dropdowns (may show "undefined") |
| New model not in dropdown | Not refreshed / wrong folder / yaml mapping added after startup | `R` first → check folder vs table → restart server |
| CUDA out of memory | 12 GB card + big model + other GPU apps | Close games/video apps; lower resolution; switch to fp8 variant of the model |
| Every generation slow (not just first) | Model spilling to system RAM | Same as OOM: smaller/fp8 model variant |
| First generation slow (1–3 min) | Checkpoint loading — NORMAL | No action; don't diagnose before one full run completes |
| c10.dll error at startup | Missing VC redist | https://aka.ms/vc14/vc_redist.x64.exe |
| `tar: This does not look like a tar archive` on .7z | Git Bash GNU tar | Use `& "$env:WINDIR\System32\tar.exe" -xf` (bsdtar) |
| Downloaded file "missing" | It's in `E:\Downloads`, not the user profile Downloads | Check `E:\Downloads` first |
| Bad/garbled generations from anime checkpoint | Natural-language prompt on booru-tag model | Rewrite as comma-separated tags (`1girl, ...`) |
| JSON parse errors from API | BOM or empty response | Global rule: check BOM + empty body specifically |
