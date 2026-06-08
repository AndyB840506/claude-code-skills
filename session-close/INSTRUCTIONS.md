# Session Close — Implementation Instructions

This document defines how `/session-close` executes all 6 steps automatically.

## Auto-Execution Sequence

When Claude invokes `/session-close`, execute this sequence **without user interruption**:

```
STEP 1: Invoke /retrospective
  → User confirms: "Apply these changes?" YES/NO
  → Continue to STEP 2

STEP 2: Invoke /prompt-reviewer
  → User confirms: "Apply improvements?" YES/NO
  → Continue to STEP 3

STEP 3: Invoke /skill-kit-auditor
  → User confirms: "Apply fixes?" YES/NO
  → Continue to STEP 4

STEP 4: Invoke /handoff via Skill("handoff") tool call — NEVER generate handoff content inline as text
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
6. **Step 4 writes a file and pushes** — Handoff doc is written to `.agents/handoff/YYYY-MM-DD-<topic>.md`, committed, and pushed to origin/main
7. **CRITICAL: Step 4 must use Skill tool** — Call `Skill("handoff")` to invoke the handoff skill. NEVER write handoff content inline as text output — that bypasses the skill's clipboard and git logic entirely.
7. **Step 5 always executes** — Attempt to copy to Google Drive if folder exists; skip silently if not, but step itself is mandatory

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
Found Z issues in the skill kit. Apply fixes? (YES/NO)
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
- Writes `.agents/handoff/YYYY-MM-DD-<topic>.md`, commits, and pushes to origin/main
- If git commit/push fails: display error but continue (handoff file is still written to disk)
- Confirm: "Handoff saved to .agents/handoff/..., pushed to GitHub"

**For Step 5 (Google Drive backup):**
- Check if `G:\My Drive\claude projects\` folder exists
- If exists: copy handoff to Google Drive (optional, nice-to-have)
- If doesn't exist: skip silently (not an error condition)
- **Do NOT create files** if folder doesn't exist
- Session closes successfully either way
- Handoff is already safe in clipboard and GitHub

**General:**
- All git commits succeed or fail atomically (can be retried)
- All skill updates are reversible via git
- User can always retry entire `/session-close` from the start

## Storage Paths

**Primary Storage (Always):**
- File: `.agents/handoff/YYYY-MM-DD-<topic>.md` written to project repo
- Git: Commit + push to origin/main (automatic)

**Optional Storage (Step 5 only):**
- Google Drive: `G:\My Drive\claude projects\` (only if folder exists)

**Files Created:**
- ✓ `.agents/handoff/YYYY-MM-DD-<topic>.md` — handoff doc committed to repo
- ✓ Git commit created and pushed (automatic)
- ✓ Optional Google Drive copy (if folder exists)

## Git Integration

Each step that modifies files should result in a clean git state:
- Step 1 changes tracked
- Step 2 changes tracked
- Step 3 changes tracked
- Step 4 creates one commit: `Session: [topic] YYYY-MM-DD HH:MM:SS`
- Step 4 pushes to GitHub (origin/main)

### Git Commit Syntax (PowerShell)

In Windows PowerShell 5.1, use single-quoted here-strings for multi-line commit messages.
The closing `'@` must be at column 0 (no leading whitespace):

```powershell
git commit -m @'
First line summary

Body line.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
'@
```

Do NOT use Bash-style heredoc (`<<'EOF'`) — it fails in PowerShell 5.1.

## Testing

To verify implementation:
1. Invoke `/session-close` in a test session
2. Confirm all 5 steps execute in order
3. Verify approval prompts appear for Steps 1-3
4. Verify Steps 4-5 run without prompts
5. **CRITICAL:** Verify `.agents/handoff/YYYY-MM-DD-<topic>.md` was created in the repo
6. **CRITICAL:** Verify git commit and push succeeded (`git log -1`)
7. Verify git commit uses `handoff: <topic> YYYY-MM-DD` message format
8. (Optional) Check `G:\My Drive\claude projects\` if folder sync is enabled
