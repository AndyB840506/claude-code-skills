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

You have invoked `/skill-management`. Now audit and organize the skills.

### Step 1: Audit Folder Structure

Scan `.claude/skills/` directory and check each skill for:

**Structure Issues:**
- Missing SKILL.md file
- SKILL.md exceeds 50 lines (content should be in workflows/docs/)
- Missing workflows/ folder when workflows are referenced
- Missing docs/ folder when documentation is referenced
- Orphaned files outside expected structure
- Incorrect file naming (not kebab-case)

**Organization Issues:**
- Content scattered across files inconsistently
- No clear separation between router (SKILL.md) and procedures (workflows/)
- Templates/scripts not in dedicated folders
- Documentation in SKILL.md instead of docs/

**Routing Issues:**
- SKILL.md doesn't list all workflows
- Workflows reference files that don't exist
- Cross-skill links are broken

Identify each issue with:
- Skill name
- File path
- What's wrong
- Suggested fix

**Note:** If `.claude/skills/` folder doesn't exist, it will be created automatically.

### Step 2: Propose Reorganization

For each issue, propose a specific fix:

**Example Issue:**
```
Skill: my-skill
Problem: SKILL.md is 120 lines (exceeds 50)
Current: All content in SKILL.md
Proposed: Move detailed sections to workflows/ and docs/
```

**Example Fix:**
```
1. Create workflows/main.md with step-by-step process
2. Create docs/reference.md with reference material
3. Reduce SKILL.md to 40 lines as router
```

### Step 3: Ask Confirmation

Present all findings and ask:

> **Reorganize skills to standard pattern?**
>
> Found X organization issues in Y skills:
> - Z structure issues
> - Z routing issues
> - Z missing folders
>
> This will:
> - Create Z new folders
> - Move Z files
> - Update Z routing documents
>
> Continue? [yes/no]

Wait for user response.

### Step 4: Apply Changes (If Approved)

If user said YES:
- Create missing folders (workflows/, docs/, templates/, scripts/)
- Move files to proper locations
- Update SKILL.md routing if needed
- Rename files to kebab-case if needed
- Show each change as it's applied

If user said NO:
- No changes made
- Return to main workflow

### Step 5: Verify Structure

After changes (if approved):
- Scan again to confirm all issues resolved
- Report: "Structure verified ✓" or list remaining issues
- Summarize total changes made

---

**Skill management complete!** Structure audited and organized (if approved).
