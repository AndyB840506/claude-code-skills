---
name: session-close
description: "Automated 6-step session close: retrospective + prompt review + skill audit + handoff (writes .agents/handoff/*.md, commits, pushes to GitHub) + bootstrap sync. Triggers: session close, end session, closing session, session wrap-up, wrap up, end-of-session, cierre de sesión, cerrar sesión, finalizar sesión, terminar sesión, fin de sesión, cerrar proyecto, guardar y cerrar."
---

# Session Close — Automated Complete Workflow

Automated 6-step workflow. Steps 1-3 require user confirmation; Steps 4-6 run automatically.

**Execution sequence:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Bootstrap Sync

---

## What It Does

Closes your session completely in one command. Executes all 6 steps automatically:

1. **Retrospective** — Extract learnings, propose skill updates
2. **Prompt Reviewer** — Review and improve updated skills  
3. **Skill Management** — Full audit of the skill kit (redundancies, structure, circular flows)
4. **Handoff** — Write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub
5. **Bootstrap Sync** (Automatic) — Run `sync.ps1` in `claude-bootstrap` to push latest config + memory to GitHub

All steps run sequentially. Each step completes before the next begins.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)  
✓ Handoff document written to `.agents/handoff/YYYY-MM-DD-<topic>.md`  
✓ Handoff committed and pushed to GitHub  
✓ Bootstrap sync: latest config + memory pushed to `claude-bootstrap` repo

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

When `/session-close` is invoked, execute all 6 steps automatically:

1. Invoke `/retrospective` → ask user to confirm changes
2. Invoke `/prompt-reviewer` → ask user to confirm improvements  
3. Invoke `/skill-management` → it asks audit mode first (Modo A: kit completo / Modo B: skill individual) per its own Paso 0 — let that question surface, then show results and ask user to confirm fixes
4. Invoke `/handoff` → write `.agents/handoff/YYYY-MM-DD-<topic>.md`, commit, push to GitHub (automatic)
5. Run bootstrap sync (automatic):
   ```powershell
   Push-Location "$env:USERPROFILE\claude-bootstrap"; .\sync.ps1; Pop-Location
   ```
   Pushes latest config + memory to GitHub so any other machine can pull and resume.

**Steps 1-3:** Show results and wait for user confirmation.  
**Steps 4-6:** Run automatically without user prompts.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for implementation rules and error handling.

