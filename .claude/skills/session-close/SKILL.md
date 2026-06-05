---
name: session-close
description: "Automated 5-step session close: retrospective + prompt review + full kit audit (18 criteria, redundancies, circular flows) + handoff (to clipboard, no files) + Google Drive backup. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Automated Complete Workflow

Automated 5-step workflow that executes automatically when invoked. No manual steps required.

**Execution sequence:** Retrospective → Prompt Reviewer → Skill Kit Auditor → Handoff → Google Drive Backup

---

## What It Does

Closes your session completely in one command. Executes all 5 steps automatically:

1. **Retrospective** — Extract learnings, propose skill updates
2. **Prompt Reviewer** — Review and improve updated skills  
3. **Skill Kit Auditor** — Verify folder structure, suggest fixes
4. **Handoff** — Generate handoff document, create git commit + push
5. **Google Drive Backup** — Copy handoff to `G:\My Drive\claude projects`

All steps run sequentially. Each step completes before the next begins.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)  
✓ Handoff document copied to clipboard (Ctrl+V ready)  
✓ Git commit made and pushed to GitHub  
✓ Optional: Handoff backed up to Google Drive (if folder exists)  
✓ No files created — document stays in clipboard only

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up

---

## EXECUTION

When `/session-close` is invoked, execute all 5 steps automatically:

1. Invoke `/retrospective` → ask user to confirm changes
2. Invoke `/prompt-reviewer` → ask user to confirm improvements  
3. Invoke `/skill-kit-auditor` → el auditor mostrará su alerta de orden de ejecución. Responde "Sí" cuando aparezca (el /retrospective ya corrió en el Paso 1). Pedir confirmación al usuario para los cambios de reorganización.
4. Invoke `/handoff` → generate doc in memory → copy to clipboard → git commit (automatic)
5. Copy the handoff document to `G:\My Drive\claude projects\` using local file copy (automatic)

**Steps 1-3:** Show results and wait for user confirmation.  
**Steps 4-5:** Run automatically without user prompts.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.

---

## Auto-trigger via SessionEnd Hook

Configure in `~/.claude/settings.json` to prompt automatically at session end:

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{ "type": "command", "command": "echo 'Session ended — run /session-close'" }]
    }]
  }
}
```

**Note:** Do NOT also configure `/retrospective` or `/handoff` as `SessionEnd` hooks — `session-close` already invokes both. Configuring all three creates duplication.

