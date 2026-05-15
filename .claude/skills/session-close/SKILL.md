---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Complete Closing Workflow

Automated 5-step workflow to close your session: analyze learnings, review skills, organize structure, and backup everything.

**Executes in order:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive sync

---

## Quick Start

```
/session-close
```

Or run steps individually:

```
/retrospective        # Step 1: Analyze learnings
/prompt-reviewer      # Step 2: Review skills
/skill-management     # Step 3: Organize structure
/handoff              # Step 4: Document + GitHub backup
                      # Step 5: Auto-sync to Google Drive (automatic)
```

---

## 5-Step Workflow

| Step | Skill | Purpose |
|---|---|---|
| 1 | Retrospective | Extract learnings, propose skill updates |
| 2 | Prompt Reviewer | Audit and improve skills |
| 3 | Skill Management | Verify folder structure |
| 4 | Handoff | Generate summary doc + git push |
| 5 | Auto-sync | Copy to Google Drive (if installed) |

---

## Execution

All steps execute automatically with confirmation checkpoints where needed:

- **Step 1:** Extracts learnings, asks "Apply these changes?"
- **Step 2:** Reviews skills, suggests improvements (optional)
- **Step 3:** Audits structure, asks "Reorganize?" (optional)
- **Step 4:** Generates handoff doc and pushes to GitHub
- **Step 5:** Auto-syncs to Google Drive if configured

---

## Output

✓ Skill improvements (if approved)  
✓ Structured handoff document (`.agents/handoff/YYYY-MM-DD-topic.md`)  
✓ GitHub commit + push  
✓ Google Drive sync (if installed)

---

## Tips

- **End of day recommended** — especially after creating/modifying skills
- **Optional** — run individual steps in any order
- **With retrospective** — skill improvements are optional
- **Triple backup** — document + GitHub + Google Drive
