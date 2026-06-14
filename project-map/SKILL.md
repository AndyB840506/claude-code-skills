---
name: project-map
description: "Scans all repos in the base directory, reads their structure and key files, and generates a persistent project index saved to ~/.claude/project-map.md. Gives Claude full visibility of the workspace at the start of any session. Triggers: /project-map, /map, index repos, scan projects, update project map, what projects do I have."
---

# Project Map — Persistent Workspace Index

Scans all local repos and generates a structured context map. Saved to
`~/.claude/project-map.md` so Claude can load it at the start of any session without
re-exploring.

## What It Generates

For each repo:
- **Purpose** — what the project does (1 line)
- **Stack** — languages, frameworks, key dependencies
- **Entry points** — main files to read first
- **Status** — active / archived / in progress
- **Notes** — anything non-obvious from the code

## Workflow

Sigue `workflows/scan.md` — encuentra el base dir, escanea los directorios con `.git`,
genera `~/.claude/project-map.md` y confirma cuántos repos indexó. Incluye cómo cargar
el mapa al inicio de sesión. Re-correr al agregar o quitar repos.
