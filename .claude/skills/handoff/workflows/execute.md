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

## Step 3: Display Document in Chat (PRIMARY — always do this)

Show the complete handoff document as a markdown code block in the conversation.
This is the reliable delivery method — clipboard may silently fail in Claude's subprocess.

## Step 4: Clipboard Copy via Temp File (REQUIRED — use this exact pattern)

Write handoff to temp file first, then read and copy via WinForms.
This avoids two failure modes: `$var | clip` (silent fail) and here-strings with path-like
strings (trigger Claude Code security hooks that block execution).

```powershell
# Step A: Write tool writes the handoff to temp file (no PowerShell needed for this part)
# File: C:\Users\andre\AppData\Local\Temp\_handoff.txt

# Step B: PowerShell reads and copies via WinForms
Add-Type -AssemblyName System.Windows.Forms
$text = Get-Content "C:\Users\andre\AppData\Local\Temp\_handoff.txt" -Raw
[System.Windows.Forms.Clipboard]::SetText($text)
$verify = [System.Windows.Forms.Clipboard]::GetText()
if ($verify.Length -gt 50) { Write-Host "OK — $($verify.Length) chars en clipboard" } else { Write-Host "FALLO" }
```

NEVER use: `$var | clip` (silently fails), here-strings with slash-paths (trigger security hooks).

## Step 5: GitHub Backup (Automatic)

Create git commit with session data:
```bash
git add -A
git commit -m "Session: [topic] YYYY-MM-DD HH:MM:SS"
git push origin main
```

---

**Handoff complete!** Document copied to clipboard and backed up to GitHub. Ready to paste in next session.
