---
name: handoff
description: "Automatically generate session handoff document with accomplishments, pause point, and blockers. Copies to clipboard for easy pasting in next session. Creates git commit + automatic GitHub backup. Triggers: handoff, session handoff, write handoff, continue session, session notes, pause point, next session, where we stopped, backup session."
---

# Handoff — Session Summary to Clipboard

Automatically generates a session summary and copies it to your clipboard — ready to paste with Ctrl+V in next session. Creates git commit + GitHub backup automatically.

**What it does:**
1. Analyzes recent git commits and file changes
2. Generates structured handoff document
3. Automatically copies to clipboard (Ctrl+V ready)
4. Displays the document in chat
5. Done — ready for next session

---

## Quick Start

Simply invoke:

```
/handoff
```

The summary is copied to your clipboard. Paste it with **Ctrl+V** at the start of your next session to pick up exactly where you left off.

Or with a custom topic (brief, kebab-case):

```
/handoff skill-execution-fix
/handoff documentation-overhaul
/handoff bug-fixes-session
```

---

## Workflows

1. **execute** — The 5-step automatic execution flow
2. **generate-document** — Document template and structure

---

## Output

✓ Handoff document automatically copied to clipboard  
✓ Full document displayed in chat  
✓ Ready to paste with Ctrl+V in next session  
✓ GitHub backup created (automatic)  
✓ Optional: Copy the generated `report-[name]-[date].md` to `G:\My Drive\claude projects` for Google Drive sync

---

## See Also

- [Tips & Best Practices](docs/tips.md) — When to use, how to customize
- [Output Example](docs/example.md) — Real example of generated document

---

## EXECUTION

See [Execution Workflow](workflows/execute.md) for detailed step-by-step instructions.
