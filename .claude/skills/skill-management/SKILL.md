---
name: skill-management
description: "DEPRECADO — reemplazado por skill-kit-auditor. Triggers mantenidos para compatibilidad: skill structure, organize skill, skill architecture, skill folder, refactor skill, skill maintenance, organize skills, fix skill structure, audit skills."
---

# Skill Management — DEPRECADO

> ⚠️ **Esta skill está deprecada.** Fue reemplazada por `/skill-kit-auditor`, que hace lo mismo con criterios más completos (18 patrones), scope guards, y alerta de orden de ejecución.
>
> **Usa `/skill-kit-auditor` en su lugar.**

---

# Skill Management (original) — Audit, Organize, and Improve Skills

Audits skill structure, proposes fixes, and asks for explicit confirmation before making changes. Create maintainable, portable skills using a self-contained folder pattern. Keep SKILL.md minimal as a router, move workflows and details to separate files.

**Critical Rule:** This skill ALWAYS asks for confirmation before reorganizing or modifying any skill folders. Changes only apply if user explicitly approves.

---

## Quick Start

Run the audit workflow:

```
/skill-management audit
```

Or run individual workflows:

1. **audit** — Scan `.claude/skills/` and identify organization issues
2. **organize** — Propose reorganization of skills into folder structure
3. **verify** — Check after changes are applied

---

## The Pattern

Self-contained skills with folder structure:

```
.claude/skills/my-skill/
├── SKILL.md          # Router: triggers + workflow list (<50 lines)
├── workflows/        # Step-by-step procedures
├── templates/        # HTML, email, docs
├── scripts/          # Helper tools (Python)
└── docs/             # Advanced reference
```

**Rule:** If SKILL.md exceeds 50 lines, move content to workflows/ or docs/.

---

## Skills Are Self-Contained

✅ Templates inside: `.claude/skills/my-skill/templates/invoice.html`  
✅ Scripts inside: `.claude/skills/my-skill/scripts/process.py`  
✅ Everything in one folder → easy to share

---

## See Also

- [Standard Folder Pattern](docs/folder-structure.md) — Detailed breakdown
- [Real Examples](docs/examples.md) — Document analyzer skill walkthrough
- [Best Practices](docs/best-practices.md) — Quick checklist before shipping

---

## EXECUTION

You have invoked `/skill-management`. Now execute the audit and organize workflow:

1. **Audit Structure** — Scan `.claude/skills/` for organization issues, missing folders, oversized SKILL.md files
2. **Identify Issues** — Check each skill for: structure problems, routing issues, missing documentation folders
3. **Propose Fixes** — Generate specific reorganization steps for each issue
4. **Confirm & Apply** — Present findings and apply changes only if user approves
5. **Verify** — Scan again to confirm all issues are resolved

See [Full Workflow](workflows/audit.md) for detailed step-by-step instructions.

**Result:** Skills reorganized into standard pattern (if approved).
