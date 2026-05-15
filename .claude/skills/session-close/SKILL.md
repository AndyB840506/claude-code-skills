---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Complete Closing Workflow

Automated 5-step workflow to close your session: analyze learnings, review skills, organize structure, and backup everything.

**Executes in order:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive Backup

---

## 5-Step Workflow

1. **Retrospective** → `/retrospective` — Extract learnings, propose skill updates
2. **Prompt Reviewer** → `/prompt-reviewer` — Review and improve updated skills (optional)
3. **Skill Management** → `/skill-management` — Verify folder structure, suggest fixes (optional)
4. **Handoff** → `/handoff` — Generate handoff document, create git commit + push
5. **Google Drive Backup** — Automatic via Desktop app (Step 4 handoff syncs)

Steps 1-3 are independent (skip/rerun as needed). Steps 4-5 run sequentially.

See [Full Workflow](workflows/execute.md) for detailed step-by-step execution.

---

## Output

✓ Skill improvements (if approved)  
✓ Handoff document copied to clipboard (Ctrl+V to paste in next session)  
✓ Backup to GitHub (automatic)  
✓ Backup to Google Drive (Step 5, manual copy to `G:\My Drive\claude projects`)

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up
- **Optional during long sessions** — run individual steps mid-stream

---

## EXECUTION

See [Execution Workflow](workflows/execute.md) for detailed step-by-step instructions.

