---
name: handoff
description: "Automatically generate session handoff document with accomplishments, pause point, and blockers + GitHub backup. Creates copiable summary for next session. Output: .agents/handoff/YYYY-MM-DD-topic.md + git commit + push. Triggers: handoff, session handoff, write handoff, continue session, session notes, pause point, next session, where we stopped, backup session."
---

# Handoff — Session Summary + GitHub Backup

Automatically generates a copiable summary of what you accomplished, where you paused, and what's next — plus backs up to GitHub.

**What it does:**
1. Analyzes recent git commits and file changes
2. Generates structured handoff document
3. Saves to `.agents/handoff/YYYY-MM-DD-topic.md`
4. Performs git add/commit/push to GitHub
5. Displays the document for you to copy/paste into next session

---

## How to Use

Simply invoke:

```
/handoff
```

Or specify a topic:

```
/handoff skill-fixes
```

---

## What Gets Generated

The skill automatically creates a document with:

**What We Accomplished**
- List of commits and changes from this session
- Files modified with brief description
- Features added, bugs fixed, skills created

**Where We Paused**
- Last action completed
- Next action to do
- Any blockers or pending decisions

**Files to Read First**
- Recently modified files listed
- Critical paths for next session

**Status**
- Ready for next session immediately

---

## Automatic Execution Flow

**When you invoke `/handoff`, Claude immediately executes:**

### Step 1 — Analyze Session (Automatic)
Claude runs:
```bash
git log --oneline -5
git diff --stat HEAD~5
```
Extracts: commit messages, changed files, theme/topic

### Step 2 — Generate Document (Automatic)
Claude creates `.agents/handoff/YYYY-MM-DD-topic.md` with:
- Date and session status
- What was accomplished (from commits)
- Where we paused (Claude asks you this)
- Files to read first (from changed files)
- Any blockers or decisions needed

### Step 3 — Ask for Session Summary
Claude asks you:
```
¿Dónde pausamos exactamente?

- Last action: [what was just done]
- Next action: [what should happen next]
- Blockers: [anything blocking progress]
```

Wait for your response, then incorporate into document.

### Step 4 — Display Document (Automatic)
Claude shows the complete generated document in chat:
- Full text visible for reading
- Ready to copy/paste entirely
- For pasting at start of next session

### Step 5 — GitHub Backup (Automatic)
Claude executes:
```bash
git add -A
git commit -m "Session: [topic] [timestamp]"
git push origin main
```

Shows commit hash and GitHub link as confirmation.

**Everything happens automatically** — no need to ask "do it now". Just invoke `/handoff` and it handles all 5 steps.

---

## Output Example

```
✓ Handoff document created:
  File: .agents/handoff/2026-05-14-bug-fixes.md
  
[Full document content below — copy for next session]

---

# Handoff: Bug Fixes

**Date:** 2026-05-14  
**Status:** Between tasks — ready to continue

## What We Accomplished This Session

### 1. Fixed retrospective skill not triggering
- Moved files from loose .md to folder structure
- All 13 skills now discoverable
- File: .claude/skills/retrospective/SKILL.md

### 2. Clarified auto-compact configuration
- Updated .claude/settings.json
- Added instructions to CLAUDE.md
- Context now compacts at 50% threshold

**Files changed (last 5):**
- .claude/settings.json
- .claude/skills/session-close/SKILL.md
- CLAUDE.md

## Where We Paused

Session complete. All skills working, backups current.

**Last action:** Ran session-close workflow  
**Next action:** Continue development (no blockers)

## Files to Read First

```
.claude/skills/session-close/SKILL.md
.claude/settings.json
```

---

✓ GitHub backup:
  Commit: c8cec62
  Message: "Session: bug-fixes 2026-05-14 20:34"
  
Status: Ready for next session
```

---

## Tips

- **Copy the entire document** — paste it at the start of next session for quick context
- **Customize before closing** — edit the document if you want to add notes
- **Always backs up** — even minimal handoff documents trigger git push
- **Use with session-close** — this is Paso 4 of the `/session-close` workflow
- **Manual or automatic** — invoke `/handoff` anytime, or let `/session-close` do it
