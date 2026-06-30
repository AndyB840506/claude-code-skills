---
name: deploy-to-vercel
description: "Deploy any project to Vercel via the right method for its current state — git-push, CLI link+deploy, or first-time setup. Adapted from Vercel's official agent skill. Triggers: deploy to vercel, vercel deploy, push this live, create a preview deployment, deploy my app, vercel preview."
---

# Deploy to Vercel

Detects whether a project is git-linked, CLI-linked, or neither, and uses the
right deploy method for that state. Always deploys as a **preview** unless the
user explicitly asks for production.

If deploying a project inside this skills workspace (BTQ/MPD/Lucca-Tech
monorepo), run `/deploy-preflight` first — it catches this repo's specific
directory-mapping and prebuilt-deploy pitfalls that this generic flow doesn't
know about. This skill handles the deploy mechanics; deploy-preflight handles
this repo's known gotchas.

## Workflow

Sigue `workflows/deploy.md` — revisa el estado del proyecto (git remote,
`.vercel/` link, CLI auth), elige el método correcto (git push / `vercel
deploy` / link primero / instalar+autenticar), ejecuta, y reporta la URL del
deployment.
