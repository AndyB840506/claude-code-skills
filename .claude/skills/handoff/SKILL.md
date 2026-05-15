---
name: handoff
description: "Automatically generate session handoff document with accomplishments, pause point, and blockers. Copies to clipboard for easy pasting in next session + GitHub backup. Triggers: handoff, session handoff, write handoff, continue session, session notes, pause point, next session, where we stopped, backup session."
---

# Handoff — Session Summary + GitHub Backup

Automatically generates and copies a session summary to your clipboard — no file creation needed. Plus backs up all changes to GitHub.

**What it does:**
1. Analyzes recent git commits and file changes
2. Generates structured handoff document
3. Automatically copies to clipboard (Ctrl+V ready)
4. Displays the document in chat
5. Performs git add/commit/push to GitHub

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

✓ Handoff document automatically copied to clipboard  
✓ Full document displayed in chat  
✓ GitHub commit with hash  
✓ Ready to paste with Ctrl+V in next session

---

## See Also

- [Tips & Best Practices](docs/tips.md) — When to use, how to customize
- [Output Example](docs/example.md) — Real example of generated document
