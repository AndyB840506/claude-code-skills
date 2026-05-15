---
name: retrospective
description: "Analyze session to extract learnings, propose skill updates, ask for confirmation before applying. Detects corrections, redone work, missing steps, patterns that worked. Proposes specific diffs with user approval required. Triggers: retrospective, what did we learn, update skills, what did we improve, lessons learned, session review."
---

# Retrospective — Learn and Update Skills

Analyzes the current session to extract reusable learnings and proposes updates to skill files.

**Critical:** Always asks for explicit user approval before applying ANY changes to skill files.

---

## Quick Start

```
/retrospective
/retrospective skill-name
```

---

## How It Works

**5-Step Workflow:**

1. [Extract Signals](workflows/extract.md) — Identify learnings from this session
2. [Map to Skills](workflows/map.md) — Which skills need updating
3. [Propose Diffs](workflows/propose.md) — Show specific changes
4. [Ask Confirmation](workflows/confirm.md) — Wait for explicit approval
5. [Apply Changes](workflows/apply.md) — Update skills if approved

---

## When to Use

- After completing a multi-step workflow
- When you corrected my approach multiple times
- When something was redone 3+ times
- When you ask "what did we learn"
- After `/session-close` workflow

---

## See Also

- [What to Encode](docs/what-to-encode.md) — Process changes, anti-patterns, tool behavior
- [Auto-Suggest](docs/auto-suggest.md) — When to suggest retrospective vs when to skip

---

## EXECUTION

You have invoked `/retrospective`. Now perform the 5-step retrospective analysis.

### Step 1: Extract Signals

Scan the conversation transcript for these patterns:

**Corrections (highest priority):**
- User rejected output: "this isn't great", "remove this", "wrong"
- User redirected approach: "no, do it this way", "don't do that"
- User added context: "we have a skill for that", "follow the playbook"

**Redone Work:**
- Something generated, rejected, regenerated with different approach
- Multiple iterations on same artifact (3+ versions)
- Sub-agent output that had to be cleaned up

**Missing Steps:**
- Things improvised that aren't in workflows
- Steps that should've been in checklist but weren't
- Tools/scripts that existed but weren't referenced

**What Worked Well:**
- Patterns that produced good results first try
- New approaches that should become default
- Shortcuts that saved time

Format findings as a table:
```
| # | Learning | Type | Skill | Change |
|---|----------|------|-------|--------|
| 1 | Static docs don't execute | Correction | session-close | Add EXECUTION section |
| 2 | Skills need pattern guidance | Missing Step | skill-creator | Document EXECUTION requirement |
```

### Step 2: Map to Skills

For each learning, identify which skill(s) need updating. If learning applies to multiple skills, list each one.

### Step 3: Propose Diffs

For each proposed change, show:
- **What's changing:** Specific section or file
- **Why:** The learning that drove this
- **How:** The exact text change or new content

Example:
```
**Skill:** skill-management
**File:** workflows/audit.md
**Why:** We discovered that structure checks should happen before reorg
**Change:** 
- OLD: "Run reorganization immediately after audit"
+ NEW: "Audit first, ask user before reorganizing"
```

### Step 4: Ask Confirmation

Present all proposed changes and ask:

> **Apply these skill updates?**
> 
> This will modify X skill files with Y total changes.
> 
> [Show summary of what will change]
> 
> Continue? [yes/no]

Wait for user response.

### Step 5: Apply Changes (If Approved)

If user said YES:
- Update each skill file with proposed changes
- Show confirmation for each file updated
- Summarize total changes made

If user said NO:
- Discard all changes
- Return to main workflow

---

**Retrospective complete!** Learnings extracted and skills updated (if approved).
