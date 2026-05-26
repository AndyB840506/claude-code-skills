---
name: skill-creator
description: "Create custom Claude Code skills from scratch. The skill that makes skills. Build your own automation, workflow, or command. Triggers EN: 'create a skill', 'I want a skill', 'custom skill', 'automate this as a skill', 'create a command', 'convert to a skill', 'make this automatic'."
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
- [Design Principles](docs/design-principles.md) — 14+ principles of great skills

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

## Distinction from crear-skill

- **`/skill-creator`** — This skill. English instructions, for generic or globally shareable skills.
- **`/crear-skill`** — Spanish version, for use within this workspace.

---

## See Also

- [Storage & Organization](docs/storage.md) — Skill folder structure
- [EXECUTION Sections](docs/execution-sections.md) — How to make skills actually work

---

## EXECUTION

You have invoked `/skill-creator`. Now execute the creation flow:

1. **Understand** — Ask what process to automate (language, input, output, who uses it). See [Step 1](workflows/understand.md).
2. **Design** — Plan the skill structure (steps, outputs, triggers). See [Step 2](workflows/design.md).
3. **Write** — Generate the complete skill `.md` file. See [Steps 3-5](workflows/create-install.md).
4. **Confirm** — Show the generated skill and ask for approval before saving.
5. **Install** — Save to `.claude/skills/[name]/SKILL.md` upon approval.
6. **Test & Present** — Verify it works and summarize what was created. See [Steps 6-7](workflows/test-present.md).

**Result:** A ready-to-use skill file installed in the workspace.
