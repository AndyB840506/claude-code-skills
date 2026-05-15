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

Create a structured handoff document in `.agents/handoff/YYYY-MM-DD-topic.md`:

```markdown
---
date: 2026-05-14
session-topic: Skills folder reorganization
---

# Session: Skills folder reorganization

## Accomplishments
- ✓ Reorganized 11 skills into self-contained folders
- ✓ Added execution sections to all dependent skills
- ✓ Created comprehensive documentation for session-close
- ✓ All skills now have proper structure (SKILL.md + workflows/ + docs/)
- ✓ Committed to GitHub

## Files Changed
- .claude/skills/session-close/SKILL.md (added EXECUTION section)
- .claude/skills/retrospective/SKILL.md (added EXECUTION section)
- .claude/skills/prompt-reviewer/SKILL.md (added EXECUTION section)
- .claude/skills/skill-management/SKILL.md (added EXECUTION section)
- .claude/skills/handoff/SKILL.md (added EXECUTION section)
- New docs: workflow-overview.md, when-to-use.md, what-to-expect.md

## Pause Point
Session-close skill is now fully executable. Next session can:
1. Test the complete workflow end-to-end
2. Fine-tune the skill based on real usage
3. Work on new features or improvements

## Blockers
None identified. All skills functional.
```

### Step 4: Copy to Clipboard

Automatically copy the document content to clipboard so user can Ctrl+V paste it.

### Step 5: Git Commit and Push

Execute git operations:

```bash
git add .
git commit -m "Session: session-topic YYYY-MM-DD HH:MM:SS

[Session accomplishments from document]"

git push
```

Expected output:
```
[main abc1234] Session: session-topic 2026-05-14 18:30:00
X files changed, Y insertions(+), Z deletions(-)
```

### Step 6: Display Document

Show the generated document in chat with confirmation:

> **Handoff document created!**
>
> ✓ Saved to: `.agents/handoff/2026-05-14-topic.md`
> ✓ Copied to clipboard (Ctrl+V ready)
> ✓ Committed and pushed to GitHub
>
> [Full document content displayed]

---

**Handoff complete!** Session documented, committed, and backed up.
