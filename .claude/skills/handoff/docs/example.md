# Output Example

This is what a generated handoff document looks like.

---

```
✓ Handoff document created:
  File: .agents/handoff/2026-05-14-bug-fixes.md
  
[Full document content below — copy for next session]

---

# Handoff: Bug Fixes

**Date:** 2026-05-14  
**Status:** Between tasks — ready to continue

## What We Accomplished This Session

### 1. Fixed retrospective skill not triggering
- Moved files from loose .md to folder structure
- All 13 skills now discoverable
- File: .claude/skills/retrospective/SKILL.md

### 2. Clarified auto-compact configuration
- Updated .claude/settings.json
- Added instructions to CLAUDE.md
- Context now compacts at 50% threshold

**Files changed (last 5):**
- .claude/settings.json
- .claude/skills/session-close/SKILL.md
- CLAUDE.md

## Where We Paused

Session complete. All skills working, backups current.

**Last action:** Ran session-close workflow  
**Next action:** Continue development (no blockers)

## Files to Read First

```
.claude/skills/session-close/SKILL.md
.claude/settings.json
```

---

✓ GitHub backup:
  Commit: c8cec62
  Message: "Session: bug-fixes 2026-05-14 20:34"
  
Status: Ready for next session
```

---

## What to Do with This

1. **Copy the entire document** (from the lines between the dashes)
2. **At the start of next session,** paste it in the chat message to restore context
3. **Edit it if needed** — add notes, update blockers, clarify decisions

This gives the next session instant context about what was done and what's next.
