# Execute Handoff — Implementation Workflow

When `/handoff` is invoked, Claude executes this workflow.

---

## Step 1: Analyze Recent Session

Gather information about what happened:

```bash
# Get last 5 commits
git log --oneline -5

# Get file statistics from last 5 commits  
git diff --stat HEAD~5

# Get the current topic from latest commit
git log -1 --format="%s"
```

From this, extract:
- **Topic:** The main theme (e.g., "bug-fixes", "skill-creation", "documentation")
- **Commits:** List of what was done
- **Files changed:** Which files were modified

---

## Step 2: Generate Handoff Document Content

Create structured markdown with:

```markdown
# Handoff: [TOPIC]

**Date:** YYYY-MM-DD  
**Status:** [Paused between tasks | Mid-task | Blocked on X]

---

## What We Accomplished This Session

### 1. [Accomplishment 1]
[Brief description]

**Files changed:**
- `path/to/file.md` — What changed

### 2. [Accomplishment 2]
[Brief description]

**Files changed:**
- `path/to/file.md` — What changed

---

## Where We Paused

[Clear description of pause point]

**Last action:** [What was just done]  
**Next action:** [What should happen next]  
**Blockers (if any):** [Any blocking issues]

---

## Files to Read First

```
path/to/important-file.md
path/to/related-file.md
```

---

## Questions for Next Session

1. [Any open questions?]
```

---

## Step 3: Copy to Clipboard & Display

Automatically copy the document to the user's clipboard, then display in chat:

```powershell
# Use PowerShell Set-Clipboard to copy document content
$content | Set-Clipboard
Write-Host "✓ Handoff copied to clipboard — ready to paste"
```

Display in chat:
```
✓ Handoff copied to clipboard:

---
[FULL DOCUMENT CONTENT HERE]
---

✓ Paste in new session with Ctrl+V
```

---

## Step 4: Perform GitHub Backup

```bash
# Stage all changes
git add -A

# Commit with timestamp
git commit -m "Session: [topic-slug] $(date +'%Y-%m-%d %H:%M:%S')"

# Push to remote
git push origin main

# Capture commit hash
git rev-parse HEAD
```

---

## Step 5: Show Confirmation

Display:
```
✓ Handoff copied to clipboard — ready to paste

✓ GitHub backup:
  Commit: [hash]
  Message: "Session: [topic] [timestamp]"
  
Status: Ready for next session
```

---

## Pseudo-Code (For Claude Implementation)

```
WHEN /handoff is invoked:

1. GET recent commits (git log --oneline -5)
2. GET file changes (git diff --stat HEAD~5)  
3. EXTRACT topic from latest commit message
4. GENERATE markdown document with:
   - Accomplishments from commits
   - Changed files from diff
   - Pause point (ask user or infer)
   - Files to read (from changed files)
5. COPY document to clipboard (PowerShell Set-Clipboard)
6. DISPLAY full document in chat
7. RUN git add -A && git commit && git push
8. SHOW commit hash and confirmation
```

---

## Key Points

✓ Document is **automatically generated** from git data  
✓ Document is **automatically copied to clipboard** — no manual copy needed  
✓ GitHub **backup is automatic** with every handoff  
✓ **Clipboard-first workflow** — no redundant files created  
✓ **Ready to paste** in next session with Ctrl+V for instant context
