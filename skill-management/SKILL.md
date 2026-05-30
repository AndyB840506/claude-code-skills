---
name: skill-management
description: "Referencia de estructura y mejores prácticas para skills existentes. Usar cuando el usuario quiere gestionar, reorganizar o auditar skills — NO para crear una skill desde cero (usar crear-skill o 10-skill-creator). English triggers: manage skills, list skills, show skills, skill structure, skill best practices, skill format, skill naming, skill folder structure, skill guidelines, organize skills, skill architecture. Triggers ES: gestionar skills, administrar skills, ver mis skills, listar skills, estructura de skill, mantener skills, mejores prácticas de skills, formato de skill, estructura de carpetas skill, organizar skills, arquitectura de skill."
---

# Skill Management

Guide for creating and maintaining skills in your Claude Code project.

## When to Create a Skill

| Need | Solution |
|------|----------|
| Always-needed context | AGENTS.md |
| User triggers specific prompt | Slash command (`.claude/commands/`) |
| Repeated workflow with scripts/docs | **Skill** |
| Troubleshooting/reference docs | Skill with `docs/` folder |

**Create a skill when** (use table above to compare):

## Skill Structure (Self-Contained)

```
.claude/skills/my-skill/
├── SKILL.md              # routing + minimal docs
├── templates/            # templates INSIDE skill (self-contained)
│   └── my-template.md
├── workflows/            # step-by-step procedures
│   ├── create.md
│   └── publish.md
├── scripts/              # helper scripts
│   └── do-thing.py
└── docs/                 # detailed docs (on-demand)
    └── troubleshooting.md
```

**Key principle:** Skills are self-contained. Templates live inside the skill folder, not in a separate `.claude/templates/` folder. This way copying/moving a skill brings everything with it.

## SKILL.md Format

```markdown
---
name: my-skill
description: What it does. USE WHEN [trigger phrases].
---

# My Skill

## Quick Start
[Most common commands]

## Workflow Routing
- Creating X → `workflows/create.md`
- Publishing X → `workflows/publish.md`
```

**Key principle:** Workflows contain knowledge. SKILL.md stays minimal — just commands and routing table. Explain once in the workflow, encode it, never explain again.

Reference: [Daniel Miessler's PAI v2](https://danielmiessler.com/blog/personal-ai-infrastructure)

## Progressive Disclosure Pattern

**Problem:** Large skills bloat context, slow down agent.

**Solution:** Keep SKILL.md lean, put details in `docs/`.

| In SKILL.md (always loaded) | In docs/ (loaded on-demand) |
|-----------------------------|-----------------------------|
| Quick start commands | Full API reference |
| Common workflows | Edge cases |
| Brief troubleshooting pointers | Detailed troubleshooting |
| Script locations | Script implementation details |

**Example:**
```markdown
## Troubleshooting

### Audio Sync Issues
**Symptom:** Webcam drifts out of sync.
**Quick check:** `r_frame_rate=19200/1` = VFR problem.
**Full guide:** See [docs/vfr-sync-fix.md](docs/vfr-sync-fix.md)
```

**When to split to docs/:**
- Section is >50 lines
- Content is used <20% of the time
- Multiple sub-cases or variations
- Historical/example content

**Keep in SKILL.md when:**
- Used in >80% of skill invocations
- Required for basic operation
- Less than 10 lines

## Documentation at Scale (60K+ words)

**Problem:** Large documentation projects (>20 documents) become unnavigable.

**Solution:** Organize by topic, add master README, include visual structure guide.

**Structure for large projects:**
```
project-root/
├── README_DOCUMENTATION.md      # Master index + quick links
├── FOLDER_STRUCTURE.txt         # Visual structure reference
└── docs/
    ├── topic-a/                 # Organized by feature/phase
    ├── topic-b/
    └── topic-c/
```

**README_DOCUMENTATION.md contains:**
- Quick links (5-min reads by role)
- Navigation by use case ("I need to build X")
- Reading guides organized by role (CTO, Engineer, PM)
- Statistics (word count, document count)
- Decision tree ("What should I read?")

**FOLDER_STRUCTURE.txt contains:**
- Visual tree of all folders
- What each folder contains
- Quick pointers to key docs

**When to apply:**
- >20 documents across project
- Different audiences (engineers, managers, external partners)
- Multiple phases or products
- Documents updated frequently

**Example:** HireSignal project (60K words, 20 docs)
→ Organized into `docs/hiresignal/` + `docs/leracom/`
→ Master `README_DOCUMENTATION.md` with decision tree
→ `FOLDER_STRUCTURE.txt` for quick navigation

## Discovery Capture During Integration

**Problem:** Real discoveries (API endpoints, constraints, behavior) found during integration testing get lost or poorly documented.

**Solution:** When discoveries contradict assumptions, immediately:
1. Create a discovery document in `docs/discoveries.md`
2. Update affected design documents with real findings
3. Re-validate specs against reality

**Pattern:**
```
Discovery: "API endpoint X actually uses method Y, not Z"
→ Update: design document with discovered endpoint
→ Note: actual signature, parameters, behavior
→ Validation: update test cases to match real behavior
```

**Example:** Found `api_prod_studio_getsupervisor_ai__jit_plugin.updateBlueprint`
→ Created: `LERACOM_API_DISCOVERIES.md`
→ Updated: `LERACOM_MCP_DEVELOPER_BRIEF.md` with real endpoint
→ Validated: endpoint in spec matches reality

## Where to Store Skills

| Location | Purpose |
|----------|---------|
| `~/.claude/skills/` | Vault-specific |
| `~/projects/my-tools/skills/` | Shared/reusable (git repo) |

**Pattern:**
- Reusable → create in project repo, symlink to vault
- Vault-specific → create directly in `.claude/skills/`

```bash
# symlink shared skill into vault (Mac/Linux)
ln -s ~/projects/my-tools/skills/my-skill .claude/skills/my-skill
```

```powershell
# Windows (PowerShell — run as Administrator)
New-Item -ItemType SymbolicLink -Path .claude/skills/my-skill -Target ~/projects/my-tools/skills/my-skill
```

## Creating a New Skill

**Checklist before creating:**
- [ ] Check for collision with existing skills
- [ ] Check if workflow belongs in existing skill instead
- [ ] Check for existing template to reference (don't duplicate structure)

**Steps:**
1. **Choose location** (shared vs vault-specific)
2. **Create folder:** `skills/skill-name/`
3. **Create SKILL.md** with frontmatter
4. **Add workflows/** for procedures
5. **Add scripts/** if needed
6. **Symlink** if in shared repository

## Templates in Skills

**Pattern:** Templates live INSIDE the skill that uses them.

```
.claude/skills/review/
  templates/
    morning-checkin.md    ← Template here
    evening-checkin.md
  workflows/
    morning/main.md       ← Embeds: ![[.claude/skills/review/templates/morning-checkin.md]]
```

**Why:**
- Self-contained - skill folder has everything it needs
- Single source of truth - template defines structure
- Embeddable - workflows can embed templates for visual context

**Embedding templates in workflows:**
```markdown
### Questions (single source of truth)
![[.claude/skills/review/templates/morning-checkin.md]]
```

**For vault-wide templates** (not skill-specific), use `Templates/` folder.

## Workflow Structure

Workflows live in `workflows/` directory with clear names (no nested `main.md` files).

### Data Access Section

Every workflow that queries Bases needs a Data Access section at the top:

```markdown
## Data Access

**FIRST:** Read `.claude/skills/obsidian-cli/SKILL.md` to understand how to query Obsidian Bases.

The embeds below show what data to pull. Use the Obsidian CLI:

\`\`\`bash
obsidian base:query path="PATH" view="VIEW" format=json
\`\`\`
```

**Why:** Claude needs to know HOW to get the data, not just what data to get.

### Embeds vs CLI

| Pattern | Purpose | Example |
|---------|---------|---------|
| Embed `![[base#view]]` | Visual reference in Obsidian | `![[Goals.base#Every morning]]` |
| CLI query | Agent actually gets data | `obsidian base:query path="..." view="..." format=json` |

**Embeds are for humans** viewing the workflow in Obsidian.
**CLI is for Claude** executing the workflow.

### Referencing Other Skills

When a workflow depends on another skill, be explicit:

```markdown
## Data Access

**FIRST:** Read `.claude/skills/obsidian-cli/SKILL.md` to understand queries.

## Step 3: Update Tasks

**Use:** Add `- [ ]` items to session files or update task frontmatter via Obsidian CLI (`obsidian property:set`).
```

**Pattern:** "FIRST: Read [skill]" or "Use: [skill] for [operation]"

### Step Numbering

Use consistent numbering:

```markdown
## Step 0: Environment Setup / Prerequisites
## Step 1: Main Action
## Step 2: Next Action
```

- Step 0: Setup and prerequisites combined (optional)
- Steps 1+: Main workflow

Avoid fractional steps (Step 0.5, Step 1.5). If a prerequisite check
is needed before Step 1, include it at the end of Step 0 or as a
named section: `## Before you begin`.

## Naming Conventions

- **Skill name:** lowercase, hyphens, max 64 chars (e.g., `video-edit`)
- **Must match:** folder name = frontmatter `name`
- **Scripts:** `do-verb.py` or `verb-noun.py`
- **Workflows:** `workflow-name.md` (e.g., `create.md`, `publish.md`)
- **Docs:** `topic-name.md` (e.g., `vfr-sync-fix.md`)

## CLI Tools

**Always use Python for CLI tools. Never Bash.**

- Use `argparse` with subparsers for commands
- Follow the pattern in existing Python CLI skills
- Shebang: `#!/usr/bin/env python3`
- Make executable: `chmod +x script.py`

**Why not Bash:**
- Harder to maintain and debug
- String handling is error-prone
- No proper argument parsing
- Mixing Bash + embedded Python is ugly

## Description Best Practices

The `description` determines when agent loads the skill. Be specific:

**Good:**
```yaml
description: Automate video post-processing (recording → audio processing → upload prep). Use for editing recordings, audio processing, or publishing workflow.
```

**Bad:**
```yaml
description: Video stuff.
```

**Include trigger phrases in description:** "Use when user mentions X, Y, or Z"

> ⚠️ Triggers belong in the `description` field, NOT as a separate section in SKILL.md body. The description is what Claude uses to match user requests to skills.

## Analyzing Skills for Collisions

Check if skill descriptions overlap and might cause confusion.

**List all skills with descriptions:**
```bash
for skill in .claude/skills/*/SKILL.md; do
  [ -f "$skill" ] && echo "$(grep -m1 '^name:' "$skill" | cut -d: -f2): $(grep -m1 '^description:' "$skill" | cut -d: -f2-)"
done
```

**What to look for:**
- Similar trigger phrases across different skills
- Overlapping domains (e.g., two skills both handle "tasks")
- Vague descriptions that could match many requests
- Language-specific duplicates (e.g., `skill` vs `skill-en`)

**How to fix collisions:**
- Make descriptions more specific
- Add distinguishing trigger phrases
- Consider merging skills if they do the same thing
- **For multilingual collisions:** Merge into one skill with balanced bilingual trigger coverage (~50/50 Spanish/English) rather than separate `-en` variants

## Bilingual Skill Trigger Audit

**When collision detection reveals language-specific duplicates** (e.g., `prompt-reviewer` and `prompt-reviewer-en`), the solution is not separate skills but one unified skill with equal trigger coverage in both languages. This section provides the audit checklist to ensure that merge is done correctly.

**Pattern:** When a skill needs to work in multiple languages, ensure trigger phrase coverage is **balanced across languages**, not dominant in one.

**Red flag signs:**
- Skill has 15+ Spanish triggers but only 3 English triggers (or vice versa)
- Separate `-en` or `-es` skill variants exist for the same functionality
- English users report skill not activating while Spanish users can activate it

**Audit checklist before publishing:**
- [ ] Skill description includes 3-5 trigger phrases in each language
- [ ] Trigger distribution is roughly 50/50 (not 80/20 either direction)
- [ ] No separate language-specific variants exist (merge instead)
- [ ] Example triggers tested in actual conversation to confirm activation

**Test bilingual activation:**
Use PowerShell script to validate trigger detection:

```powershell
$skillPath = ".claude/skills/my-skill/SKILL.md"
$content = Get-Content $skillPath -Raw
if ($content -match "trigger phrase en español") { Write-Host "✓ Spanish trigger found" }
if ($content -match "trigger phrase in english") { Write-Host "✓ English trigger found" }
```

**Example output (should see both):**
```
✓ Spanish trigger found
✓ English trigger found
```

If only one language matches, the skill has imbalanced trigger coverage and should be rebalanced before deployment.
