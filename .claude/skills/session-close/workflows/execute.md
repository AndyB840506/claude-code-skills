# Session Close — Automatic Execution Workflow

When you invoke `/session-close`, the skill automatically executes all 5 steps in order. You only need to confirm approval prompts when they appear.

---

## Complete Automated Flow

```
/session-close invoked
  ↓
Step 1: /retrospective → scan learnings → [YOU: confirm changes?] → update skills
  ↓
Step 2: /prompt-reviewer → review updated skills → [YOU: confirm improvements?] → improve docs
  ↓
Step 3: /skill-management → audit structure → [YOU: confirm reorganize?] → fix structure
  ↓
Step 4: /handoff → create document → git commit → push to GitHub → copy to clipboard
  ↓
Step 5: Google Drive Backup → copy handoff to G:\My Drive\claude projects → auto-sync
  ↓
✓ DONE — Session fully closed, documented, and backed up
```

---

## STEP 1: Retrospective (Automatic)

**What happens automatically:**
1. Scans your entire conversation for: corrections, redone work, missing steps, patterns that worked
2. Identifies which skills should be updated
3. Proposes specific changes with reasoning
4. Shows you a summary of learnings found

**You confirm:** "Apply these changes?" → YES/NO
- YES: Skill files updated with proposed changes
- NO: No changes made, continue to Step 2

**Expected output:**
- 2-5 learnings identified
- 1-3 skill files updated (if approved)
- Time: 2-3 minutes

---

## STEP 2: Prompt Reviewer (Automatic)

**What happens automatically:**
1. Reviews skills that were updated in Step 1 (or all skills if none updated)
2. Scans for: clarity issues, missing edge cases, effectiveness gaps
3. Proposes specific improvements with reasoning
4. Shows you improvement suggestions

**You confirm:** "Apply improvements?" → YES/NO
- YES: Skill documentation improved
- NO: No changes made, continue to Step 3

**Expected output:**
- 1-3 improvement suggestions
- 0-2 skills improved (if approved)
- Time: 2-3 minutes

---

## STEP 3: Skill Management (Automatic)

**What happens automatically:**
1. Audits skill folder structure
2. Checks each skill for proper layout: SKILL.md, workflows/, docs/
3. Identifies issues: missing files, incorrect routing, organization problems
4. Lists specific findings

**You confirm:** "Reorganize?" → YES/NO
- YES: Creates folders, moves files, updates routing
- NO: No changes made, continue to Step 4

**Expected output:**
- 0-3 structural issues identified
- 0-10 files reorganized (if approved)
- Time: 2-3 minutes

---

## STEP 4: Handoff (Fully Automatic)

**What happens automatically:**
1. Analyzes entire session from conversation
2. Creates `.agents/handoff/YYYY-MM-DD-topic.md` with:
   - **Accomplishments:** What was completed this session
   - **Pause Point:** Where to resume next session
   - **Blockers:** Any issues or decisions needed
   - **Files Changed:** List of modified files
3. Creates git commit: `Session: [topic] YYYY-MM-DD HH:MM:SS`
4. Pushes commit to GitHub
5. Copies handoff summary to clipboard (ready to paste in next session)

**No confirmation needed** — this step runs completely automatically

**Expected output:**
- Handoff file created in `.agents/handoff/`
- Git commit made and pushed
- Summary copied to clipboard
- Time: 1-2 minutes

---

## STEP 5: Google Drive Backup (Fully Automatic)

**What happens automatically:**
1. Locates the handoff file created in Step 4
2. Copies it to `G:\My Drive\claude projects\`
3. Google Drive for Desktop automatically syncs to cloud (5-10 seconds)

**No confirmation needed** — this step runs completely automatically

**Expected output:**
- Handoff file copied to Google Drive Desktop folder
- Cloud sync completed
- Confirmation: "✓ Handoff backed up to Google Drive"
- Time: 5-10 seconds

---

## Key Points

- **Automatic execution** — All 5 steps run sequentially when you invoke `/session-close`
- **Approval prompts** — Steps 1-3 ask you to confirm changes, Steps 4-5 run without approval
- **Reversible** — All changes tracked in git (use `git log` to see each step)
- **Total time** — ~10 minutes for full run (depends on session length)
- **Comprehensive** — Covers learnings, quality, structure, documentation, backup

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No learnings found" | Session may be too short or routine — skill continues to Step 4 |
| "Git push failed" | Check GitHub connection, ensure `git branch -u origin/main` is set |
| "Handoff file not created" | Check `.agents/` folder exists and has write permissions |
| "Google Drive copy failed" | Check `G:\My Drive\claude projects\` exists and is accessible |
| "No structure issues" | Skills are well-organized — Step 3 shows no changes needed |

---

## Success = All 5 Steps Complete

✓ Step 1: Retrospective (learnings extracted, skills updated if approved)  
✓ Step 2: Prompt Reviewer (documentation improved if approved)  
✓ Step 3: Skill Management (structure verified, reorganized if approved)  
✓ Step 4: Handoff (document generated, committed, pushed to GitHub)  
✓ Step 5: Google Drive Backup (document copied to `G:\My Drive\claude projects`)

**Session is fully closed, documented, and backed up.**
