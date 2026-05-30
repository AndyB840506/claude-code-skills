# Session Close — 5-Step Workflow Overview

Complete session closing in 5 steps: extract learnings, review skills, organize structure, and backup.

---

## Step 1: Retrospective — Extract Learnings

**Command:** `/retrospective`

**What happens:**
- Scans conversation for patterns: corrections, redone work, missing steps, what worked well
- Proposes updates to skill files based on learnings
- Asks "Apply these changes?" for each proposed change
- Updates skill files if approved

**Why it matters:**
- Captures learnings while they're fresh
- Prevents repeating the same issues
- Builds institutional knowledge into skills

**Time:** 2-3 minutes

---

## Step 2: Prompt Reviewer — Audit Skills

**Command:** `/prompt-reviewer`

**What happens:**
- Reviews skills for clarity issues, missing edge cases, effectiveness gaps
- Proposes specific improvements with reasoning
- Asks for confirmation before applying changes
- Updates documentation if approved

**Why it matters:**
- Ensures skills remain clear and maintainable
- Catches gaps from Step 1
- Improves quality of next iteration

**Time:** 2-3 minutes (optional if no changes from Step 1)

---

## Step 3: Skill Management — Verify Structure

**Command:** `/skill-management`

**What happens:**
- Audits folder structure (SKILL.md as router, workflows/, docs/)
- Checks for missing files or organization issues
- Proposes reorganization
- Asks "Reorganize?" before making changes

**Why it matters:**
- Ensures skills stay maintainable long-term
- Prevents structural debt
- Makes future updates easier

**Time:** 2-3 minutes (optional)

---

## Step 4: Handoff — Document & Backup

**Command:** `/handoff`

**What happens:**
- Generates handoff document in memory with:
  - Accomplishments from this session
  - Where to resume next session
  - Any blockers or issues
  - Files changed
- Copies complete document to clipboard (ready to paste with Ctrl+V)
- Displays document in chat
- Creates git commit with session data
- Pushes to GitHub

**Why it matters:**
- Creates clear handoff for next session (in clipboard)
- Automatic GitHub backup
- Preserves session context
- Ready to paste immediately

**Time:** 1-2 minutes

---

## Step 5: Google Drive Backup — Local File Copy

**Automatic** (no user action needed)

**What happens:**
- Takes handoff document from Step 4
- Writes to temp file: `handoff-[YYYY-MM-DD].md`
- Copies to: `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
- Deletes temp file
- Google Drive Desktop auto-syncs to cloud (5-10 seconds)

**Why it matters:**
- Triple backup (clipboard + GitHub + Google Drive)
- Accessible from Google Drive account
- Cloud sync happens automatically

**Time:** 5-10 seconds

---

## Step 6: Compact Context — Optimize Space

**Automatic**

**What happens:**
- Runs `/compact` command
- Compresses conversation history
- Removes verbose/redundant output
- Frees up context for next session

**Why it matters:**
- Prepares for long-running projects
- Optimizes token usage
- Maintains conversation efficiency
- Creates space for new work

**Time:** 1-2 seconds

---

## Step 7: Clear Screen — Start Fresh

**Optional** (after confirming paste)

**What happens:**
- Ask: "Have you pasted the handoff summary in your next session?"
- If YES: Execute `clear` to clean the screen
- If NO: Skip (user can clear manually)

**Why it matters:**
- Clean slate for next session
- No clutter from previous work
- Psychological reset

**Time:** < 1 second

---

## Execution Summary

| Step | Skill | Action | Time | Required |
|------|-------|--------|------|----------|
| 1 | Retrospective | Extract & apply learnings | 2-3m | Yes |
| 2 | Prompt Reviewer | Review & improve | 2-3m | No |
| 3 | Skill Management | Verify structure | 2-3m | No |
| 4 | Handoff | Copy to clipboard | 1-2m | Yes |
| 5 | Google Drive Sync | Auto-backup | Auto | Yes* |
| 6 | Compact | Compress context | 1-2s | Yes |
| 7 | Clear Screen | Clean screen | Auto | Optional |

*Requires Google Drive MCP installed

---

## Key Principles

- **No forced changes** — Every modification requires user confirmation
- **Independent steps** — Run any step in any order, skip as needed
- **Reversible** — All changes committed to git, easy to revert
- **Comprehensive** — Covers learnings, quality, structure, documentation, backup
