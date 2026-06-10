# Immediate Handoff Workflow

Write handoff doc to a file, commit, and push so any machine can resume.

## Steps

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

## When No Session File Exists

If there is no `status: in-progress` session file, skip session-related steps and build
the handoff directly from conversation context. Do not block or ask the user to create
a session — just proceed with what's known.
