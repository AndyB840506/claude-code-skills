---
name: skill-management
description: "Crea
te and organize skills properly. Build self-c
ontained skills with SKILL.md as a minimal ro
uter and separate workflow files for procedur
es. Everything related to a skill lives in on
e folder: templates, scripts, docs. Use when 
restructuring a skill, understanding skill ar
chitecture, or making a complex skill maintai
nable. Triggers: skill structure, organize sk
ill, skill architecture, skill folder, refact
or skill, skill maintenance."
---

# Skill Ma
nagement — Build Better Organized Skills

C
reate maintainable, portable skills using a s
elf-contained folder pattern. Keep SKILL.md m
inimal (under 50 lines) as a router, move wor
kflows and details to separate files.

## Qui
ck Start (30 seconds)

```
.claude/skills/my-
skill/
├── SKILL.md          # Router: 
trigger phrases + workflow list only
├─�
� workflows/
│   ├── workflow1.md  # 
Step-by-step procedure
│   └── workfl
ow2.md  # Another procedure
├── templat
es/        # HTML, email, docs templates
├�
��─ scripts/          # Python CLI tools
�
�── docs/             # Detailed referenc
e (on-demand)
```

**Rule:** If SKILL.md exce
eds 50 lines, move it to workflows/ or docs/.


---

## The Problem

Skills grow messy when
 you put everything in one file. SKILL.md bec
omes 500+ lines. Templates live in different 
folders. Scripts are scattered. Finding anyth
ing takes time.

## The Solution

**One folde
r per skill.** Everything related to a skill 
lives in one place:

```
.claude/skills/my-sk
ill/
├── SKILL.md          # Router + t
rigger phrases (minimal, <50 lines)
├──
 workflows/        # Step-by-step procedures

├── scripts/          # Helper tools (P
ython CLI)
├── templates/        # Temp
lates (live here, not elsewhere)
└── do
cs/             # Detailed reference (loaded 
on-demand)
```

---

## Step 1 — Understand
 the Pattern

**SKILL.md is a router, not a d
umping ground.**

Its only job: list what the
 skill does and which workflow to follow.

``
`markdown
---
name: my-skill
description: "Wh
at it does. Triggers: phrase1, phrase2, phras
e3."
---

# My Skill

One-liner description.


## Quick Start

1. Run `/my-skill workflow1`
 — [what this workflow does]
2. Run `/my-sk
ill workflow2` — [what this workflow does]

```

That's it. Everything else goes in `work
flows/`, `docs/`, or `scripts/`.

---

## Ste
p 2 — Organize by Purpose

**workflows/** �
�� step-by-step procedures the user will foll
ow
- One file per major workflow
- Named: `wo
rkflow1.md`, `workflow2.md`, etc.
- Contains:
 numbered steps, examples, decision trees

**
scripts/** — reusable helper tools
- Python
 CLI tools with argparse
- One script per too
l
- Auto-installable if skill needs them

**t
emplates/** — HTML, email, document templat
es
- Keep them *inside* the skill folder
- Ne
ver in a separate `.claude/templates/` direct
ory
- Named: `template-name.html`, `invoice.h
tml`, etc.

**docs/** — detailed reference 
material
- Loaded on-demand, not in the main 
flow
- Examples: API reference, advanced opti
ons, troubleshooting
- Keeps SKILL.md under 5
0 lines

---

## Step 3 — Keep SKILL.md Min
imal

Rule: **If a section in SKILL.md would 
be longer than 50 lines, move it to docs/ or 
workflows/.**

Good SKILL.md:
- Lists trigger
s clearly
- Links to workflows
- Explains con
text in 2-3 sentences
- Nothing more

Bad SKI
LL.md:
- Full procedure inline
- Dozens of ex
amples
- Detailed error handling
- Advanced o
ptions explained in detail

---

## Step 4 �
� Name Consistently

```
.claude/skills/my-sk
ill/
├── SKILL.md                    �
� Always "SKILL.md", never "my-skill.md"
├�
��─ workflows/
│   └── extract-data
.md         ← Descriptive names (not "workf
low1.md")
├── scripts/
│   └── 
validate-csv.py         ← Lowercase, hyphen
s, starts with verb
└── docs/
    └�
�─ edge-cases.md
```

**Rules:**
- Skill fo
lder name = frontmatter `name:` (both lowerca
se-with-hyphens)
- Main file: always `SKILL.m
d`
- Workflows: descriptive (`extract-data`, 
not `w1`)
- Scripts: verbs first (`validate-c
sv`, not `csv-validation`)

This makes skills
 self-documenting and easy to navigate.

---


## Step 5 — Make Skills Self-Contained

Ev
erything a skill needs lives in its folder:


✅ Templates inside: `.claude/skills/my-skil
l/templates/invoice.html`  
❌ Templates out
side: `.claude/templates/invoice.html`

✅ S
cripts inside: `.claude/skills/my-skill/scrip
ts/process.py`  
❌ Scripts outside: `.claud
e/scripts/process.py`

This makes skills port
able. You can share the entire folder and it 
works.

---

## Step 6 — Storage Strategy


Choose where to store based on reusability:


| Location | Use When | Availability |
|-----
-----|----------|--------------|
| `.claude/s
kills/my-skill/` | Specific to this project o
nly | This project only |
| `~/.claude/skills
/my-skill/` | Reusable across all projects | 
All projects, all repos |

**Example:**
- Pro
ject-specific: `.claude/skills/client-proposa
l-generator/` (only used in this client work)

- Vault-wide: `~/.claude/skills/doc-analyzer
/` (used in multiple projects)

**To share:**
 Include skill folder in project repo. Others
 clone it → Claude discovers it automatical
ly in that project's `.claude/skills/` folder
.

---

## Step 7 — Use Progressive Disclos
ure

Workflows reveal information as needed. 
Main workflow should handle 90% of cases. Exc
eptions and advanced options go in `docs/`.


**Bad flow:**
```
SKILL.md says: "For PDFs, u
se --ocr flag unless file is under 5MB and co
ntains searchable text. 
In that case, set OC
R_QUALITY=high. Note: OCR doesn't work with s
canned images from 2005-2009."
```
User is co
nfused before starting.

**Good flow:**
```
S
KILL.md: "1. Extract text from PDF"
→ workf
lows/extract.md: Simple extraction (handles 9
5% of cases)
→ docs/ocr-advanced.md: When O
CR is needed, settings, edge cases
```

User 
starts with the simple path. Advanced stuff i
s there if needed, not front-loaded.

---

##
 When to Skip This Pattern

Skip the folder s
tructure if:

- **Micro-skills:** Single-task
 skill (under 30 lines). Example: "Extract em
ails from text" — one SKILL.md file is enou
gh.
- **Context, not workflow:** Use `AGENTS.
md` for always-needed system context (like BT
Q project guidelines).
- **One-off prompts:**
 Use `/slash-commands` for quick user-trigger
ed templates.

**Use the folder pattern when:
**
- Skill has 2+ workflows
- Includes helper
 scripts or templates
- Needs detailed refere
nce docs
- Will be shared or reused across pr
ojects

---

## Troubleshooting: Skill Detect
ion Issues

**Problem: Skill isn't showing in
 Claude Code's available skills list**

**Mos
t common cause:** Loose `.md` files in `.clau
de/skills/` directory mixed with folder-based
 skills.

**Example of what breaks detection:
**
```
.claude/skills/
├── my-skill.md 
                   ❌ Loose file
├── m
y-skill/SKILL.md              ❌ Same skill 
as folder
└── other-skill/SKILL.md     
       ✓ Correct
```

Claude Code gets conf
used and may fail to detect ANY skills when t
his happens.

**Fix:**
1. Check `.claude/skil
ls/` for loose `.md` files
2. For each loose 
file, create a folder with that name
3. Move 
the `.md` file inside as `SKILL.md`
4. Delete
 the original loose `.md` file
5. Commit the 
change to git

**Correct structure (always):*
*
```
.claude/skills/
├── skill-name-1/

│   └── SKILL.md                   �
�� Always in a folder
├── skill-name-2/

│   └── SKILL.md                   �
�� Folder with SKILL.md
```

After fixing, Cl
aude Code auto-discovers skills. No restart n
eeded.

**Note the distinction:** that "no re
start" applies to *fixing a structural confli
ct* (e.g., removing a loose `.md` duplicate) 
in skills the session already knows about. Ad
ding a **brand-new** skill folder is differen
t — Claude Code loads the slash-command reg
istry at session start, so a freshly copied s
kill won't respond to `/skill-name` until you
 start a new session.

---

## Real Example: 
Document Analyzer Skill

This skill is 200+ l
ines if flat. With folder structure, it's org
anized:

```
.claude/skills/doc-analyzer/
├
── SKILL.md
│   # Just: trigger phrases
 + 3-workflow list
│   # 20 lines
│
├�
�─ workflows/
│   ├── summarize.md 
          # Extract key points from any doc
�
��   ├── audit.md               # Check
 for compliance issues  
│   └── extr
act-data.md        # Pull structured data (ta
bles, dates, etc)
│
├── scripts/
│ 
  ├── parse-tables.py        # Convert 
HTML tables → CSV
│   └── split-by-
section.py    # Break doc into sections
│
�
��── templates/
│   └── audit-rep
ort.html      # HTML report template
│
└�
��─ docs/
    ├── formats-supported.m
d   # PDF, Word, Google Docs, etc
    └─�
�� troubleshooting.md     # What to do if ext
raction fails
```

**SKILL.md stays lean (20 
lines):** "Run `summarize` to extract key poi
nts. Run `audit` to check compliance. Run `ex
tract-data` to pull structured information. S
ee docs/ for supported formats and troublesho
oting."

**Each workflow is self-contained:**
 Open `workflows/summarize.md` → complete p
rocedure. User never feels lost.

---

## Qui
ck Checklist for New Skills

### Before you w
rite SKILL.md:
- [ ] Identify all workflows (
usually 1-3)
- [ ] Plan what goes in each wor
kflow file
- [ ] List any templates needed
- 
[ ] Identify advanced options that go in docs
/

### SKILL.md checklist:
- [ ] Trigger phra
ses in description (at least 5)
- [ ] Workflo
w list (what the user can do)
- [ ] Under 50 
lines total
- [ ] Links to workflows/ if they
 exist

### Folder structure:
- [ ] `workflow
s/` — one file per major workflow
- [ ] `te
mplates/` — all templates live here (if any
)
- [ ] `docs/` — advanced/reference only (
if needed)
- [ ] `scripts/` — Python CLI to
ols (if useful)

### Test it:
- [ ] Open SKIL
L.md → understand what I can do in 10 secon
ds
- [ ] Open a workflow → complete procedu
re without jumping around
- [ ] Find a templa
te → it's in templates/ folder

If it passe
s these checks, you have a maintainable skill
.


