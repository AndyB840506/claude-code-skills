# Best Practices Checklist

Use this before shipping a skill.

## Before Writing SKILL.md

- [ ] Identify all workflows (usually 1-3)
- [ ] Plan what goes in each workflow file
- [ ] List any templates needed
- [ ] Identify advanced options that go in docs/

## SKILL.md Checklist

- [ ] Trigger phrases in description (at least 5)
- [ ] Workflow list (what the user can do)
- [ ] Under 50 lines total
- [ ] Links to workflows/ if they exist

## Folder Structure

- [ ] `workflows/` — one file per major workflow
- [ ] `templates/` — all templates live here (if any)
- [ ] `docs/` — advanced/reference only (if needed)
- [ ] `scripts/` — Python CLI tools (if useful)

## Test It

- [ ] Open SKILL.md → understand what I can do in 10 seconds
- [ ] Open a workflow → complete procedure without jumping around
- [ ] Find a template → it's in templates/ folder

## Naming Conventions

- [ ] Folder name = frontmatter `name:` (both lowercase-with-hyphens)
- [ ] Main file: always `SKILL.md`
- [ ] Workflows: descriptive (`extract-data`, not `w1`)
- [ ] Scripts: verbs first (`validate-csv`, not `csv-validation`)
- [ ] Templates: descriptive (`invoice.html`, not `t1.html`)

## Self-Contained

- [ ] Templates inside skill folder, not in `.claude/templates/`
- [ ] Scripts inside skill folder, not in `.claude/scripts/`
- [ ] Everything needed to use the skill is in the folder

If it passes these checks, you have a maintainable skill.
