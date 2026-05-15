---
name: handoff
description: "Automatically generate session handoff document with accomplishments, pause point, and blockers + GitHub backup. Creates copiable summary for next session. Output: .agents/handoff/YYYY-MM-DD-topic.md + git commit + push. Triggers: handoff, session handoff, write handoff, continue session, session notes, pause point, next session, where we stopped, backup session."
---

# Handoff — Session Summary + GitHub Backup

Automatically generates a copiable summary of what you accomplished, where you paused, and what's next — plus backs up to GitHub.

**What it does:**
1. Analyzes recent git commits and file changes
2. Generates structured handoff document
3. Saves to `.agents/handoff/YYYY-MM-DD-topic.md`
4. Performs git add/commit/push to GitHub
5. Displays the document for you to copy/paste into next session

---

## Quick Start

Simply invoke:

```
/handoff
```

Or with a custom topic:

```
/handoff my-topic
```

---

## Workflows

1. **execute-handoff** — The 5-step automatic execution flow
2. **generate-document** — Document template and structure

---

## Output

✓ Handoff document: `.agents/handoff/YYYY-MM-DD-topic.md`  
✓ GitHub commit with hash  
✓ Full document displayed in chat for copy/paste

---

## See Also

- [Tips & Best Practices](docs/tips.md) — When to use, how to customize
- [Output Example](docs/example.md) — Real example of generated document
