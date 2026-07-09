---
name: deploy-preflight
description: "Corre checks basicos antes de un deploy a produccion (Vercel, DO App Platform u otro host). Usar antes de cualquier vercel build/--prod o git push que publique. Triggers ES: deploy preflight, valida el deploy, checks antes de deploy, preflight de vercel, deploy a produccion. Triggers EN: deploy preflight, pre-deploy checks, production deploy check."
---

# Deploy Preflight

Valida destino, metodo de deploy y contenido antes de publicar: detecta el host
real de produccion (headers — no confiar en docs del repo, pueden estar stale) y
aplica el flujo que corresponda (Vercel prebuilt, DO deploy-on-push, etc.).

## Workflow

Sigue `workflows/checks.md` (Pasos 1–7): identifica el proyecto, verifica
`.vercel/repo.json` y el directorio de deploy, verifica que no haya secrets en
los archivos a deployar, confirma la baseline de produccion, resume, y — si el
flujo incluye un `git push` a main/master — corre el post-push check para
detectar auto-deploys que rompan produccion (mas el flujo prebuilt si el
proyecto usa `ignoreCommand`).
