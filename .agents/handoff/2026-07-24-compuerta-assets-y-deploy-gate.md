# Handoff: Compuerta de assets + deploy gate tangible + editorial retirada
**Date:** 2026-07-24 (viernes — par fecha/día verificado con Get-Date)
**Machine:** desktop (E:\)
**Status:** Builds #2 y #3 completos y probados contra defectos reales. Queda #1 (wave paralela) sin hacer.

> Continúa desde `2026-07-23-consolidacion-reglas-verificacion.md` (mismo hilo, cruzó
> medianoche). Aquel cubre la consolidación de reglas + skill `verify`; este cubre lo
> construido después.

---

## Qué se construyó

### 1 · Compuerta de assets de episodio (`scripts/verify_assets.py` + `banned-patterns.json`)
- **Etapa mecánica (script):** variantes presentes, dimensiones, aspect derivado (atrapa estiramiento), negro puro `#000000`, existencia de región de negro de marca, límites de caracteres. Exit 0/1, sin modo warnings.
- **Negro de marca POR SHOW** (un techo global reprobaba MPD/CCC): BTQ `#0A0A0A`→24, MPD `#1A1A1A`→40, CCC `#141414`→34. Flag `--show btq|mpd|ccc`.
- **Etapa 2 (lectura del modelo):** `banned-patterns.json`, 10 patrones backfilleados de 7 pipeline-audit BTQ + brand-constants. Los motivos visuales (anillos, typos, silueta plana) NO son detectables por script — el registry lo declara explícito.
- **Probado:** EP.022 real PASA (exit 0). Control sintético: 5/5 aserciones disparan por separado. **Control histórico:** la portada `(pre-pcb-fix backup)` PASA el script pero el stage 2 la REPRUEBA por patrón de circuito — eso prueba que las dos etapas hacen falta.

### 2 · Deploy gate del sitio (`scripts/verify_web.py` + hook)
- `verify_web.py <dir>`: og-image ≤500 KB, 1600×900, no negro puro; cada `<img>` con width lleva `height:auto` (por-imagen, NO grep global). Exit 0/1.
- **Hook `~/.claude/hooks/block-btq-deploy-unverified.ps1`** (PreToolUse Bash|PowerShell): corre el gate y **DENIEGA** un `vercel --prod` de BTQ si falla. Registrado en `~/.claude/settings.json` (3 hooks PreToolUse ahora).
- **Probado EN VIVO** (el hook ya estaba activo — el settings global carga en la sesión): deploy real BTQ → DENY por og-image de 2 MB; commit que menciona los términos → pasa; deploy de otro sitio → pasa.
- Cableado como paso en `episode-pipeline/workflows/05-deploy-verify.md`.

### 3 · Editorial og-image RETIRADA
- Decisión de Andy: la imagen editorial de marca (figura + surcos de vinilo) murió porque dependía de los aros vetados. `artwork-general-v3.md` marcado CONCEPTO MUERTO (registro histórico); su reemplazo será concepto nuevo, no corrección.

## Notes / Gotchas
- **El hook mordió su propio desarrollo:** detección inicial por substring bloqueó mi `git commit` (el mensaje decía "vercel" y "btq-production"). Arreglado: exige `vercel` en posición de comando con flag de deploy. **Al commitear algo que mencione el patrón, usar `git commit -F archivo`, no `-m`.**
- **Alcance fail-open a propósito:** un `vercel --prod` pelado desde el cwd del sitio (sin nombrar `btq-production`) NO se detecta — el hook no ve el cwd confiable. Se prefiere no bloquear kumatalent/andyfreelancer/MPD por error.
- **El gate solo enforza lo mecánico.** El typo horneado y los aros son lectura visual (stage 2), documentado.
- MPD/CCC en `verify_assets.py` tienen spec derivada de scripts/docs, **no probada contra assets reales** (no existe set completo). La primera corrida real puede necesitar ajustar la tolerancia.

## Next Steps
1. **Build #1 — capa de wave paralela en `episode-pipeline`** (único de los 3 builds sin hacer). NO un orquestador nuevo. A/B/E en paralelo; C+D secuenciales (una GPU). Dry-run sobre EP.022 sin escrituras. Decisiones cerradas en el handoff del 07-23.
2. **Reemplazar la og-image en vivo** — sigue con typo "PREMIUM KEY EDITOIAL", 2 MB, concepto muerto. Necesita GPU + concepto nuevo sin aros (decisión creativa de Andrés). El gate ya impide re-publicarla vía el path detectado.
3. **Producción parada:** BTQ EP.023 (guion listo, sin artwork, sin grabar); MPD EP.006 (guion listo, sin artwork/metadata/social).
4. **NEEDS USER INPUT (Andrés + Hugo) — heredado:** plan de fulfillment de HireSignal.
5. Opcional: cablear `verify_web.py` también a `deploy-preflight` para doble red (hoy solo lo corren el hook y el paso 05).
