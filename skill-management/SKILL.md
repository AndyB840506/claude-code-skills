---
name: skill-management
description: "Create and organize skills properly. Build self-contained skills with SKILL.md as a minimal router and separate workflow files for procedures. Everything related to a skill lives in one folder: templates, scripts, docs. Use when restructuring a skill, understanding skill architecture, or making a complex skill maintainable. Triggers: skill structure, organize skill, skill architecture, skill folder, refactor skill, skill maintenance."
---

# Skill Management — Build Better Organized Skills

Create maintainable, portable skills using a self-contained folder pattern. Keep SKILL.md minimal (under 50 lines) as a router; move workflows and details to separate files.

## Folder Pattern

```
.claude/skills/my-skill/
├── SKILL.md       # Router: trigger phrases + workflow list only (<50 lines)
├── workflows/     # Step-by-step procedures, one file per workflow
├── scripts/       # Helper tools (Python CLI, etc.)
├── templates/     # Templates live here, not elsewhere
└── docs/          # Detailed reference, loaded on-demand
```

## Rules

- **SKILL.md is a router**, not a dumping ground — list what the skill does and which workflow to follow. If a section would exceed 50 lines, move it to `workflows/` or `docs/`.
- **Self-contained**: everything a skill needs lives in its own folder (templates, scripts, docs) — never in shared `.claude/templates/` or `.claude/scripts/`.
- **Naming**: folder name = frontmatter `name:` (lowercase-with-hyphens). Main file is always `SKILL.md`. Workflows use descriptive names (`extract-data.md`, not `w1.md`).
- **Storage**: project-specific skills go in `.claude/skills/`; reusable skills go in `~/.claude/skills/`.
  - In this repo (which *is* `~/.claude/skills/`): skills at the **repo root** (e.g. `session-close/`, `handoff/`) are global, available in every project. Skills under **`.claude/skills/`** (e.g. `crear-skill/`, `deploy-preflight/`) are project-specific to this skill-creator project only.
- **Skip the folder pattern** for micro-skills (<30 lines), always-needed context (use `AGENTS.md`/`CLAUDE.md`), or one-off prompts (use slash commands).
- **No speculative bolt-ons**: before adding a new step to an existing workflow skill, confirm it's regularly used. Unconfirmed "automatic" steps tend to drift out of sync with the rest of the skill and cause recurring inconsistency bugs.

## Skill Detection Issues

If skills aren't showing up: check `.claude/skills/` for loose `.md` files mixed with folder-based skills (e.g., `my-skill.md` alongside `my-skill/SKILL.md`). This confuses detection. Fix by moving each loose file into `<name>/SKILL.md` and deleting the original. New skill folders require a new session to register `/skill-name`.

## Checklist for New/Reviewed Skills

- [ ] Trigger phrases in description (at least 5)
- [ ] Workflow list — what the user can do
- [ ] SKILL.md under 50 lines total
- [ ] Links to `workflows/`/`docs/` if they exist
- [ ] `workflows/` — one file per major workflow
- [ ] `templates/` — all templates inside the skill folder
- [ ] `docs/` — advanced/reference material only, not front-loaded
- [ ] No loose `.md` files alongside folder-based skills
- [ ] No mid-word line breaks or garbled text (sign of a corrupted save)
- [ ] **Trigger overlap:** run `python skill-management/scripts/audit-triggers.py` from the kit root — 5 tests (exact, containment, near-duplicate, project-scope, missing trigger zone). Don't eyeball it: exact-match alone misses the worst case (a project-only skill claiming a generic phrase).

If a skill passes these checks, it's maintainable.
