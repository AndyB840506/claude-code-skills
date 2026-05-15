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

See [Execution Workflow](workflows/execute.md) for step-by-step instructions to execute the 7-step session-close workflow.
