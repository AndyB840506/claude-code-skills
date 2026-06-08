---
name: handoff
description: >
  Transfer work context between agent sessions without losing progress.
  Use when switching to a new session mid-task, parking work to resume
  later, or creating a persistent handoff committed to GitHub. Triggers:
  transfer context, park session, guardar contexto, transferir sesión,
  next session, continue in new session, retomar sesión, pasar contexto,
  park work, resume later. NOT for end-of-session close — use session-close
  for that.
---

# Handoff Skill

Transfer work context between agent sessions without losing progress.
Handoff files are committed and pushed to GitHub so any machine where
the repo is cloned can resume from exactly this point.

## Workflow Routing

| Command | Mode |
|---|---|
| `/handoff` | File: write handoff doc, commit, push to GitHub |
| `/handoff park` | Park: update session Progress only, no file, no push |

## Key Rules

Follow these steps in order:
1. **Update docs first** - the vault/project is the source of truth
2. **User's direction > agent's analysis** - if user said what to focus on next, that's the priority. Supplement with agent analysis only if user direction is incomplete
3. **Scan for pending markers before Next Steps** - grep for `USER-COMMENT`, `NEEDS USER INPUT`, `[TODO]`, `FIXME` in active session files. Every marker found must appear explicitly in Next Steps with where it lives, what's being asked, and who must act
4. **Verificar estado real al retomar** — Al iniciar sesión con handoff, preguntar explícitamente: "¿Alguno de los next steps del handoff ya fue completado?" El handoff captura el estado al momento de escribirse. No asumir que los Next Steps siguen pendientes.

## Immediate Handoff Workflow

Write handoff doc to a file, commit, and push so any machine can resume.

### Steps

1. **Get repo root**
   ```
   git rev-parse --show-toplevel
   ```
   Use that path for the file. If not in a git repo, write to the current directory.

2. **Determine topic slug** — 2-4 words from the session's main topic, kebab-case.
   Example: `ep017-guion`, `bootstrap-deploy`, `handoff-skill-redesign`

3. **Scan for pending markers** before drafting Next Steps:
   - Search active project files for `USER-COMMENT`, `NEEDS USER INPUT`, `[TODO]`, `FIXME`
   - Note: ignore markers inside `.claude/skills/` files — only flag project files

4. **Write the handoff file** to `<repo-root>/.agents/handoff/YYYY-MM-DD-<topic>.md`

   Format:
   ```markdown
   # Handoff: <Title>
   **Date:** YYYY-MM-DD
   **Status:** Complete | In progress — [one-line state]
   ---
   ## What We Accomplished This Session
   - [concrete bullet points — what was built/changed/decided]

   ## Where We Paused
   **Last action:** [the very last thing done]
   **Next action:** [first thing to do on resume]
   **Blockers:** [anything waiting on user, external system, or unclear]

   ## Files to Read First
   - `path/to/file.md` — why it matters

   ## Notes / Gotchas
   - [non-obvious constraints, decisions, or surprises discovered]

   ## Questions to Answer
   - [open items that need resolution]
   ```

5. **Commit and push**
   ```
   git add .agents/handoff/YYYY-MM-DD-<topic>.md
   git commit -m "handoff: <topic> YYYY-MM-DD"
   git push origin main
   ```
   Use PowerShell on Windows, bash on Mac/Linux.

6. **Confirm**
   > Handoff saved to `.agents/handoff/YYYY-MM-DD-<topic>.md` — committed and pushed.
   > Resume on any machine: open this repo in VS Code, Claude will auto-resume from the handoff.

## Park Workflow

Update session Progress only. No file, no push. The session file IS the handoff for later resumption.

### Why This Works

The session already has Goal, Context, Progress, Definition of Done. A separate handoff artifact duplicates this = two sources of truth = one goes stale. Use Park only when you plan to resume in the same machine/session context without needing cross-machine continuity.

### Progress Entry Format

```markdown
### YYYY-MM-DD (parked)
**Done:** What was accomplished. Concrete, not vague.
**Learned:**
- Gotchas, constraints, decisions discovered during work
**Stopped at:** Exactly where work paused.
**Next:**
1. First thing to do when resuming
2. Second action
**Files:**
- `path/to/file.md` - what it is
```

### Steps

1. **Find the active session** - Check for `status: in-progress` session worked on in this conversation.

2. **Update session Progress section** - Append a new entry using the Progress Entry Format above. Factual, not verbose.

3. **Capture user's direction** - If user gave specific intention for next session, put that first in Next.

4. **Confirm:**
   > Session updated: `Notes/Sessions/YYYY-MM-DD-HHMM-Title.md`
   > To resume: reopen the session when ready.

## When No Session File Exists

If there is no `status: in-progress` session file, skip session-related steps and build the handoff directly from conversation context. Do not block or ask the user to create a session — just proceed with what's known.

## Auto-trigger via SessionEnd Hook

`handoff` can be configured to remind you automatically when a session ends. Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{ "type": "command", "command": "echo 'Session ended — run /handoff to transfer context'" }]
    }]
  }
}
```

**Note:** If you also use `session-close`, configure only one as a `SessionEnd` hook — `session-close` already invokes `handoff` as its step 4, so configuring both creates duplication.
