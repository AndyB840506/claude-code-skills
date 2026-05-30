# When to Use Session Close

Guidelines for when to run the complete session close workflow.

---

## Required: End of Major Sessions

Run full session-close when you've completed significant work:

- ✓ **After creating new skills** — Capture design patterns and decisions
- ✓ **After major refactoring** — Extract learnings from structural changes
- ✓ **After bug fixes** — Document the root cause and how it was solved
- ✓ **After feature implementation** — Preserve process improvements
- ✓ **After user feedback** — Update skills based on corrections

---

## Optional: During Long Sessions

Run individual steps without full closure:

- **After 2+ hours of work** — Run `/retrospective` to capture learnings mid-stream
- **When testing fails repeatedly** — Run `/skill-management` to check automation structure
- **When frustrated with a tool** — Run `/prompt-reviewer` on relevant skill docs

---

## NOT Recommended For

- ✗ Small fixes or typos (unnecessary overhead)
- ✗ Reading code or researching (no learnings to capture)
- ✗ One-off commands (not part of a workflow)
- ✗ Testing or debugging (capture learnings when done)

---

## Quick Decision Tree

```
Did I complete a multi-step workflow? → YES → Run /session-close
Did I create or modify a skill? → YES → Run /retrospective + /skill-management
Did I fix multiple bugs? → YES → Run /retrospective
Did I spend 30+ minutes on this? → YES → Consider running at least /retrospective
Otherwise → Skip for now, run at end of day
```

---

## Time Investment

- **Full run** (all 5 steps): ~10 minutes
- **Retrospective only**: ~3 minutes
- **Retrospective + Handoff**: ~5 minutes

---

## When to Batch

Instead of running after every small task:

- **Daily cadence** — Run once at end of day for all changes
- **Weekly cadence** — Run Friday evening for entire week of work
- **Project cadence** — Run when switching to new project

This saves context-switching overhead and groups related learnings.

---

## Success Looks Like

After session-close completes:
- ✓ Session learnings are documented in skill files
- ✓ Skills are reviewed and improved
- ✓ Folder structure is verified
- ✓ Handoff document created and pushed
- ✓ Google Drive backup complete
- ✓ Ready to hand off or continue next session
