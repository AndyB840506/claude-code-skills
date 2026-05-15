# Session Close — Implementation Instructions

This document defines how `/session-close` executes all 5 steps automatically.

## Auto-Execution Sequence

When Claude invokes `/session-close`, execute this sequence **without user interruption**:

```
STEP 1: Invoke /retrospective
  → User confirms: "Apply these changes?" YES/NO
  → Continue to STEP 2

STEP 2: Invoke /prompt-reviewer
  → User confirms: "Apply improvements?" YES/NO
  → Continue to STEP 3

STEP 3: Invoke /skill-management
  → User confirms: "Reorganize?" YES/NO
  → Continue to STEP 4

STEP 4: Invoke /handoff
  → NO USER CONFIRMATION NEEDED
  → Handoff runs to completion automatically
  → Continue to STEP 5

STEP 5: Copy handoff to Google Drive
  → NO USER CONFIRMATION NEEDED
  → Copy from current dir to G:\My Drive\claude projects\
  → Automatic sync via Google Drive Desktop
  → Display completion message
```

## Implementation Rules

1. **Steps 1-3 require user approval** — show results and ask for confirmation
2. **Steps 4-5 are automatic** — run without asking, just display progress
3. **Each step completes before next starts** — do not run in parallel
4. **Display clear status messages** — show which step is running and when it completes
5. **All changes are reversible** — everything goes through git
6. **Step 5 uses local file copy** — write handoff markdown to a temp file, then copy to `G:\My Drive\claude projects\` using bash `cp` or PowerShell `Copy-Item`

## User Prompts

**Step 1 Prompt:**
```
Found X learnings. Apply these changes? (YES/NO)
```

**Step 2 Prompt:**
```
Found Y improvements. Apply these changes? (YES/NO)
```

**Step 3 Prompt:**
```
Found Z structure issues. Reorganize? (YES/NO)
```

**Steps 4-5 Output:**
```
Step 4: Creating handoff document... ✓ Done
Step 5: Backing up to Google Drive... ✓ Done

Session closed successfully.
```

## Error Handling

**For Steps 1-3 (user confirmation steps):**
- If skill invocation fails: show error, ask user to retry or skip
- User can choose YES/NO even if results unclear

**For Step 4 (handoff):**
- If handoff invocation fails: display error and stop sequence
- User can retry with `/handoff` manually
- Cannot proceed to Step 5 without handoff output (clipboard content)

**For Step 5 (Google Drive file copy):**
- If file copy fails: show error but continue
- Display: "⚠ Could not back up to Google Drive: [reason]"
- Hint: "Check that `G:\My Drive\claude projects\` exists and is writable"
- **Do NOT stop** — Step 4 succeeded, backup is optional
- Session close still completes successfully
- Handoff is already in clipboard from Step 4

**General:**
- All git commits succeed or fail atomically (can be retried)
- All skill updates are reversible via git
- User can always retry entire `/session-close` from the start

## Storage Paths

- Handoff document: Lives in memory/clipboard only (not written to disk)
- Google Drive backup: `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
- Folder must exist beforehand: `G:\My Drive\claude projects\` (use Google Drive Desktop)

## Git Integration

Each step that modifies files should result in a clean git state:
- Step 1 changes tracked
- Step 2 changes tracked
- Step 3 changes tracked
- Step 4 creates one commit: `Session: [topic] YYYY-MM-DD HH:MM:SS`
- Step 4 pushes to GitHub (origin/main)

## Testing

To verify implementation:
1. Invoke `/session-close` in a test session
2. Confirm all 5 steps execute in order
3. Verify approval prompts appear for Steps 1-3
4. Verify Steps 4-5 run without prompts
5. Verify handoff document is copied to clipboard (can paste with Ctrl+V)
6. Check `G:\My Drive\claude projects\` for `handoff-[date].md` file
7. Verify git commit created and pushed
