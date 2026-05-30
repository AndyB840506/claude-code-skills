---
name: session-close
description: "Automated 5-step session close: retrospective + prompt review + skill audit + handoff (to clipboard, no files) + Google Drive backup. Triggers: session close, end session, closing session, session wrap-up, wrap up, end-of-session, cierre de sesión, cerrar sesión, finalizar sesión, terminar sesión, fin de sesión, cerrar proyecto, guardar y cerrar."
---

# Session Close — Automated Complete Workflow

Automated 5-step workflow that executes automatically when invoked. No manual steps required.

**Execution sequence:** Retrospective → Prompt Reviewer → Skill Kit Auditor → Handoff → Google Drive Backup

---

## What It Does

Closes your session completely in one command. Executes all 5 steps automatically:

1. **Retrospective** — Extract learnings, propose skill updates
2. **Prompt Reviewer** — Review and improve updated skills  
3. **Skill Kit Auditor** — Full audit of the skill kit (redundancies, structure, circular flows)
4. **Handoff** — Generate handoff document, create git commit + push
5. **Google Drive Backup** (Optional) — Copy handoff to `G:\My Drive\claude projects` (if folder exists)

All steps run sequentially. Each step completes before the next begins.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)  
✓ Handoff document copied to clipboard (Ctrl+V ready)  
✓ Git commit made and pushed to GitHub  
⚠️ Google Drive backup (skipped if folder not accessible — no blocking error)  
✓ No files created — document stays in clipboard only

**Note:** Step 5 is optional. If you don't have Google Drive mounted, the handoff is still complete in the clipboard. To set up Google Drive backup: use Rclone or Google Drive File Stream to mount `G:\My Drive\`.

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up

---

## Auto-trigger via SessionEnd Hook

Instead of typing `/session-close` manually, you can configure Claude Code to trigger this skill automatically when any session ends. Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{ "type": "command", "command": "echo 'Session ended — run /session-close to close properly'" }]
    }]
  }
}
```

This fires a reminder at session end. If both `handoff` and `session-close` are in your kit, only configure one as a SessionEnd hook — they serve different purposes (handoff = context transfer, session-close = full workflow).

---

## EXECUTION

When `/session-close` is invoked, execute all 5 steps automatically:

1. Invoke `/retrospective` → ask user to confirm changes
2. Invoke `/prompt-reviewer` → ask user to confirm improvements  
3. Invoke `/skill-kit-auditor` → ask user to confirm fixes
4. Invoke `/handoff` → generate doc in memory → copy to clipboard → git commit (automatic)
5. Copy the handoff document to `G:\My Drive\claude projects\` using local file copy (automatic)

**Steps 1-3:** Show results and wait for user confirmation.  
**Steps 4-5:** Run automatically without user prompts.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.

