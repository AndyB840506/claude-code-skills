---
name: skill-creator
description: "Create custom Claude Code skills from scratch. The skill that makes skills. Use this when you want to build your own skill, automate a workflow, make Claude repeat a process, create a custom command, or convert something manual into something automatic. Triggers: 'create a skill', 'I want a skill', 'custom skill', 'automate this as a skill', 'create a Claude Code command', 'convert this to a skill', 'make this automatic', 'skill for X'."
---

# Skill Creator — Build Your Own Skills

Describe a process you want to automate and I'll generate a complete, ready-to-use skill. It's the tool that builds tools.

Claude Code skills are `.md` files that teach Claude to do specific tasks. Any repetitive process can become a skill. Works in any language you prefer.

---

## Step 1 — Understand What You Need

Ask conversationally:

- **What language?** — Spanish or English
- **Where should this skill live?** — Business (private, company-only) or Other (public, shareable)
  - **Business:** Skills for internal projects, confidential or company-specific. Saved in `.claude/skills/business/` and never shared publicly.
  - **Other:** General-purpose skills that can be shared with other users. Saved in `.claude/skills/other/` and can be published to public repos.
- **What should Claude do automatically?** — describe the outcome you want
- **What information does it need?** — URL, text, folder, data, file...
- **What should it generate?** — HTML, report, file, code, dashboard...
- **Will you use this yourself or share with others?** (this can also help determine if it's business or other)

If you've already described enough (e.g., "a skill that reads a CSV of products and generates product cards in HTML"), I'll design directly.

If you're unsure what skill to build, here are ideas:

**For Business:**
- Commercial proposal generator (client data → professional PDF/HTML)
- Budget calculator (service + hours → detailed quote)
- Contract generator (data → customized contract)
- Sales presentation creator (product → HTML slides)
- Client onboarding (data → folder + emails + docs)

**For Marketing:**
- Ad copy generator (product + audience → ad variations)
- Content planner (niche → 30-day calendar with ideas)
- Sales email creator (product → email sequence)
- Social media post generator (topic → Instagram/LinkedIn/X posts)

**For Development:**
- API generator (data model → complete API)
- Code documenter (repository → documentation)
- Test generator (code → test suite)
- Project scaffolder (project type → complete structure)

**For Productivity:**
- Document summarizer (PDF → executive summary)
- Meeting transcriber (notes → formal minutes)
- SOP generator (process → step-by-step procedure doc)
- Data analyzer (CSV → dashboard with insights)

---

## Step 2 — Design the Skill

Before writing, plan the structure:

1. **Input** — what does the skill ask the user for?
2. **Process** — what steps does it follow (in order)?
3. **Tools** — what does it use? (WebFetch, Bash, Read, Write, native Claude Code tools)
4. **Output** — what does it generate and in what format?
5. **User experience** — how does it feel to use? (friendly messages, natural flow)

### Design Principles

These make a skill genuinely good:

**1. Never invent data** — if the skill needs info from the user, ask. Never make it up.

**2. Real data first, questions second** — if the skill can fetch data automatically, do it first. Only ask what you can't find alone.

**3. Auto-install dependencies** — if it needs tools, install them automatically.

**4. Creative freedom in design** — if generating HTML/dashboards, don't mandate rigid CSS. Describe the result and let Claude design.

**5. Adapt to context** — if the skill works for different types, adapt accordingly.

**6. Conversational flow** — skill should feel like natural conversation, not a form.

**7. Friendly fallbacks** — if something fails, offer alternative and move forward.

**8. Welcome message** — if the skill goes in a kit, include a welcome message.

**9. No suggested pricing** — don't include "as a service" or cost suggestions.

**10. Clear results** — show what was generated, what data was used, what's missing.

---

## Step 3 — Write the Skill

Generate the `.md` file with clear structure:

1. Frontmatter with `name` and `description`
2. Numbered sections with clear steps
3. Concrete examples
4. Explicit rules

---

## Step 4 — Install the Skill

After generating, install in the correct folder:

**If BUSINESS (private):**
```bash
mkdir -p .claude/skills/business
cp [skill-name].md .claude/skills/business/
```

**If OTHER (public):**
```bash
mkdir -p .claude/skills/other
cp [skill-name].md .claude/skills/other/
```

---

## Step 5 — Create Kit (if sharing)

If the skill will be used by others, generate a complete kit with CLAUDE.md and INSTRUCTIONS.md.

---

## Step 6 — Test

1. Simulate being a new user
2. Verify instructions are clear
3. If it generates files, verify they work
4. Adjust if something doesn't flow well

---

## Step 7 — Present to User

Show:
1. Filename and path
2. Trigger phrases
3. Input and output
4. Instructions for use
5. Ask if they want to adjust
