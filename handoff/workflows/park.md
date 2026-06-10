# Park Workflow

Update session Progress only. No file, no push. The session file IS the handoff for
later resumption.

## Why This Works

The session already has Goal, Context, Progress, Definition of Done. A separate
handoff artifact duplicates this = two sources of truth = one goes stale. Use Park
only when you plan to resume in the same machine/session context without needing
cross-machine continuity.

## Progress Entry Format

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

## Steps

1. **Find the active session** - Check for `status: in-progress` session worked on in this conversation.

2. **Update session Progress section** - Append a new entry using the Progress Entry Format above. Factual, not verbose.

3. **Capture user's direction** - If user gave specific intention for next session, put that first in Next.

4. **Confirm:**
   > Session updated: `Notes/Sessions/YYYY-MM-DD-HHMM-Title.md`
   > To resume: reopen the session when ready.
