---
name: deploy-preflight
description: "Corre checks basicos antes de un deploy a Vercel (vercel build/vercel --prod). Usar antes de cualquier comando vercel que despliegue. Triggers ES: deploy preflight, valida el deploy, checks antes de deploy, preflight de vercel. Triggers EN: deploy preflight, pre-deploy checks."
---

# Deploy Preflight

Valida que un deploy a Vercel desde este repo (monorepo con `.vercel/repo.json`) apunte
al directorio correcto antes de correr `vercel build` / `vercel --prod`.

## Workflow

Sigue `workflows/checks.md` (Pasos 1–6): identifica el proyecto, verifica
`.vercel/repo.json` y el directorio de deploy, confirma la baseline de produccion,
resume, y — si el flujo incluye un `git push` a main/master — corre el post-push
check para detectar auto-deploys que rompan produccion.
