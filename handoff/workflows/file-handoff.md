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

5. **Commit and push** — use a **scoped add** and **pull --rebase before pushing**
   ```
   git add .agents/handoff/YYYY-MM-DD-<topic>.md   # scoped: only the handoff file
   git commit -m "handoff: <topic> YYYY-MM-DD"
   git pull --rebase origin main                   # integrate parallel work first
   git push origin main
   ```
   Use PowerShell on Windows, bash on Mac/Linux.
   - **Never `git add .` / `git add -A` here** — a broad add can absorb another
     parallel session's uncommitted changes into your commit (see Parallel sessions).
   - The `pull --rebase` makes a second session integrate instead of getting a
     non-fast-forward rejection. Handoff files have distinct names, so the rebase is clean.
   - If the rebase reports a real conflict (both sessions edited the same shared file,
     e.g. `MEMORY.md`), stop and resolve it with the user — do not force-push.

6. **Confirm**
   > Handoff saved to `.agents/handoff/YYYY-MM-DD-<topic>.md` — committed and pushed.
   > Resume on any machine: open this repo in VS Code, Claude will auto-resume from the handoff.

## Parallel sessions (avoid "crossed wires")

Andrés sometimes runs **two sessions at once** to keep unrelated work from confusing the
model. Two risks, and how this workflow handles them:

- **Handoff files do NOT overwrite each other** — each gets a distinct `YYYY-MM-DD-<topic>.md`.
  Just make sure the topic slug is specific to *this* session's work, not generic.
- **The real overwrite risk is two sessions sharing one working tree** — one session's
  broad `git add` captures the other's uncommitted edits into the wrong commit. Defenses:
  scoped `git add` (step 5), `git pull --rebase` before push (step 5), and ideally a
  **separate `git worktree` per session** so each has its own working directory.
- An agent **cannot close another running session** — sessions are isolated. To close both,
  the user runs `/session-close` in each. Sequencing them (finish one, let it push, then
  the other) lets the second rebase cleanly on the first.

## When No Session File Exists

If there is no `status: in-progress` session file, skip session-related steps and build
the handoff directly from conversation context. Do not block or ask the user to create
a session — just proceed with what's known.
