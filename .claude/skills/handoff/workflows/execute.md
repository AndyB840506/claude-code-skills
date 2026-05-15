# Handoff Execution Workflow

You have invoked `/handoff`. Now generate and copy the handoff document.

## Step 1: Analyze Recent Session

Gather information from git:
```bash
git log --oneline -5
git diff --stat HEAD~5
git log -1 --format="%s"
```

Extract: topic (from latest commit), what was accomplished, files changed.

## Step 2: Generate Handoff Document

Create structured markdown containing:
- **Date and topic** — When and what
- **Accomplishments** — 3-5 bullet points of what was completed
- **Files changed** — List of modified files with brief descriptions
- **Pause point** — Where to resume next session
- **Next actions** — What should happen next
- **Blockers (if any)** — Any issues preventing progress
- **Files to read** — Important files to review in next session

## Step 3: Copy to Clipboard

Automatically copy the complete document to clipboard using:
```powershell
$content | Set-Clipboard
```

Result: Document is ready to paste with Ctrl+V in next session.

## Step 4: Display Document in Chat

Show the complete generated handoff document in chat so user can see what was created.

## Step 5: GitHub Backup (Automatic)

Create git commit with session data:
```bash
git add -A
git commit -m "Session: [topic] YYYY-MM-DD HH:MM:SS"
git push origin main
```

---

**Handoff complete!** Document copied to clipboard and backed up to GitHub. Ready to paste in next session.
