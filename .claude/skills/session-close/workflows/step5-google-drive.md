# Step 5 — Google Drive Backup Implementation

## Purpose

Automatically copy the handoff document created in Step 4 to `G:\My Drive\claude projects\` for cloud backup and sync.

## How It Works

After Step 4 creates the handoff file at `.agents/handoff/YYYY-MM-DD-topic.md`:

1. **Read the handoff file** from `.agents/handoff/` 
2. **Create a copy in Google Drive** using `mcp__claude_ai_Google_Drive__create_file`
3. **Target location:** `G:\My Drive\claude projects\handoff-[YYYY-MM-DD].md`
4. **Google Drive Desktop automatically syncs** the file to cloud (5-10 seconds)

## Implementation

When `/session-close` reaches Step 5:

```
Display: "Step 5: Backing up to Google Drive..."

Read handoff file from .agents/handoff/
  → Get filename and content

Use Google Drive tool to create file:
  - Title: "handoff-[date].md"
  - Parent folder: "G:\My Drive\claude projects\" (or find folder ID)
  - Content: Full markdown from handoff file
  - MIME type: "text/markdown"

Wait for sync (5-10 seconds)

Display: "✓ Handoff backed up to Google Drive"
```

## Key Points

- **No user confirmation needed** — runs automatically
- **Folder must exist** — `G:\My Drive\claude projects\` should be created beforehand
- **Google Drive Desktop handles sync** — no manual upload needed
- **File naming:** `handoff-[YYYY-MM-DD].md` for easy organization
- **Reversible** — file is just a copy; deleting it doesn't affect local handoff

## Error Handling

If backup fails:
- Display error: "⚠ Could not back up to Google Drive: [reason]"
- Show hint: "Check that `G:\My Drive\claude projects\` exists and is accessible"
- **Do NOT stop** — Step 4 completed successfully, backup is optional
- Continue and display session close summary

## Testing

To verify Step 5 works:
1. Check that `G:\My Drive\claude projects\` folder exists
2. Run `/session-close`
3. Confirm Steps 1-4 complete
4. Check `G:\My Drive\claude projects\` folder for new `handoff-[date].md` file
5. Verify Google Drive Desktop syncs the file to cloud
