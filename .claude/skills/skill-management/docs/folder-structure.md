# Standard Folder Structure

Complete breakdown of the self-contained skill pattern.

## The Pattern

```
.claude/skills/my-skill/
├── SKILL.md          # Router: trigger phrases + workflow list (minimal, <50 lines)
├── workflows/        # Step-by-step procedures
│   ├── workflow1.md
│   └── workflow2.md
├── templates/        # HTML, email, docs
│   └── template.html
├── scripts/          # Helper tools (Python CLI)
│   └── helper.py
└── docs/             # Advanced reference (on-demand)
    └── advanced.md
```

## SKILL.md (Router, <50 lines)

Its only job: list what the skill does and which workflow to follow.

```markdown
---
name: my-skill
description: "What it does. Triggers: phrase1, phrase2, phrase3."
---

# My Skill

One-liner description.

## Workflows

1. **workflow1** — What this workflow does
2. **workflow2** — What this workflow does

## See Also

- [Advanced Guide](docs/advanced.md) — Edge cases, settings
```

That's it. Everything else goes elsewhere.

---

## workflows/ — Step-by-Step Procedures

One file per major workflow. Numbered steps, examples, decision trees.

**Naming:** `extract-data.md`, `validate-csv.md` (verbs first, descriptive)

**Content:**
- Numbered steps (1, 2, 3...)
- Examples for each step
- What to do if something fails
- When to use this workflow vs. another

---

## docs/ — Advanced Reference (On-Demand)

Loaded only when user needs it. Keeps SKILL.md lean.

**Files:**
- `advanced.md` — Advanced options, settings, fine-tuning
- `edge-cases.md` — Unusual scenarios and workarounds
- `api-reference.md` — Detailed API or tool reference
- `troubleshooting.md` — When something breaks

---

## templates/ — All Templates in One Place

**Rule:** Templates stay INSIDE the skill folder, never in `.claude/templates/`.

This makes skills portable — user can share the entire skill folder and it works.

**Naming:** `invoice.html`, `email-template.html`, `report.html`

---

## scripts/ — Helper Tools

Python CLI tools with argparse. One script per tool.

**Naming:** `validate-csv.py`, `process-data.py`

**Example:**
```python
#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Input file')
parser.add_argument('--output', help='Output file')
args = parser.parse_args()
```

Auto-installable if skill needs them. Install message: "Preparing tools, takes 30 seconds first time."

---

## Storage Location

Choose based on scope:

| Location | Use When | Shared |
|----------|----------|--------|
| `.claude/skills/my-skill/` | Only this project | No |
| `~/.claude/skills/my-skill/` | All projects | Yes |

To share a project-specific skill: Include folder in repo → others clone → Claude discovers automatically.

---

## Self-Contained Rule

Everything a skill needs lives in its folder.

✅ `my-skill/templates/invoice.html`  
❌ `.claude/templates/invoice.html`

✅ `my-skill/scripts/process.py`  
❌ `.claude/scripts/process.py`

This makes skills portable and easy to share.
