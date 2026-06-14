# Execution

When `/project-map` is invoked:

## Step 1 — Find base directory
Check `~/.claude/` for `settings.json` or `local-settings.json` to find the base directory.
Default: `$env:USERPROFILE\repos`

## Step 2 — Scan repos
List all directories in the base dir that contain a `.git` folder.
For each repo, read (in order, stop when you have enough):
1. `CLAUDE.md` — project instructions
2. `README.md` — project description
3. `package.json` / `composer.json` / `pyproject.toml` — stack info
4. Top-level file list — entry points

Use parallel agents to scan multiple repos simultaneously (see `/parallel-workflow`).
Skip `node_modules`, `vendor`, `.git` directories.

## Step 3 — Generate map
Build `~/.claude/project-map.md` with this structure:

```markdown
# Project Map
Generated: YYYY-MM-DD

## [repo-name]
**Purpose:** one-line description
**Stack:** list of tech
**Entry points:** key files
**Status:** active | archived | in-progress
**Notes:** anything non-obvious
---
```

## Step 4 — Save and confirm
Write to `~/.claude/project-map.md`.
Report: how many repos indexed, path saved to.
The file is automatically synced to GitHub on the next bootstrap sync (sync.ps1) — no
manual action needed.

---

## Loading the map

At the start of any session, Claude can read `~/.claude/project-map.md` to get instant
context on all projects — no exploration needed. Add to your `CLAUDE.md`:
```
At session start, read ~/.claude/project-map.md for workspace context.
```

Re-run `/project-map` whenever you add or remove repos.
