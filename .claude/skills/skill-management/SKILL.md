---
name: skill-management
description: "Audit and reorganize skills properly. Scans for structure issues, suggests fixes, asks for confirmation before applying changes. Build self-contained skills with SKILL.md as minimal router and separate workflows/templates/docs. Triggers: skill structure, organize skill, skill architecture, skill folder, refactor skill, skill maintenance, organize skills, fix skill structure, audit skills."
---

# Skill Management — Audit, Organize, and Improve Skills

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

See [Audit Workflow](workflows/audit.md) for step-by-step instructions to audit and organize skills.
