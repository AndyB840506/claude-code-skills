---
name: skill-management
description: "Create and organize skills properly. Build self-contained skills with SKILL.md as a minimal router and separate workflow files for procedures. Everything related to a skill lives in one folder: templates, scripts, docs. Use when restructuring a skill, understanding skill architecture, or making a complex skill maintainable. Triggers: skill structure, organize skill, skill architecture, skill folder, refactor skill, skill maintenance, audit skills, skill kit audit."
---

# Skill Management — Build Better Organized Skills

Create maintainable, portable skills using a self-contained folder pattern. Keep SKILL.md minimal (under 50 lines) as a router, move workflows and details to separate files.

## Quick Start (30 seconds)

```
.claude/skills/my-skill/
├── SKILL.md          # Router: trigger phrases + workflow list only
├── workflows/
│   ├── workflow1.md  # Step-by-step procedure
│   └── workflow2.md  # Another procedure
├── templates/        # HTML, email, docs templates
├── scripts/          # Python CLI tools
└── docs/             # Detailed reference (on-demand)
```

**Rule:** If SKILL.md exceeds 50 lines, move content to workflows/ or docs/.

---

## The Problem

Skills grow messy when you put everything in one file. SKILL.md becomes 500+ lines. Templates live in different folders. Scripts are scattered. Finding anything takes time.

## The Solution

**One folder per skill.** Everything related to a skill lives in one place:

```
.claude/skills/my-skill/
├── SKILL.md          # Router + trigger phrases (minimal, <50 lines)
├── workflows/        # Step-by-step procedures
├── scripts/          # Helper tools (Python CLI)
├── templates/        # Templates (live here, not elsewhere)
└── docs/             # Detailed reference (loaded on-demand)
```

---

## Step 1 — Understand the Pattern

**SKILL.md is a router, not a dumping ground.**

Its only job: list what the skill does and which workflow to follow.

```markdown
---
name: my-skill
description: "What it does. Triggers: phrase1, phrase2, phrase3."
---

# My Skill

One-liner description.

## Quick Start

1. Run `/my-skill workflow1` — [what this workflow does]
2. Run `/my-skill workflow2` — [what this workflow does]
```

That's it. Everything else goes in `workflows/`, `docs/`, or `scripts/`.

---

## Step 2 — Organize by Purpose

**workflows/** — step-by-step procedures the user will follow
- One file per major workflow
- Named descriptively: `extract-data.md`, `audit.md`
- Contains: numbered steps, examples, decision trees

**scripts/** — reusable helper tools
- Python CLI tools with argparse
- One script per tool
- Auto-installable if skill needs them

**templates/** — HTML, email, document templates
- Keep them *inside* the skill folder
- Never in a separate `.claude/templates/` directory
- Named: `template-name.html`, `invoice.html`, etc.

**docs/** — detailed reference material
- Loaded on-demand, not in the main flow
- Examples: API reference, advanced options, troubleshooting
- Keeps SKILL.md under 50 lines

---

## Step 3 — Keep SKILL.md Minimal

Rule: **If a section in SKILL.md would be longer than 50 lines, move it to docs/ or workflows/.**

Good SKILL.md:
- Lists triggers clearly
- Links to workflows
- Explains context in 2-3 sentences
- Nothing more

Bad SKILL.md:
- Full procedure inline
- Dozens of examples
- Detailed error handling
- Advanced options explained in detail

---

## Step 4 — Name Consistently

```
.claude/skills/my-skill/
├── SKILL.md                       # Always "SKILL.md"
├── workflows/
│   └── extract-data.md            # Descriptive names
├── scripts/
│   └── validate-csv.py            # Lowercase, hyphens, verb-first
└── docs/
    └── edge-cases.md
```

**Rules:**
- Skill folder name = frontmatter `name:` (both lowercase-with-hyphens)
- Main file: always `SKILL.md`
- Workflows: descriptive (`extract-data`, not `w1`)
- Scripts: verbs first (`validate-csv`, not `csv-validation`)

---

## Step 5 — Make Skills Self-Contained

Everything a skill needs lives in its folder:

- Templates inside: `.claude/skills/my-skill/templates/invoice.html`
- Scripts inside: `.claude/skills/my-skill/scripts/process.py`

This makes skills portable. Share the entire folder and it works.

---

## Step 6 — Storage Strategy

| Location | Use When |
|----------|----------|
| `.claude/skills/my-skill/` | Specific to this project only |
| `~/.claude/skills/my-skill/` | Reusable across all projects |

---

## Step 7 — Use Progressive Disclosure

Workflows reveal information as needed. Main workflow handles 90% of cases. Exceptions go in `docs/`.

**Good flow:**
```
SKILL.md: "1. Extract text from PDF"
-> workflows/extract.md: Simple extraction (handles 95% of cases)
-> docs/ocr-advanced.md: When OCR is needed, settings, edge cases
```

User starts with the simple path. Advanced stuff is there if needed.

---

## When to Skip This Pattern

Skip the folder structure if:
- **Micro-skills:** Single-task skill under 30 lines
- **Context, not workflow:** Use `AGENTS.md` for always-needed system context
- **One-off prompts:** Use slash-commands for quick user-triggered templates

**Use the folder pattern when:**
- Skill has 2+ workflows
- Includes helper scripts or templates
- Needs detailed reference docs
- Will be shared or reused across projects

---

## Troubleshooting: Skill Detection Issues

**Problem: Skill not showing in available skills list**

Most common cause: loose `.md` files in `.claude/skills/` mixed with folder-based skills.

**Fix:**
1. Check `.claude/skills/` for loose `.md` files
2. For each loose file, create a folder with that name
3. Move the `.md` file inside as `SKILL.md`
4. Delete the original loose `.md` file

**Note:** Adding a brand-new skill folder requires a new session for Claude Code to discover it.

---

## Quick Checklist for New Skills

### SKILL.md checklist:
- [ ] Trigger phrases in description (at least 5)
- [ ] Workflow list (what the user can do)
- [ ] Under 50 lines total
- [ ] Links to workflows/ if they exist

### Folder structure:
- [ ] `workflows/` — one file per major workflow
- [ ] `templates/` — all templates live here (if any)
- [ ] `docs/` — advanced/reference only (if needed)
- [ ] `scripts/` — Python CLI tools (if useful)

### Test it:
- [ ] Open SKILL.md -> understand what I can do in 10 seconds
- [ ] Open a workflow -> complete procedure without jumping around
- [ ] Find a template -> it's in templates/ folder
