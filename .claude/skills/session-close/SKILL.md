---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Automated Complete Workflow

Automated 5-step workflow that executes automatically when invoked. No manual steps required.

**Execution sequence:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive Backup

---

## What It Does

Closes your session completely in one command. Executes all 5 steps automatically:

1. **Retrospective** — Extract learnings, propose skill updates
2. **Prompt Reviewer** — Review and improve updated skills  
3. **Skill Management** — Verify folder structure, suggest fixes
4. **Handoff** — Generate handoff document, create git commit + push
5. **Google Drive Backup** — Copy handoff to `G:\My Drive\claude projects`

All steps run sequentially. Each step completes before the next begins.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)  
✓ Handoff document created and backed up  
✓ Git commit made and pushed to GitHub  
✓ Handoff copied to Google Drive backup folder  
✓ Summary displayed with all changes

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up

---

## EXECUTION

Invokes `/session-close` to execute all 5 steps automatically.

**Steps 1-3:** User confirms approval prompts as each step completes.  
**Steps 4-5:** Run automatically without confirmation.

See [Execution Workflow](workflows/execute.md) for detailed step-by-step instructions.  
See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules.

