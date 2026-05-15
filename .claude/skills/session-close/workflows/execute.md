# Session Close — Complete Execution Flow

When you invoke `/session-close`, Claude executes all 5 steps in sequence. Steps 1-3 require your confirmation; Steps 4-5 run automatically.

---

## How Claude Executes `/session-close`

```
/session-close invoked by user
  ↓
Step 1: Invoke /retrospective
  Show learnings → [USER: confirm?] → continue
  ↓
Step 2: Invoke /prompt-reviewer  
  Show improvements → [USER: confirm?] → continue
  ↓
Step 3: Invoke /skill-management
  Show structure issues → [USER: confirm?] → continue
  ↓
Step 4: Invoke /handoff (automatic)
  Create .agents/handoff/[date].md
  Commit to git, push to GitHub
  Copy to clipboard
  ↓
Step 5: Copy handoff to Google Drive (automatic)
  Read handoff file from .agents/handoff/
  Create copy in G:\My Drive\claude projects\
  Display completion
  ↓
✓ DONE — All 5 steps complete, session backed up
```

---

## STEP 1: Retrospective (Show Results + Confirm)

Claude invokes `/retrospective` which scans the conversation for:
- Corrections to existing behavior
- Work that was redone or needed adjustment
- Patterns that worked well
- Missing steps in workflows

**Output:** List of 2-5 learnings with proposed skill updates

**Claude asks you:** "Apply these changes? (YES/NO)"

**Your response determines:** Whether to update skills or skip

**Then continues to Step 2**

---

## STEP 2: Prompt Reviewer (Show Results + Confirm)

Claude invokes `/prompt-reviewer` which reviews skills (updated ones from Step 1, or all if none updated) for:
- Clarity issues in documentation
- Missing edge cases
- Effectiveness gaps
- Completeness of instructions

**Output:** List of 1-3 improvement suggestions

**Claude asks you:** "Apply these improvements? (YES/NO)"

**Your response determines:** Whether to improve docs or skip

**Then continues to Step 3**

---

## STEP 3: Skill Management (Show Results + Confirm)

Claude invokes `/skill-management` which audits the skills folder for:
- Proper file structure (SKILL.md, workflows/, docs/)
- Missing or misplaced files
- Incorrect routing
- Organization issues

**Output:** List of 0-3 structure issues found

**Claude asks you:** "Reorganize? (YES/NO)"

**Your response determines:** Whether to reorganize or skip

**Then continues to Step 4**

---

## STEP 4: Handoff (Fully Automatic)

Claude invokes `/handoff` which automatically:
1. Analyzes entire session from conversation
2. Creates `.agents/handoff/YYYY-MM-DD-[topic].md` with:
   - **Summary** — what was accomplished
   - **Pause Point** — where to resume next session  
   - **Blockers** — any unresolved issues
   - **Files Changed** — list of modified files
3. Creates git commit: `Session: [topic] YYYY-MM-DD HH:MM:SS`
4. Pushes commit to GitHub (origin/main)
5. Copies summary to clipboard for pasting in next session

**Output:** Confirmation that handoff is created and committed

**No user confirmation needed**

**Then continues to Step 5**

---

## STEP 5: Google Drive Backup (Fully Automatic)

Claude automatically:
1. Reads the handoff file just created in Step 4 from `.agents/handoff/[date].md`
2. Uses Google Drive API tool to copy it to `G:\My Drive\claude projects\`
3. Creates file with name: `handoff-[YYYY-MM-DD].md`
4. Google Drive for Desktop automatically syncs to cloud (5-10 seconds)

**Process:**
```
Read: .agents/handoff/2026-05-15-[topic].md
Create in Google Drive: G:\My Drive\claude projects\handoff-2026-05-15.md
Sync happens automatically via Google Drive Desktop
```

**Output:** "✓ Handoff backed up to Google Drive"

**No user confirmation needed**

**If backup fails:**
- Display error message with reason
- Show hint to troubleshoot
- Continue anyway (Step 4 succeeded, backup is secondary)
- Session still closes successfully

---

## Summary

| Step | User Action | What Claude Does |
|------|-------------|------------------|
| 1 | Confirm changes | Invoke /retrospective → update skills if approved |
| 2 | Confirm improvements | Invoke /prompt-reviewer → improve docs if approved |
| 3 | Confirm reorganization | Invoke /skill-management → fix structure if approved |
| 4 | None (automatic) | Invoke /handoff → create document & git commit |
| 5 | None (automatic) | Copy handoff to Google Drive using API tool |

---

## Timing & Expectations

- **Step 1:** 2-3 minutes (scans conversation)
- **Step 2:** 2-3 minutes (reviews documentation)
- **Step 3:** 1-2 minutes (audits structure)
- **Step 4:** 1-2 minutes (creates handoff & commits)
- **Step 5:** 10-30 seconds (copies to Google Drive)
- **Total:** ~10 minutes for complete session close

---

## What Gets Backed Up

**Local backup (git):**
- `.agents/handoff/YYYY-MM-DD-[topic].md` — committed to git
- All skill updates from Steps 1-3 — tracked in git history

**Cloud backup (Google Drive):**
- `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md` — synced by Google Drive Desktop

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| "No learnings found" | Short session or no corrections | Normal — skip to Step 4 |
| Step 4 fails | Git or GitHub issue | Check git status, verify GitHub connection |
| Step 5 fails | Google Drive not accessible | Ensure `G:\My Drive\claude projects\` exists, check Google Drive Desktop |
| Whole sequence stuck | Skills not found | Ensure `/retrospective`, `/prompt-reviewer`, `/skill-management` exist |

---

## Next Session

Start by reviewing the handoff copied to clipboard:
- It summarizes what was accomplished
- Shows where to resume work
- Lists any blockers or decisions needed

File also stored at: `G:\My Drive\claude projects\handoff-[date].md` for easy reference.
