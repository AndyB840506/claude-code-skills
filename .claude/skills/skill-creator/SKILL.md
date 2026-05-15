---
name: skill-creator
description: "Create custom Claude Code skills from scratch. The skill that makes skills. Build your own automation, workflow, or command. Triggers: 'create a skill', 'I want a skill', 'custom skill', 'automate this as a skill', 'create a command', 'convert to a skill', 'make this automatic'."
---

# Skill Creator — Build Your Own Skills

Describe a process you want to automate and I'll generate a complete, ready-to-use skill. It's the tool that builds tools.

Claude Code skills are `.md` files that teach Claude to do specific tasks. Any repetitive process can become a skill.

---

## 7-Step Creation Flow

1. **Understand** — What do you want to automate?
2. **Design** — Plan input, process, output
3. **Write** — Generate the skill `.md`
4. **Confirm** — Approve before saving
5. **Install** — Skill goes into `.claude/skills/`
6. **Test** — Verify it works
7. **Present** — Summary of what was created

---

## Quick Links

- [Step 1: Understand](workflows/understand.md) — What you need
- [Step 2: Design](workflows/design.md) — Skill structure
- [Steps 3-5: Create & Install](workflows/create-install.md) — Generate and save
- [Steps 6-7: Test & Present](workflows/test-present.md) — Verify and show
- [Design Principles](docs/design-principles.md) — 13 principles of great skills

---

## Example

```
/skill-creator

"I want a skill that reads a CSV of products 
and generates product cards in HTML"

↓

I generate the complete skill → ask approval → 
install it → ready to use
```

---

## Storage

All skills go in:
```
.claude/skills/skill-name/SKILL.md
```

For larger skills, use folder structure:
```
.claude/skills/skill-name/
├── SKILL.md (router)
├── workflows/ (procedures)
└── docs/ (references)
```

---

## Critical: EXECUTION Sections

For your skill to actually *execute* (not just display documentation), SKILL.md must include an `## EXECUTION` section with explicit instructions.

**Without EXECUTION:** Skill shows documentation but doesn't trigger action  
**With EXECUTION:** Skill actually performs the process when invoked

### Template

```markdown
## EXECUTION

You have invoked `/your-skill`. Now perform the process:

### Step 1: [First action]
[What to do, what to look for]

### Step 2: [Second action]
[What to do, what to look for]

[Continue for all steps...]

---

**Process complete!** [Summary of what was accomplished]
```

### Example (from real skill: retrospective)

```markdown
## EXECUTION

You have invoked `/retrospective`. Now perform the analysis:

### Step 1: Extract Signals
Scan conversation for: corrections, redone work, missing steps, what worked well

### Step 2: Map to Skills
Identify which skills need updating

### Step 3: Propose Changes
Show specific diffs

### Step 4: Ask Confirmation
Wait for user approval

### Step 5: Apply Changes
Update files if approved

---

**Retrospective complete!**
```

**Include EXECUTION sections in every skill you generate.** This is what makes skills actually work.
