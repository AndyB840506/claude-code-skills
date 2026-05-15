# Skill Storage & Organization

Skills are stored in the `.claude/skills/` directory. Each skill follows a standard self-contained folder pattern.

## Single-File Skills

Simple skills can be a single `.md` file:

```
.claude/skills/skill-name/SKILL.md
```

## Folder Structure (for larger skills)

For skills with multiple workflows or documentation:

```
.claude/skills/skill-name/
├── SKILL.md          # Router: triggers + quick links
├── workflows/        # Step-by-step procedures
│   ├── workflow1.md
│   └── workflow2.md
├── templates/        # HTML, email, doc templates
└── docs/            # Reference documentation
    ├── design-principles.md
    └── examples.md
```

## Rules

- **SKILL.md stays under 50 lines** — It's a router, not a manual. Link to workflows and docs for details.
- **Self-contained folders** — All templates, scripts, and docs live inside the skill folder
- **Easy to share** — The entire skill folder can be copied to another project and work immediately

## Example

```
.claude/skills/document-analyzer/
├── SKILL.md
├── workflows/
│   ├── extract-text.md
│   └── analyze-structure.md
├── templates/
│   └── report-template.html
└── docs/
    ├── supported-formats.md
    └── examples.md
```
