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

If any step fails:
1. Display error message
2. Show troubleshooting hint
3. Stop sequence (do NOT continue to next step)
4. User can retry entire `/session-close` or run individual steps

## Storage Paths

- Handoff document: `.agents/handoff/YYYY-MM-DD-topic.md`
- Google Drive backup: `G:\My Drive\claude projects\report-[name]-[YYYY-MM-DD].md`

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
5. Check `.agents/handoff/` folder for document
6. Check `G:\My Drive\claude projects\` for backup
7. Verify git commit created and pushed
