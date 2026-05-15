---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Complete Closing Workflow

Automated 7-step workflow to close your session: analyze learnings, review skills, organize structure, backup everything, and prepare for next session.

**Executes in order:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive sync → Compact Context → Clear Screen

---

## How It Works

Execute the following 7-step workflow in order. See [Execution Workflow](workflows/execute.md) for detailed process:

**Step 1: Retrospective**
- Run: `/retrospective`
- Extracts learnings, proposes skill updates
- User confirms or skips changes

**Step 2: Prompt Reviewer**
- Run: `/prompt-reviewer`
- Reviews and improves updated skills (optional)
- User confirms or skips changes

**Step 3: Skill Management**
- Run: `/skill-management`
- Verifies folder structure, suggests fixes (optional)
- User confirms or skips changes

**Step 4: Handoff**
- Run: `/handoff`
- Generates handoff document
- Creates git commit + push to GitHub

**Step 5: Google Drive Sync** (Automatic)
- Backup document is automatically synced to Google Drive if MCP is configured

**Step 6: Compact Context** (Automatic)
- Run: `/compact`
- Compresses conversation history to free context space
- No user interaction needed

**Step 7: Clear Screen** (Optional)
- Asks user confirmation: "Have you pasted the handoff summary in your next session?"
- If YES: Clears the screen for a fresh start
- If NO: Skips, user can clear manually later

Steps 1-3 are independent and optional (skip or rerun as needed). Steps 4-6 run sequentially. Step 7 is optional based on user preference.

---

---

## Documentation

- **[Workflow Overview](docs/workflow-overview.md)** — Detailed breakdown of each step
- **[When to Use](docs/when-to-use.md)** — Decision tree for running session-close
- **[What to Expect](docs/what-to-expect.md)** — Expected output and troubleshooting
- **[Execution Workflow](workflows/execute.md)** — Step-by-step execution guide

---

## Output

✓ Skill improvements (if approved)  
✓ Handoff document copied to clipboard (Ctrl+V to paste in next session)  
✓ Google Drive sync (if installed, automatic)  
✓ Context compressed (Step 6)  
✓ Screen cleared for fresh start (Step 7, optional)  

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up
- **Optional during long sessions** — run individual steps mid-stream

---

## EXECUTION

You have invoked `/session-close`. Execute the 7-step workflow in order. Each step MUST complete before proceeding to the next.

---

## STEPS 1-4: User-Confirmation Steps

### Step 1: Retrospective
```
/retrospective
```
- Waits for user confirmation
- If YES: applies skill updates
- If NO or SKIP: continues to Step 2
- **Then proceed to Step 2**

### Step 2: Prompt Reviewer  
```
/prompt-reviewer quick
```
- Waits for user confirmation
- If YES: applies improvements
- If NO or SKIP: continues to Step 3
- **Then proceed to Step 3**

### Step 3: Skill Management
```
/skill-management audit
```
- Reports audit results (no changes needed or will ask for confirmation)
- If changes approved: applies them
- **Then proceed to Step 4**

### Step 4: Handoff
```
/handoff
```
- Generates document and copies to clipboard
- Creates git commit and pushes to GitHub
- **Then proceed to Step 5 immediately**

---

## STEPS 5-7: Sequential Execution (Must execute in moment; Step 7 requires confirmation)

### Step 5: Google Drive Sync
**ACTION:** Attempt to sync handoff to Google Drive if MCP is configured
- If Google Drive MCP is available: sync the handoff document
- If Google Drive MCP is NOT available: report "Google Drive MCP not installed - sync skipped"
- **Result:** Backup created or skipped. Continue to Step 6 immediately.

### Step 6: Compact Context  
**ACTION:** Execute compact command
```
/compact
```
**MUST EXECUTE:** This is not optional. User may need to run this themselves if `/compact` requires user input.
- Report: "Context compressed. Ready for next session."
- **Continue to Step 7 immediately**

### Step 7: Clear Screen (Final Confirmation)
**ACTION:** Ask user for confirmation
```
Have you pasted the handoff summary in your next session?
[yes/no]
```
- **If YES:** Execute clear screen command: `clear`
  - Report: "✓ Session closed and screen cleared. Ready for new work!"
- **If NO:** Report: "✓ Session complete. You can clear the screen manually anytime with `clear` command."

---

## Success Criteria

All 7 steps completed in sequence:
✓ Step 1: Retrospective (learnings captured)
✓ Step 2: Prompt Reviewer (improvements applied)
✓ Step 3: Skill Management (structure verified)
✓ Step 4: Handoff (document generated and backed up)
✓ Step 5: Google Drive (sync attempted or skipped)
✓ Step 6: Compact (context compressed)
✓ Step 7: Clear (screen cleared or skipped)

**Session is fully closed, documented, and ready for next session.**
