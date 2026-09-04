# Session Close — Implementation Instructions

This document defines how `/session-close` executes its 6 steps.

## Execution Sequence

```
STEP 1: Invoke /retrospective
  → Reconciliar los prompts/reglas que el usuario pegó en la sesión (ver abajo)
  → User confirms: "Apply these changes?" YES/NO
  → Continue to STEP 2

STEP 2: Audit the skill kit against skill-management's checklist
  → User confirms: "Apply fixes?" YES/NO
  → Continue to STEP 3

STEP 3: Invoke /handoff via Skill("handoff") tool call — NEVER generate handoff content inline as text
  → Writes .agents/handoff/YYYY-MM-DD-<topic>.md, commits, pushes to origin/main
  → No user confirmation needed
  → Display the document in chat
  → Continue to STEP 4

STEP 4: Skills repo sync. NOTE: `~/.claude/skills` and this project's own repo root
        (kit-skill-creator) are two separate clones of the SAME remote
        (github.com/AndyB840506/claude-code-skills) — confirmed 2026-09-04, both list
        the identical top-level skill folders (session-close/, handoff/, comfyui/...).
        Step 3's handoff commit does NOT cover this: it uses a scoped `git add` on only
        the handoff file, by design (see file-handoff.md's parallel-sessions warning),
        so any skill edited THIS session — in either clone — still needs its own
        commit+push here. (Gap found 2026-09-04: a whole new skill, linkedin-liderazgo,
        written straight into ~/.claude/skills, sat uncommitted through what would have
        been a full close until this step was added.)
  → cd "$env:USERPROFILE\.claude\skills"
  → git pull --rebase origin main   (the project repo may have just pushed via Step 3 —
    integrate that first so this push doesn't get rejected as non-fast-forward)
  → git status --short
  → If dirty: git add -A; git commit -m "session-close: skill updates <date>"; git push origin main
  → If clean: report "sin cambios"
  → No user confirmation needed — same trust level as Step 3 (skill edits already happened
    with approval earlier in the session; this only commits what's already on disk)
  → If this session's skill edits were made in THIS project's own repo root instead of
    ~/.claude/skills (both are valid places per skill-management's storage rule), also
    pull there afterward so the two clones stay in sync — don't leave the other one stale.
  → Continue to STEP 5

STEP 5: Run the claude-continuity sync (backs up ~/.claude memory + config)
  → Windows: cd "C:\Users\andre\repos\claude-continuity"; .\sync.ps1
  → Mac/Linux: cd <repo path> && bash sync.sh
  → No user confirmation needed — it only copies ~/.claude state and pushes
  → Report which memory folders synced (or "nothing changed")

STEP 6: Memory + skill-kit audit check
  → Count *.md files in C:\Users\andre\.claude\projects\<workspace>\memory\ (exclude MEMORY.md)
  → Count SKILL.md files via Glob "**/SKILL.md" in c:\Users\andre\.claude\skills
  → Read memory\.audit-baseline.json for lastAuditFileCount/lastSkillCount (if missing,
    create it with current counts and skip the trigger this time — nothing to compare yet)
  → If (current memory count - lastAuditFileCount) >= 15 OR (current skill count !=
    lastSkillCount): invoke Skill("memory-audit") now, no confirmation prompt to trigger
    it (memory-audit gates its own apply step; now also scans skill files for corruption)
  → Otherwise: report "Memoria: N archivos (+M), Skills: K archivos (umbral: memoria +15
    o cambio en K)"
  → No user confirmation needed for this step itself
```

## Step 1 — Reconciliar los prompts pegados en la sesión

Si el usuario pegó reglas o prompts a lo largo de la sesión, reconciliar **ANTES de seguir**:
producir una tabla `lo que pegó | dónde quedó en disco | en qué difiere del texto original`.
Leerla **de los archivos, no de memoria**.

Una sesión larga con pastes secuenciales pierde el rastro: el 2026-07-23 el usuario tuvo que
preguntar "¿aplicamos todos los prompts?" — de 12, uno se había ejecutado como tarea sin quedar
nunca escrito como regla, y 4 habían quedado con texto materialmente distinto al pegado.

## Implementation Rules

1. **Steps 1-2 require user approval** — show results and ask for confirmation before applying any edits
2. **Steps 3-6 run automatically** — no prompt needed (Step 3 writes/commits/pushes the handoff; Step 4 commits/pushes ~/.claude/skills; Step 5 syncs ~/.claude memory+config to GitHub)
3. **Each step completes before the next starts** — do not run in parallel
4. **All changes are reversible** — everything goes through git
5. **CRITICAL: Step 3 must use the Skill tool** — call `Skill("handoff")`. Never write handoff content inline as text output; that bypasses the skill's git logic.
6. **Steps 4-5 back up what Step 3 does NOT** — `~/.claude/skills` (this may share a remote with the current project repo, as two clones, but Step 3's scoped `git add` never commits skill files from either) and `~/.claude/` memory+config (a fully separate repo, `claude-continuity`). Skipping either leaves that state unbacked up. See [[feedback_always_backup_github]].

## User Prompts

**Step 1 Prompt:**
```
Found X learnings. Apply these changes? (YES/NO)
```

**Step 2 Prompt:**
```
Found Y issues in the skill kit. Apply fixes? (YES/NO)
```

**Step 3 Output:**
```
Step 3: Creating handoff document... done

Session closed successfully.
```

## Error Handling

**For Steps 1-2:**
- If skill invocation fails: show error, ask user to retry or skip
- User can choose YES/NO even if results are unclear

**For Step 3:**
- Writes `.agents/handoff/YYYY-MM-DD-<topic>.md`, commits, and pushes to origin/main
- If git commit/push fails: display error but continue (handoff file is still written to disk)
- Confirm: "Handoff saved to .agents/handoff/..., pushed to GitHub"

**For Step 4:**
- `~/.claude/skills` is a separate git repo (`claude-code-skills`) from both the project repo (Step 3) and `claude-continuity` (Step 5) — don't confuse the three.
- If `git status --short` is empty: report "sin cambios", continue — not an error.
- If commit/push fails (no network, auth): report the error but continue to Step 5 — the local commit (if it succeeded) still protects the work; only the push needs a retry later.
- Confirm: "Skills repo: <N> skill(s) commiteados y pusheados" or "Skills repo: sin cambios."

**For Step 5:**
- `sync.ps1`/`sync.sh` must be run from the `claude-continuity` repo root (it uses relative paths). The script handles its own `git add`/commit/push to `origin master`.
- If the repo isn't cloned or `local-settings.json` is missing, the script prints a hint to run `install.ps1` first — relay it, don't fail the whole close.
- If push fails (no network): the memory copy + local commit still happened; report it and tell the user to re-run `sync.ps1` when back online.
- Confirm: "Continuity sync: backed up <N> memory folders + config to GitHub."

**For Step 6:**
- If `memory\.audit-baseline.json` doesn't exist yet: create it with the current file
  count and skip the trigger this time (no baseline to compare against, not a failure)
- If `Skill("memory-audit")` invocation fails: report the error, do not fail the whole
  close — the check itself already ran and reported the count
- Confirm: "Memoria: N archivos (+M desde la última auditoría)" — plus "memory-audit
  disparado" if the threshold was crossed

**General:**
- All git commits succeed or fail atomically (can be retried)
- All skill updates are reversible via git
- User can always retry the entire `/session-close` from the start

## Storage

- File: `.agents/handoff/YYYY-MM-DD-<topic>.md` written to project repo
- Git: committed and pushed to origin/main (automatic)
- Any machine with the repo cloned can pull and resume from this point

## Git Commit Syntax (PowerShell)

In Windows PowerShell 5.1, use single-quoted here-strings for multi-line commit messages.
The closing `'@` must be at column 0 (no leading whitespace):

```powershell
git commit -m @'
First line summary

Body line.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
'@
```

Do NOT use Bash-style heredoc (`<<'EOF'`) — it fails in PowerShell 5.1.

## Testing

To verify implementation:
1. Invoke `/session-close` in a test session
2. Confirm all 6 steps execute in order
3. Verify approval prompts appear for Steps 1-2
4. Verify Step 3 runs without a prompt
5. **CRITICAL:** Verify `.agents/handoff/YYYY-MM-DD-<topic>.md` was created in the repo
6. **CRITICAL:** Verify git commit and push succeeded (`git log -1`)
7. Verify git commit message uses the `handoff: <topic> YYYY-MM-DD` format
8. **CRITICAL:** Verify Step 4 runs without a prompt and, if `~/.claude/skills` had
   uncommitted changes, that `git -C ~/.claude/skills log -1` shows the new commit
9. Verify Step 6 runs without a prompt and reports the memory file count
10. Verify `Skill("memory-audit")` actually fires (not just a printed suggestion) when
    the count grown since `.audit-baseline.json` is ≥15
