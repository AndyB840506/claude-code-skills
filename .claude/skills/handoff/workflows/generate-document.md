# Workflow: Generate Document

Create the structured handoff markdown document.

## Structure

The document has a standard format for consistency:

```markdown
# Handoff: [TOPIC]

**Date:** YYYY-MM-DD  
**Status:** [Paused between tasks / Mid-task / Blocked on X]

---

## What We Accomplished This Session

### 1. [Accomplishment 1]
[Brief description of what was accomplished]

**Files changed:**
- `path/to/file.md` — What changed
- `path/to/another.md` — What changed

### 2. [Accomplishment 2]
[Brief description]

**Files changed:**
- `path/to/file.md` — What changed

---

## Where We Paused

[Clear description of the pause point]

**Last action:** [What was just done]  
**Next action:** [What should happen next]  
**Blockers (if any):** [Any blocking issues or decisions needed]

---

## Files to Read First

```
path/to/most-important-file.md
path/to/related-file.md
```

---

## Questions for Next Session

1. [Any open questions that need to be answered?]
```

## Content Guidelines

**Accomplishments:**
- Extract from recent git commits
- Group related commits under one accomplishment
- Keep descriptions brief but clear
- List all changed files for each accomplishment

**Where We Paused:**
- Write in natural language, not bullet points
- Be specific about the last action
- Be clear about what comes next
- If there are blockers, note them explicitly

**Files to Read First:**
- List 3-5 most important files from this session
- Include `.claude/` skill files if modified
- Include config files if changed
- Help the next session orient quickly

**Questions:**
- Optional — only if there are open questions
- Example: "Should we split this skill into 2 files?" or "Need decision on API approach"
