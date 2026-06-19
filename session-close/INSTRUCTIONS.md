# Session Close — Implementation Instructions

This document defines how `/session-close` executes its 3 steps.

## Execution Sequence

```
STEP 1: Invoke /retrospective
  → User confirms: "Apply these changes?" YES/NO
  → Continue to STEP 2

STEP 2: Audit the skill kit against skill-management's checklist
  → User confirms: "Apply fixes?" YES/NO
  → Continue to STEP 3

STEP 3: Invoke /handoff via Skill("handoff") tool call — NEVER generate handoff content inline as text
  → Writes .agents/handoff/YYYY-MM-DD-<topic>.md, commits, pushes to origin/main
  → No user confirmation needed
  → Display the document in chat
```

## Implementation Rules

1. **Steps 1-2 require user approval** — show results and ask for confirmation before applying any edits
2. **Step 3 runs automatically** — write, commit, push, then display; no prompt needed
3. **Each step completes before the next starts** — do not run in parallel
4. **All changes are reversible** — everything goes through git
5. **CRITICAL: Step 3 must use the Skill tool** — call `Skill("handoff")`. Never write handoff content inline as text output; that bypasses the skill's git logic.

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
2. Confirm all 3 steps execute in order
3. Verify approval prompts appear for Steps 1-2
4. Verify Step 3 runs without a prompt
5. **CRITICAL:** Verify `.agents/handoff/YYYY-MM-DD-<topic>.md` was created in the repo
6. **CRITICAL:** Verify git commit and push succeeded (`git log -1`)
7. Verify git commit message uses the `handoff: <topic> YYYY-MM-DD` format
