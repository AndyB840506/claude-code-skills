---
name: handoff
description: "Automatically generate session handoff document with accomplishments, pause point, and blockers. Copies to clipboard for easy pasting in next session + GitHub backup. Triggers: handoff, session handoff, write handoff, continue session, session notes, pause point, next session, where we stopped, backup session."
---

# Handoff — Session Summary to Clipboard

Automatically generates a session summary and copies it to your clipboard — ready to paste with Ctrl+V in next session. No file creation, no git commits.

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

You have invoked `/handoff`. Now generate the session handoff document.

### Step 1: Analyze Session

Analyze the conversation transcript and git history:

**From Conversation:**
- What was accomplished in this session?
- What was the main goal or topic?
- Were there any blockers or issues?
- What's the pause point for next session?
- Key decisions made?

**From Git:**
- Recent commits (last 1-5 commits)
- Files changed in this session
- Branch name (if working on feature branch)
- Any uncommitted changes?

### Step 2: Extract Session Details

Identify and extract:

**Session Topic:**
- One-line summary of what was worked on

**Accomplishments:**
- 3-5 bullet points of completed work
- Focus on outcomes, not activities
- Example: "Reorganized 11 skills into self-contained folder structure"

**Files Changed:**
- List of files modified/created this session
- Include line counts if significant

**Pause Point:**
- Where should next session pick up?
- What's the next logical step?
- Any open decisions?

**Blockers/Issues:**
- Anything preventing progress?
- Questions that need answering?
- Known issues to address next?

### Step 3: Generate Document

Create a structured handoff document with:

**Structure:**
- Date and session topic
- Accomplishments (3-5 bullet points)
- Key learnings
- Files changed
- Pause point for next session
- Blockers (if any)

**Content:**
Focus on outcomes, not activities. Include what changed and why.

### Step 4: Copy to Clipboard

Automatically copy the complete document to clipboard so user can:
- Paste it into next session's message with Ctrl+V
- Save it to their notes/wiki if needed
- Share it with team members

**That's it.** No file creation. No git operations.

### Step 5: Display Document

Show the generated document in chat:

> **Handoff document generated!**
>
> ✓ Copied to clipboard (Ctrl+V ready)
> ✓ Paste this into next session to pick up where you left off
>
> [Full document content displayed]

---

**Handoff complete!** Ready to paste in next session.
