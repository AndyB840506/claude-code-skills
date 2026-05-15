# Steps 3–5: Create, Confirm & Install

## Step 3 — Write the Skill

I generate the `.md` file with clear structure:

```markdown
---
name: name-in-kebab-case
description: "Description + 5+ trigger phrases"
---

# Skill Name

Welcome paragraph.

## Step 1 — [Collect Data]

Instructions for this step.

## Step 2 — [Process]

Main logic.

## Step 3 — [Generate Output]

What it creates and format.
```

Rules:
- Frontmatter: `name` (kebab-case) and `description` (5+ triggers)
- Numbered sections with clear steps
- Concrete examples
- Imperative language (do, ask, generate)

## Step 4 — Request Confirmation

CRITICAL: Before saving, I ask explicitly:

```
Do you want me to save this skill?

Skill: [skill-name]
Location: .claude/skills/[skill-name]/SKILL.md

- "yes" — Save the skill
- "no" — Don't save, I want to review
- "change X" — Change something first
```

**I wait for explicit response. No saving without approval.**

## Step 5 — Install

Once approved, I create the structure:

```bash
mkdir -p .claude/skills/skill-name
# Save content to SKILL.md
```

**Important rule:** Skills always go in a folder, never as loose files:

```
.claude/skills/
├── skill-name/
│   └── SKILL.md    ← Always this way
```

For larger skills, use folder structure:

```
.claude/skills/skill-name/
├── SKILL.md        (router <50 lines)
├── workflows/      (procedures)
└── docs/           (references)
```

Result: Skill is ready to use automatically.
