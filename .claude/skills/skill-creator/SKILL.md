---
name: skill-creator
description: "Create custom Claude Code skills from scratch. The skill that makes skills. Build your own automation, workflow, or command. Triggers EN: 'create a skill', 'I want a skill', 'custom skill', 'automate this as a skill', 'create a command', 'convert to a skill', 'make this automatic'. Triggers ES: crear skill, nueva skill, crear habilidad, quiero una skill, automatizar proceso, convertir en skill."
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

## Web Version

`skill-creator-web` — deploy independiente en DigitalOcean que permite crear skills desde cualquier browser o celular, sin necesidad de Claude Code ni terminal activa. El skill generado se hace push automáticamente a `AndyB840506/claude-skills` via GitHub API.

- URL local: `http://localhost:3001/?token=skillcreator_andyf_9p2m5x3k8`
- Stack: Express + Claude API (SSE streaming) + GitHub REST API v3
- Patrón clave: `PUSH_SKILL:{json}` → mismo que `SEND_QUOTE` en andyfreelancer
- Repo de skills: `https://github.com/AndyB840506/claude-skills`

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
