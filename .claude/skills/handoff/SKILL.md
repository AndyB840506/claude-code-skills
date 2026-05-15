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

1. **execute-handoff** — The 5-step automatic execution flow
2. **generate-document** — Document template and structure

---

## Output

✓ Handoff document automatically copied to clipboard  
✓ Full document displayed in chat  
✓ Ready to paste with Ctrl+V in next session  
✓ No file creation, no git operations

---

## See Also

- [Tips & Best Practices](docs/tips.md) — When to use, how to customize
- [Output Example](docs/example.md) — Real example of generated document

---

## EXECUTION

You have invoked `/handoff`. Now generate and copy the handoff document.

### Step 1: Analyze Recent Session

Gather information from git:
```bash
git log --oneline -5
git diff --stat HEAD~5
git log -1 --format="%s"
```

Extract: topic (from latest commit), what was accomplished, files changed.

### Step 2: Generate Handoff Document

Create structured markdown containing:
- **Date and topic** — When and what
- **Accomplishments** — 3-5 bullet points of what was completed
- **Files changed** — List of modified files with brief descriptions
- **Pause point** — Where to resume next session
- **Next actions** — What should happen next
- **Blockers (if any)** — Any issues preventing progress
- **Files to read** — Important files to review in next session

### Step 3: Copy to Clipboard

Automatically copy the complete document to clipboard using:
```powershell
$content | Set-Clipboard
```

Result: Document is ready to paste with Ctrl+V in next session.

### Step 4: Display Document in Chat

Show the complete generated handoff document in chat so user can see what was created.

### Step 5: GitHub Backup (Automatic)

Create git commit with session data:
```bash
git add -A
git commit -m "Session: [topic] YYYY-MM-DD HH:MM:SS"
git push origin main
```

---

**Handoff complete!** Document copied to clipboard and backed up to GitHub. Ready to paste in next session.
