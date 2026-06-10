# Session Close — Complete Execution Flow

When you invoke `/session-close`, Claude executes 3 steps in sequence. Steps 1-2 require your confirmation; Step 3 runs automatically.

---

## How Claude Executes `/session-close`

```
/session-close invoked by user
  ↓
Step 1: Invoke /retrospective
  Show learnings → [USER: confirm?] → continue
  ↓
Step 2: Audit the skill kit against skill-management's checklist
  Show audit issues → [USER: confirm?] → continue
  ↓
Step 3: Invoke /handoff (automatic)
  Write .agents/handoff/YYYY-MM-DD-<topic>.md
  git commit + push to GitHub
  Display handoff in chat
  ↓
DONE — session backed up to GitHub
```

---

## STEP 1: Retrospective (Show Results + Confirm)

Claude invokes `/retrospective` which scans the conversation for:
- Corrections to existing behavior
- Work that was redone or needed adjustment
- Patterns that worked well
- Missing steps in workflows

**Output:** List of 2-5 learnings with proposed skill updates

**Claude asks you:** "Apply these changes? (YES/NO)"

**Your response determines:** Whether to update skills or skip

**Then continues to Step 2**

---

## STEP 2: Skill Management Audit (Show Results + Confirm)

Claude audits the full skill kit directly, using the checklist in `skill-management/SKILL.md` as the rubric.

Audits the full skill kit for:
- Trigger overlaps between skills
- Duplicate content across skills
- Oversized SKILL.md files (>50 lines)
- Structure violations and missing steps

**Output:** Prioritized issue table (CRITICAL / HIGH / MEDIUM / NOTE)

**Claude asks you:** "Apply these fixes? (YES/NO)"

**Your response determines:** Whether to apply fixes or skip

**Then continues to Step 3**

---

## STEP 3: Handoff (Fully Automatic)

Claude invokes `/handoff` via `Skill("handoff")` tool call (NOT inline text generation) which automatically:

1. Analyzes the session from git history and conversation context
2. Generates structured handoff document and writes it to `.agents/handoff/YYYY-MM-DD-<topic>.md`:
   - **Date and topic** — When and what
   - **Accomplishments** — 3-5 bullet points of what was completed
   - **Files changed** — List of modified files
   - **Pause point** — Where to resume next session
   - **Next actions** — What should happen next
   - **Blockers** — Any issues preventing progress
3. Commits and pushes the file:
   ```powershell
   git add .agents/handoff/YYYY-MM-DD-<topic>.md
   git commit -m "handoff: <topic> YYYY-MM-DD"
   git push origin main
   ```
4. Displays the document in chat (so you can see what was created)

**Storage:**
- File: `.agents/handoff/YYYY-MM-DD-<topic>.md` in project repo
- GitHub: committed and pushed to origin/main
- Any machine with the repo cloned can pull and resume from this point

**No user confirmation needed.**

---

## Summary

| Step | User Action | What Claude Does |
|------|-------------|------------------|
| 1 | Confirm changes | Invoke /retrospective → update skills if approved |
| 2 | Confirm fixes | Audit kit against skill-management checklist → apply fixes if approved |
| 3 | None (automatic) | Invoke /handoff → write .agents/handoff/*.md, commit, push to GitHub |

---

## Timing & Expectations

- **Step 1:** 2-3 minutes (scans conversation)
- **Step 2:** 1-2 minutes (audits structure)
- **Step 3:** 1-2 minutes (generates handoff & commits)
- **Total:** ~5 minutes for complete session close

---

## What Gets Backed Up

**Git backup (GitHub — primary and only):**
- `.agents/handoff/YYYY-MM-DD-<topic>.md` committed and pushed
- Any machine with the repo cloned can pull and resume

**Config + memory backup:**
- Handled separately by `claude-bootstrap` (run its own sync when you want to push `~/.claude/` config/memory updates)

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| "No learnings found" | Short session or no corrections | Normal — skill continues to Step 3 |
| Step 3 fails | Git or GitHub issue | Check git status, verify GitHub connection |
| Whole sequence stuck | Skills not found | Ensure `/retrospective` exists |

---

## Next Session

1. **Open the project in VS Code** — CLAUDE.md auto-resume pulls the latest handoff from GitHub and asks if you want to continue
2. **Or read manually** — Check `.agents/handoff/` for the most recent `.md` file
