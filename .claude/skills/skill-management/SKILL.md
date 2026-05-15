---
name: skill-management
description: "Audit and reorganize skills properly. Scans for structure issues, suggests fixes, asks for confirmation before applying changes. Build self-contained skills with SKILL.md as minimal router and separate workflows/templates/docs. Triggers: skill structure, organize skill, skill architecture, skill folder, refactor skill, skill maintenance, organize skills, fix skill structure, audit skills."
---

# Skill Management — Audit, Organize, and Improve Skills

Audits skill structure, proposes fixes, and asks for explicit confirmation before making changes. Create maintainable, portable skills using a self-contained folder pattern. Keep SKILL.md minimal (under 50 lines) as a router, move workflows and details to separate files.

**Critical Rule:** This skill ALWAYS asks for confirmation before reorganizing or modifying any skill folders. Changes only apply if user explicitly approves.

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

**Rule:** If SKILL.md exceeds 50 lines, move it to workflows/ or docs/.

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
- Named: `workflow1.md`, `workflow2.md`, etc.
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

## Step 4 — Verification & Confirmation

Before applying ANY changes:

1. **Scan the current state** — Show what needs fixing
2. **List proposed actions** — Be specific:
   ```
   Problemas encontrados:
   1. skill-x/SKILL.md es 65 líneas → Mover secciones a workflows/
   2. skill-y/templates/ → Mover a skill-y/templates/ (mejor organización)
   3. skill-z/scripts/ → Crear carpeta scripts/ (no existe)
   ```

3. **Ask for explicit confirmation:**
   ```
   ¿Quieres que haga esta reorganización?

   - "sí" / "yes" — Proceder con todos los cambios
   - "solo X" — Solo cambio específico #X
   - "no" / "skip" — No hacer nada
   ```

**CRITICAL:** Wait for user response. Do NOT proceed without approval.

### Step 5 — Name Consistently

```
.claude/skills/my-skill/
├── SKILL.md                    ← Always "SKILL.md", never "my-skill.md"
├── workflows/
│   └── extract-data.md         ← Descriptive names (not "workflow1.md")
├── scripts/
│   └── validate-csv.py         ← Lowercase, hyphens, starts with verb
└── docs/
    └── edge-cases.md
```

**Rules:**
- Skill folder name = frontmatter `name:` (both lowercase-with-hyphens)
- Main file: always `SKILL.md`
- Workflows: descriptive (`extract-data`, not `w1`)
- Scripts: verbs first (`validate-csv`, not `csv-validation`)

This makes skills self-documenting and easy to navigate.

---

## Step 5 — Make Skills Self-Contained

Everything a skill needs lives in its folder:

✅ Templates inside: `.claude/skills/my-skill/templates/invoice.html`  
❌ Templates outside: `.claude/templates/invoice.html`

✅ Scripts inside: `.claude/skills/my-skill/scripts/process.py`  
❌ Scripts outside: `.claude/scripts/process.py`

This makes skills portable. You can share the entire folder and it works.

---

## Step 6 — Storage Strategy

Choose where to store based on reusability:

| Location | Use When | Availability |
|----------|----------|--------------|
| `.claude/skills/my-skill/` | Specific to this project only | This project only |
| `~/.claude/skills/my-skill/` | Reusable across all projects | All projects, all repos |

**Example:**
- Project-specific: `.claude/skills/client-proposal-generator/` (only used in this client work)
- Vault-wide: `~/.claude/skills/doc-analyzer/` (used in multiple projects)

**To share:** Include skill folder in project repo. Others clone it → Claude discovers it automatically in that project's `.claude/skills/` folder.

---

## Step 7 — Use Progressive Disclosure

Workflows reveal information as needed. Main workflow should handle 90% of cases. Exceptions and advanced options go in `docs/`.

**Bad flow:**
```
SKILL.md says: "For PDFs, use --ocr flag unless file is under 5MB and contains searchable text. 
In that case, set OCR_QUALITY=high. Note: OCR doesn't work with scanned images from 2005-2009."
```
User is confused before starting.

**Good flow:**
```
SKILL.md: "1. Extract text from PDF"
→ workflows/extract.md: Simple extraction (handles 95% of cases)
→ docs/ocr-advanced.md: When OCR is needed, settings, edge cases
```

User starts with the simple path. Advanced stuff is there if needed, not front-loaded.

---

## When to Skip This Pattern

Skip the folder structure if:

- **Micro-skills:** Single-task skill (under 30 lines). Example: "Extract emails from text" — one SKILL.md file is enough.
- **Context, not workflow:** Use `AGENTS.md` for always-needed system context (like BTQ project guidelines).
- **One-off prompts:** Use `/slash-commands` for quick user-triggered templates.

**Use the folder pattern when:**
- Skill has 2+ workflows
- Includes helper scripts or templates
- Needs detailed reference docs
- Will be shared or reused across projects

---

## Troubleshooting: Skill Detection Issues

**Problem: Skill isn't showing in Claude Code's available skills list**

**Most common cause:** Loose `.md` files in `.claude/skills/` directory mixed with folder-based skills.

**Example of what breaks detection:**
```
.claude/skills/
├── my-skill.md                    ❌ Loose file
├── my-skill/SKILL.md              ❌ Same skill as folder
└── other-skill/SKILL.md            ✓ Correct
```

Claude Code gets confused and may fail to detect ANY skills when this happens.

**Fix:**
1. Check `.claude/skills/` for loose `.md` files
2. For each loose file, create a folder with that name
3. Move the `.md` file inside as `SKILL.md`
4. Delete the original loose `.md` file
5. Commit the change to git

**Correct structure (always):**
```
.claude/skills/
├── skill-name-1/
│   └── SKILL.md                   ✓ Always in a folder
├── skill-name-2/
│   └── SKILL.md                   ✓ Folder with SKILL.md
```

After fixing, Claude Code auto-discovers skills. No restart needed.

---

## Real Example: Document Analyzer Skill

This skill is 200+ lines if flat. With folder structure, it's organized:

```
.claude/skills/doc-analyzer/
├── SKILL.md
│   # Just: trigger phrases + 3-workflow list
│   # 20 lines
│
├── workflows/
│   ├── summarize.md           # Extract key points from any doc
│   ├── audit.md               # Check for compliance issues  
│   └── extract-data.md        # Pull structured data (tables, dates, etc)
│
├── scripts/
│   ├── parse-tables.py        # Convert HTML tables → CSV
│   └── split-by-section.py    # Break doc into sections
│
├── templates/
│   └── audit-report.html      # HTML report template
│
└── docs/
    ├── formats-supported.md   # PDF, Word, Google Docs, etc
    └── troubleshooting.md     # What to do if extraction fails
```

**SKILL.md stays lean (20 lines):** "Run `summarize` to extract key points. Run `audit` to check compliance. Run `extract-data` to pull structured information. See docs/ for supported formats and troubleshooting."

**Each workflow is self-contained:** Open `workflows/summarize.md` → complete procedure. User never feels lost.

---

## Quick Checklist for New Skills

### Before you write SKILL.md:
- [ ] Identify all workflows (usually 1-3)
- [ ] Plan what goes in each workflow file
- [ ] List any templates needed
- [ ] Identify advanced options that go in docs/

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
- [ ] Open SKILL.md → understand what I can do in 10 seconds
- [ ] Open a workflow → complete procedure without jumping around
- [ ] Find a template → it's in templates/ folder

If it passes these checks, you have a maintainable skill.
