# Real Examples

## Example 1: Document Analyzer Skill (200+ lines → organized)

Original flat structure: one huge SKILL.md with all procedures inline.

**Reorganized:**

```
.claude/skills/doc-analyzer/
├── SKILL.md (25 lines)
│   # Just: trigger phrases + 3-workflow list
│
├── workflows/
│   ├── summarize.md       # Extract key points from any doc
│   ├── audit.md           # Check for compliance issues
│   └── extract-data.md    # Pull structured data (tables, dates, etc)
│
├── scripts/
│   ├── parse-tables.py    # Convert HTML tables → CSV
│   └── split-by-section.py # Break doc into sections
│
├── templates/
│   └── audit-report.html  # HTML report template
│
└── docs/
    ├── formats-supported.md    # PDF, Word, Google Docs, etc
    └── troubleshooting.md      # What to do if extraction fails
```

**SKILL.md stays lean (25 lines):**

```markdown
---
name: doc-analyzer
description: "Analyze documents..."
---

# Doc Analyzer

Extract insights from any document.

## Workflows

1. **summarize** — Extract key points from any document type
2. **audit** — Check for compliance issues
3. **extract-data** — Pull structured data (tables, dates, etc.)

## See Also

- [Supported Formats](docs/formats-supported.md)
- [Troubleshooting](docs/troubleshooting.md)
```

**Each workflow is self-contained:**
- Open `workflows/summarize.md` → complete procedure
- User never feels lost jumping between files

---

## Example 2: Micro-Skill (Under 30 lines → No Structure Needed)

"Extract emails from text"

**Just one SKILL.md, no folders:**

```
.claude/skills/extract-emails/SKILL.md (20 lines)
# Minimal skill, no structure needed
```

When a skill is tiny, folder structure adds complexity, not clarity.

---

## Troubleshooting Skill Detection

**Problem:** Skill isn't showing in Claude Code's skills list.

**Most common cause:** Loose `.md` files mixed with folder-based skills.

```
.claude/skills/
├── my-skill.md           ❌ Loose file
├── my-skill/SKILL.md     ❌ Same skill as folder
└── other-skill/SKILL.md  ✓ Correct
```

Claude Code gets confused and may fail to detect ANY skills.

**Fix:**
1. Find loose `.md` files in `.claude/skills/`
2. For each loose file, create a folder and move inside as `SKILL.md`
3. Delete the original loose file
4. Commit to git

**Correct (always):**
```
.claude/skills/
├── skill-name-1/
│   └── SKILL.md     ✓ Always in a folder
├── skill-name-2/
│   └── SKILL.md     ✓ Folder with SKILL.md
```

After fixing, Claude Code auto-discovers. No restart needed.
