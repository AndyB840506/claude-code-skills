# Workflow: Audit Skills

Scan `.claude/skills/` and identify organization issues. Proposes fixes for SKILL.md files that exceed 50 lines or lack folder structure.

## Step 1 — Scan Current State

Check every skill folder:
1. Count lines in each `SKILL.md`
2. Check for loose `.md` files (should not exist)
3. Check for workflows/, templates/, docs/, scripts/ folders
4. Note which skills are under/over 50 lines

## Step 2 — List Issues Found

Present as a table with:
- Skill name
- Line count
- Problems found (exceeds 50 lines, no folder structure, missing sub-folders)

**Example:**
```
| Skill | Lines | Problem |
|-------|-------|---------|
| my-skill | 156 | Exceeds 50x; no workflows/ |
| other-skill | 28 | ✓ Under 50, no structure needed |
```

## Step 3 — Propose Reorganization

For skills over 50 lines, specify:
- Which sections → `workflows/`
- Which sections → `docs/`
- Which sections → `templates/` (if any)

## Step 4 — Ask for Confirmation

**CRITICAL:** Before making changes, ask explicitly:

```
¿Quieres que haga esta reorganización?

Cambios propuestos:
1. skill-name — Move X to workflows/, Y to docs/
2. other-skill — Move Z to docs/

Responde:
- "sí" / "yes" — Proceder con todos los cambios
- "solo X" — Solo cambio específico #X
- "no" / "skip" — No aplicar nada
```

**Wait for explicit user confirmation.** Do NOT proceed without approval.

## Step 5 — Execute (if approved)

After user approves:
1. Create folder structure for each skill
2. Split SKILL.md into router + workflow files
3. Move detailed content to workflows/, docs/, templates/
4. Update SKILL.md to reference new files
5. Verify all folders created correctly
6. Commit changes to git

---

## When NOT to Reorganize

Skip folder structure if skill is:
- **Micro-skill:** Under 30 lines (single task only)
- **Context, not workflow:** Use AGENTS.md instead
- **One-off template:** Use `/slash-commands` instead

Only reorganize when:
- 2+ workflows, OR
- Includes templates/scripts, OR
- Needs advanced reference docs, OR
- Will be shared across projects
