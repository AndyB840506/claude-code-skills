# Session Close Execution Workflow

Execute the 5-step workflow in order. Each step builds on previous ones. All confirmation checkpoints give user full control.

---

## STEP 1: Extract Learnings (Retrospective)

**Command to execute:**
```
/retrospective
```

**What happens:**
1. Scans conversation for: corrections, redone work, missing steps, what worked well
2. Identifies which skills should be updated
3. Proposes specific changes with reasoning
4. Displays table of learnings: `| # | Learning | Skill | Change |`
5. Asks: "Apply these changes?" 

**If user says YES:**
- Skill files updated with proposed changes
- Each change shown with diff context

**If user says NO:**
- No changes made, continue to Step 2

**Expected output:**
- 2-5 learnings identified
- 1-3 skill files updated (if approved)
- Time: 2-3 minutes

---

## STEP 2: Review Skills (Prompt Reviewer)

**Command to execute:**
```
/prompt-reviewer
```

**What happens:**
1. Reviews skills that were updated in Step 1 (or all skills if none updated)
2. Scans for: clarity issues, missing edge cases, effectiveness gaps
3. Proposes specific improvements with reasoning
4. Asks: "Apply improvements?"

**If user says YES:**
- Skill documentation improved
- Changes shown with specific examples

**If user says NO:**
- No changes made, continue to Step 3

**Expected output:**
- 1-3 improvement suggestions
- 0-2 skills improved (if approved)
- Time: 2-3 minutes (optional if Step 1 made few changes)

---

## STEP 3: Verify Structure (Skill Management)

**Command to execute:**
```
/skill-management
```

**What happens:**
1. Audits skill folder structure
2. Checks each skill for proper layout: SKILL.md, workflows/, docs/
3. Identifies issues: missing files, incorrect routing, organization problems
4. Lists specific findings
5. Asks: "Reorganize?"

**If user says YES:**
- Creates missing folders
- Moves files to proper locations
- Updates SKILL.md routing if needed
- Shows what was reorganized

**If user says NO:**
- No changes made, continue to Step 4

**Expected output:**
- 0-3 structural issues identified
- 0-10 files reorganized (if approved)
- Time: 2-3 minutes (optional)

---

## STEP 4: Document & Backup (Handoff)

**Command to execute:**
```
/handoff
```

**What happens:**
1. Analyzes entire session from conversation
2. Creates `.agents/handoff/YYYY-MM-DD-topic.md` with:
   - **Accomplishments:** What was completed this session
   - **Pause Point:** Where to resume next session
   - **Blockers:** Any issues or decisions needed
   - **Files Changed:** List of modified files
3. Creates git commit: `Session: session-topic YYYY-MM-DD HH:MM:SS`
4. Pushes commit to GitHub
5. Copies handoff summary to clipboard

**Expected output:**
- Handoff file created in `.agents/handoff/`
- Git commit made and pushed
- Summary copied to clipboard
- Time: 1-2 minutes

**Note:** This step runs automatically — no confirmation needed

---

## STEP 5: Google Drive Sync (Automatic)

**What happens:**
1. If Google Drive MCP is installed: handoff document automatically synced to Google Drive
2. If not installed: silently skips (no error)

**Expected output:**
- Handoff file backed up to Google Drive (if configured)
- Time: Automatic, < 1 second

---

## STEP 6: Clear Screen (Optional)

**What happens:**
1. Ask user: "Have you pasted the handoff summary in your next session?"
2. If YES: Execute `clear` to clean the screen
3. If NO: Skip (user can clear manually later)

**Purpose:**
- Cleans up the screen after session ends
- Ensures fresh start for next session
- Only runs after user confirms they've pasted the handoff

**Expected output:**
```
Have you pasted the handoff summary in your next session? [yes/no]

✓ Session closed and screen cleared. Ready for new work!
```

**Time:** < 1 second

---

## Full Execution Flow

```
START
  ↓
Step 1: /retrospective → [confirm changes?] → update skills
  ↓
Step 2: /prompt-reviewer → [confirm improvements?] → improve docs
  ↓
Step 3: /skill-management → [confirm reorganize?] → fix structure
  ↓
Step 4: /handoff → [automatic] → copy to clipboard
  ↓
Step 5: Google Drive sync → [automatic] → backup to Drive
  ↓
Step 6: Clear screen → [confirm pasted?] → clear screen
  ↓
DONE ✓
```

---

## Key Principles

- **User in control** — Every modification requires explicit approval
- **Independent steps** — Can skip, rerun, or do in different order
- **Reversible** — All changes tracked in git (git log shows each step)
- **Fast** — ~10 minutes total for full run
- **Comprehensive** — Covers learnings, quality, structure, documentation, backup

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No learnings found" | Session may be too short or routine — continue to handoff |
| "Git push failed" | Check GitHub connection, ensure `git branch -u origin/main` is set |
| "Handoff file not created" | Check `.agents/` folder exists and has write permissions |
| "No structure issues" | Skills are well-organized — this is good |

---

## Success = All 6 Steps Complete

✓ Retrospective: Learnings extracted (or skipped)  
✓ Prompt Reviewer: Skills improved (or skipped)  
✓ Skill Management: Structure verified (or reorganized)  
✓ Handoff: Document copied to clipboard  
✓ Google Drive: Synced (or skipped if not configured)  
✓ Clear Screen: Confirmed paste, cleared (or skipped)  

Session is closed and ready for next session with a clean slate.
