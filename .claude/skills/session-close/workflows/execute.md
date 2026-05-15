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
  Generate doc in memory
  Copy to clipboard (Ctrl+V ready)
  Display in chat
  Commit to git, push to GitHub
  ↓
Step 5: Copy handoff to Google Drive (automatic)
  Write handoff content to temp file locally
  Copy to G:\My Drive\claude projects\ using cp
  Delete temp file
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

1. Analyzes the session from git history and conversation context
2. Generates structured handoff document in memory:
   - **Date and topic** — When and what
   - **Accomplishments** — 3-5 bullet points of what was completed
   - **Files changed** — List of modified files
   - **Pause point** — Where to resume next session
   - **Next actions** — What should happen next
   - **Blockers** — Any issues preventing progress
3. Copies the complete document to clipboard using `$content | Set-Clipboard`
4. Displays the document in chat (so you can see what was created)
5. Creates and pushes git commit:
   ```bash
   git add -A
   git commit -m "Session: [topic] YYYY-MM-DD HH:MM:SS"
   git push origin main
   ```

**What the handoff document contains:**
- Complete session summary ready to paste with Ctrl+V in next session
- All essential information to resume work
- Structured format for easy reading

**Storage:**
- Primary: Clipboard (for pasting in next session)
- Backup: GitHub (git commit history)
- Not written to any local file — lives in memory only

**Output:** 
- Document displayed in chat
- Confirmation: "✓ Handoff created and committed to GitHub"
- Ready to paste in next session with Ctrl+V

**No user confirmation needed**

**Then continues to Step 5**

---

## STEP 5: Google Drive Backup (Fully Automatic)

Claude automatically:

1. Takes the handoff document content from Step 4 (still in context)
2. Writes it to a temporary file: `handoff-[YYYY-MM-DD].md` in the project root
3. Copies the file to Google Drive Desktop folder using bash:
   ```bash
   cp "handoff-2026-05-15.md" "/g/My Drive/claude projects/handoff-2026-05-15.md"
   ```
4. Deletes the temporary file from project root
5. Google Drive for Desktop automatically syncs to cloud (5-10 seconds)

**Process:**
```
Write temp file: handoff-2026-05-15.md
Copy: project root → G:\My Drive\claude projects\
Delete temp file
Google Drive Desktop syncs automatically
```

**Storage:**
- Local: `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
- Cloud: Automatically synced by Google Drive Desktop to your Google Drive account

**Output:** "✓ Handoff backed up to Google Drive"

**No user confirmation needed**

**If backup fails:**
- Display error message with reason (e.g., "could not copy to G:\My Drive\claude projects\")
- Show hint to troubleshoot (e.g., "Check that the folder exists and is writable")
- **Do NOT stop** — Step 4 succeeded, handoff is safe in clipboard and GitHub
- Session close still completes successfully
- You can manually copy the file later if needed

---

## Summary

| Step | User Action | What Claude Does |
|------|-------------|------------------|
| 1 | Confirm changes | Invoke /retrospective → update skills if approved |
| 2 | Confirm improvements | Invoke /prompt-reviewer → improve docs if approved |
| 3 | Confirm reorganization | Invoke /skill-management → fix structure if approved |
| 4 | None (automatic) | Invoke /handoff → generate doc, copy to clipboard, commit to git |
| 5 | None (automatic) | Write handoff to temp file, copy to G:\My Drive\claude projects\ |

---

## Timing & Expectations

- **Step 1:** 2-3 minutes (scans conversation)
- **Step 2:** 2-3 minutes (reviews documentation)
- **Step 3:** 1-2 minutes (audits structure)
- **Step 4:** 1-2 minutes (generates handoff & commits)
- **Step 5:** 5-10 seconds (copies to Google Drive folder)
- **Total:** ~10 minutes for complete session close

---

## What Gets Backed Up

**Clipboard backup (immediate, next session):**
- Full handoff document ready to paste with Ctrl+V

**Git backup (GitHub):**
- Session commit with all file changes
- Full conversation history in local git repository

**Cloud backup (Google Drive):**
- `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
- Automatically synced by Google Drive Desktop

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| "No learnings found" | Short session or no corrections | Normal — skill continues to Step 4 |
| Step 4 fails | Git or GitHub issue | Check git status, verify GitHub connection |
| Step 5 fails | Google Drive folder not accessible | Ensure `G:\My Drive\claude projects\` exists and has write permissions |
| Whole sequence stuck | Skills not found | Ensure `/retrospective`, `/prompt-reviewer`, `/skill-management` exist |

---

## Next Session

1. **Paste from clipboard** — Use Ctrl+V to paste the handoff summary at the start of your next session
2. **Review the summary** — It shows what was accomplished and where to resume
3. **Optional: Check Google Drive** — The same handoff is also saved at `G:\My Drive\claude projects\handoff-[date].md` for reference
