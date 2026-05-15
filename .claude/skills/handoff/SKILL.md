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

## Execution Flow

### Step 1: Analyze Session
Gathers recent commits, file changes, and identifies theme:
```bash
git log --oneline -5
git diff --stat HEAD~5
```

### Step 2: Generate Document
Creates `.agents/handoff/YYYY-MM-DD-topic.md` with structured format:
- Date and status
- Accomplishments section
- Pause point details
- Files to read first
- Questions or blockers

### Step 3: Display for Copy/Paste
Shows the generated document in the chat so you can:
- Read it immediately
- Copy entire document for next session
- Verify it captured everything correctly

### Step 4: GitHub Backup
```bash
git add -A
git commit -m "Session: [topic] [timestamp]"
git push origin main
```

### Step 5: Confirmation
Shows commit hash and link to GitHub so you can verify backup succeeded.

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
