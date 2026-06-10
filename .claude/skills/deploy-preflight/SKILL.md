---
name: deploy-preflight
description: "Corre checks basicos antes de un deploy a Vercel (vercel build/vercel --prod) y desbloquea el hook deploy-preflight-gate.ps1 por 60 minutos. Usar antes de cualquier comando vercel que despliegue. Triggers ES: deploy preflight, valida el deploy, checks antes de deploy, desbloquear deploy, preflight de vercel. Triggers EN: deploy preflight, pre-deploy checks, unlock vercel deploy."
---

# Deploy Preflight

Valida que un deploy a Vercel desde este repo (monorepo con `.vercel/repo.json`) apunte
al directorio correcto antes de permitir `vercel build` / `vercel --prod`. Si todos los
checks pasan, crea el flag `C:\Users\andre\.claude\.preflight-passed` que desbloquea el
hook `deploy-preflight-gate.ps1` por 60 minutos.

## Workflow

Sigue `workflows/checks.md` (Pasos 1–7): identifica el proyecto, verifica
`.vercel/repo.json` y el directorio de deploy, confirma la baseline de produccion,
crea el flag de desbloqueo, resume, y — si el flujo incluye un `git push` a
main/master — corre el post-push check para detectar auto-deploys que rompan
produccion.
