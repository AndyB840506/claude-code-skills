# Session Close — What to Expect

Expected behavior and output at each step of the session-close workflow.

---

## Step 1: Retrospective

### Expected Output

**Console:**
```
Running /retrospective...

Analyzing session for learnings...

LEARNINGS FOUND:
| # | Learning | Skill | Change |
|---|----------|-------|--------|
| 1 | X behavior pattern | skill.md | Add section |
| 2 | Y was missing | docs/ | Create guide |

Apply these changes? [y/n]
```

**If YES:**
- Skill files updated with new learnings
- Each file change shown with diff context

**If NO:**
- Changes discarded, continue to next step

### Duration
2-3 minutes

### When It May Be Skipped
- Very short sessions (< 30 minutes)
- Routine tasks without learnings
- When redoing retrospective from same context

---

## Step 2: Prompt Reviewer

### Expected Output

**Console:**
```
Running /prompt-reviewer on updated skills...

Found 2-3 improvement opportunities:

1. Clarity issue in skill X: "...confusing phrasing..."
2. Missing edge case in skill Y: "...should handle..."
3. Effectiveness: "...could be more concise..."

Apply improvements? [y/n]
```

**If YES:**
- Skill documentation improved
- Specific changes highlighted

**If NO:**
- Changes discarded, continue to next step

### Duration
2-3 minutes (optional)

### When It May Be Skipped
- If no changes from Step 1
- If skills already well-reviewed
- Time constraints

---

## Step 3: Skill Management

### Expected Output

**Console:**
```
Running /skill-management...

Auditing skill structure...

ISSUES FOUND:
- Missing workflows/ folder in skill X
- Docs not organized in skill Y
- SKILL.md routing issue in skill Z

Reorganize? [y/n]
```

**If YES:**
- Folders created/reorganized
- Files moved to proper locations
- SKILL.md updated if needed

**If NO:**
- Continue to next step

### Duration
2-3 minutes (optional)

### When It May Be Skipped
- Recently reorganized
- No structural issues found
- Focus on content over structure

---

## Step 4: Handoff

### Expected Output

**Console:**
```
Running /handoff...

Generating handoff document...
✓ Analyzed session from git and conversation
✓ Generated handoff document
✓ Copied to clipboard (ready to paste with Ctrl+V)
✓ Committed: "Session: session-topic 2026-05-14 18:30:00"
✓ Pushed to GitHub

Handoff document copied to clipboard
```

**Handoff Document Contents:**
- Date and topic
- Accomplishments from this session
- Pause point for next session
- Any blockers or issues
- Files changed
- Next actions

**Storage:**
- Primary: Your clipboard (ready to paste in next session with Ctrl+V)
- Backup: GitHub (committed to git history)

### Duration
1-2 minutes

### Expected Git Log
```
Session: session-topic 2026-05-14 18:30:00 (HEAD)
session-topic skill updates + handoff document
```

---

## Step 5: Google Drive Backup

### Expected Output

**Console:**
```
Step 5: Backing up to Google Drive...
✓ Handoff backed up to Google Drive
```

**File Created:**
`G:\My Drive\claude projects\handoff-2026-05-14.md`

**What happens:**
- Handoff document (from Step 4) written to temp file
- Copied to Google Drive Desktop folder
- Temp file deleted
- Google Drive Desktop auto-syncs to cloud (5-10 seconds)

**If you see error:**
- Displays warning but continues (backup is optional)
- Local clipboard + GitHub backups still exist
- You can manually copy the file later

### Duration
5-10 seconds

---

## Step 6: Compact Context

### Expected Output

**Console:**
```
Compacting conversation history...
✓ Context compressed: 2500+ tokens freed
Ready for next session
```

### Duration
1-2 seconds

---

## Step 7: Clear Screen

### Expected Output

**Console:**
```
Have you pasted the handoff summary in your next session?
[yes/no]
```

**If YES:**
```
✓ Session closed and screen cleared.
Ready for new work!

[Screen clears]
```

**If NO:**
- Screen stays as is
- User can clear manually later with `clear` command

### Duration
< 1 second

---

## Full Session Output Timeline

```
Starting session-close...
[~3m] Retrospective: Learnings extracted + confirmed
[~3m] Prompt Reviewer: Skills improved + confirmed
[~3m] Skill Management: Structure verified + confirmed
[~2m] Handoff: Document copied to clipboard
[<1s] Google Drive: Auto-synced
[<1s] Clear: Confirmed + cleared
[Total: ~10 minutes]

Session closed ✓
```

---

## Troubleshooting

### "No learnings found"
- Session may be too short
- Work may not involve skill changes
- This is normal — continue to handoff

### "No improvements suggested"
- Skills are well-written
- This is good — continue to next step

### "Git push failed"
- Check GitHub connection
- Ensure main branch tracking is set: `git branch -u origin/main`
- Retry handoff step manually

### "Handoff file not created"
- Check `.agents/` folder exists
- Ensure write permissions to directory
- Check disk space

---

## Success Criteria

Session close is complete when you see:

✓ Retrospective completed (learnings captured or skipped)  
✓ Prompt Reviewer completed (improvements applied or skipped)  
✓ Skill Management completed (structure verified or reorganized)  
✓ Handoff text copied to clipboard  
✓ Google Drive synced (or skipped if not configured)  
✓ Screen cleared (or user chose to skip)  

At this point, your session is fully documented, backed up, and ready for next session.
