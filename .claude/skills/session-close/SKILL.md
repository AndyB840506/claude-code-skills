---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Complete Closing Workflow

Automated 5-step workflow to close your session: analyze learnings, review skills, organize structure, and backup everything.

**Executes in order:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive sync

---

## How It Works

Execute the following 5-step workflow in order. See [Execution Workflow](workflows/execute.md) for detailed process:

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

Steps 1-3 are independent and optional (skip or rerun as needed). Steps 4-5 run sequentially at the end: handoff must complete before Google Drive sync.

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

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up
- **Optional during long sessions** — run individual steps mid-stream

---

---

## EXECUTION

You have invoked `/session-close`. Now execute the 5-step workflow below in order.

### Execute Step 1: Retrospective

Run this command:
```
/retrospective
```

Wait for user confirmation. If approved, skill updates are made. If skipped, continue to Step 2.

### Execute Step 2: Prompt Reviewer

Run this command:
```
/prompt-reviewer
```

Wait for user confirmation. If approved, improvements are made. If skipped, continue to Step 3.

### Execute Step 3: Skill Management

Run this command:
```
/skill-management
```

Wait for user confirmation. If approved, structure is fixed. If skipped, continue to Step 4.

### Execute Step 4: Handoff

Run this command:
```
/handoff
```

This step runs automatically — no confirmation needed. It creates the handoff document, commits, and pushes to GitHub.

### Execute Step 5: Google Drive Sync

This happens automatically if Google Drive MCP is configured. No action needed.

---

**Session close workflow complete!** All 5 steps have executed. Session is documented and backed up.
