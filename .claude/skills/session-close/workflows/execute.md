# Session Close Execution Workflow

You have invoked `/session-close`. Execute the 5-step workflow in order. Each step MUST complete before proceeding to the next.

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

## STEP 5: Google Drive Backup

**ACTION:** Copy handoff document to Google Drive backup folder

**What happens:**
1. Locate latest `report-[name]-[YYYY-MM-DD].md` in current working directory
2. Copy to `G:\My Drive\claude projects\`
3. Report: "✓ Handoff backed up to Google Drive (`G:\My Drive\claude projects`)"

**Expected output:**
- Handoff file copied to Google Drive Desktop folder
- Automatic sync via Google Drive for Desktop handles upload
- Time: 1-2 seconds

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
Step 4: /handoff → [automatic] → copy to clipboard + GitHub backup
  ↓
Step 5: Google Drive backup → [automatic] → copy to G:\My Drive\claude projects
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

## Success = All 5 Steps Complete

✓ Step 1: Retrospective (learnings extracted, skills updated if approved)  
✓ Step 2: Prompt Reviewer (documentation improved if approved)  
✓ Step 3: Skill Management (structure verified, reorganized if approved)  
✓ Step 4: Handoff (document generated and backed up to GitHub)  
✓ Step 5: Google Drive Backup (document copied to `G:\My Drive\claude projects`)

**Session is fully closed, documented, and backed up.**
