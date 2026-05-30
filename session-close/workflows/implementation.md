# Session Close — Complete Implementation Guide

When a user invokes `/session-close`, follow this exact sequence:

## STEP 1: Retrospective (Requires User Confirmation)

```
Display: "Step 1: Analyzing session for learnings..."

Invoke: /retrospective
  (This scans the conversation for corrections, redone work, patterns)

Collect the findings and show summary:
  "Found X learnings:
   - Learning 1: [description]
   - Learning 2: [description]"

Ask user: "Apply these changes? (YES/NO)"

If YES:
  → Continue retrospective to update skills
  → Display "✓ Skills updated"
  
If NO:
  → Skip retrospective updates
  → Display "Skipped"

Continue to STEP 2
```

## STEP 2: Prompt Reviewer (Requires User Confirmation)

```
Display: "Step 2: Reviewing skill documentation..."

Invoke: /prompt-reviewer
  (This checks for clarity issues, missing cases, gaps)

Collect findings and show summary:
  "Found Y improvements:
   - Improvement 1: [description]
   - Improvement 2: [description]"

Ask user: "Apply these improvements? (YES/NO)"

If YES:
  → Continue reviewer to improve skills
  → Display "✓ Documentation improved"
  
If NO:
  → Skip improvements
  → Display "Skipped"

Continue to STEP 3
```

## STEP 3: Skill Management (Requires User Confirmation)

```
Display: "Step 3: Checking skill structure..."

Invoke: /skill-management
  (This audits folder structure, naming, organization)

Collect findings and show summary:
  "Found Z structure issues:
   - Issue 1: [description]
   - Issue 2: [description]"

Ask user: "Reorganize? (YES/NO)"

If YES:
  → Continue management to fix structure
  → Display "✓ Structure reorganized"
  
If NO:
  → Skip reorganization
  → Display "Skipped"

Continue to STEP 4
```

## STEP 4: Handoff (Fully Automatic)

```
Display: "Step 4: Generating handoff document..."

Invoke: /handoff
  (This generates session summary in memory, copies to clipboard, and makes git commit)

What /handoff does:
  1. Analyzes git history and conversation context
  2. Generates handoff markdown in memory (accomplishments, pause point, blockers, etc.)
  3. Copies the complete document to clipboard (Ctrl+V ready)
  4. Displays the full document in chat
  5. Creates git commit: Session: [topic] YYYY-MM-DD HH:MM:SS
  6. Pushes commit to GitHub (origin/main)

Wait for completion. Should result in:
  - Handoff document in clipboard (ready to paste)
  - Document displayed in chat
  - Git commit made and pushed

Display: "✓ Handoff created and committed to GitHub"

Continue to STEP 5
```

## STEP 5: Google Drive Backup (Fully Automatic)

```
Display: "Step 5: Backing up to Google Drive..."

Take the handoff document from Step 4 (content still in context):
  → Extract the full markdown content
  → Generate filename: handoff-[YYYY-MM-DD].md

Write to temporary file in project root:
  → Create file: handoff-[YYYY-MM-DD].md
  → Write the complete handoff markdown

Copy to Google Drive Desktop folder:
  → Use bash: cp "handoff-[YYYY-MM-DD].md" "/g/My Drive/claude projects/handoff-[YYYY-MM-DD].md"
  → Wait for copy to complete

Delete the temporary file:
  → Remove handoff-[YYYY-MM-DD].md from project root

Google Drive Desktop auto-sync:
  → File automatically synced to cloud (5-10 seconds)

Display: "✓ Handoff backed up to Google Drive"

Continue to completion summary
```

## COMPLETION

```
Display final summary:

"Session closed successfully ✓

✓ Step 1: Retrospective (learnings extracted)
✓ Step 2: Prompt Reviewer (documentation improved)
✓ Step 3: Skill Management (structure verified)
✓ Step 4: Handoff (created & committed)
✓ Step 5: Google Drive (backed up)

All changes are tracked in git. Ready for next session."
```

## Error Handling

If any step fails:
1. Display the error message
2. Show troubleshooting hint
3. **For Steps 1-3:** User can retry with YES/NO answer
4. **For Steps 4-5:** Can be retried manually with `/handoff`
5. Entire sequence can be rerun with `/session-close`

## Key Rules

1. **Sequential execution** — never run steps in parallel
2. **Each step completes before next starts** — wait for tool responses
3. **Steps 1-3 are interactive** — show results and ask for confirmation
4. **Steps 4-5 are automatic** — run without interruption
5. **All changes reversible** — everything tracked in git
6. **Clear messaging** — always show which step is running

## Storage Paths

- Handoff primary: Clipboard (ready to paste with Ctrl+V)
- Handoff backup (git): GitHub commit history
- Handoff backup (Google Drive): `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
- Git branch: `main` (always)
- Git remote: `origin` (GitHub)
