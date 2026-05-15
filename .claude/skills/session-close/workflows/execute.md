# Step-by-Step Session Close Execution

Execute the 5-step workflow in order. Each step builds on the previous one.

---

## Step 1: Extract Learnings (Retrospective)

```
/retrospective
```

**What to expect:**
- Claude analyzes the session for learnings, corrections, and redone work
- Proposes skill updates
- Asks "Apply these changes?" if updates found
- User confirms or skips

**Output:** Updated skill files (if approved)

---

## Step 2: Review Skills (Prompt Reviewer)

```
/prompt-reviewer
```

**What to expect:**
- Reviews the skills that were potentially updated
- Checks for clarity, completeness, effectiveness
- Proposes improvements (optional)
- Asks for confirmation before applying

**Output:** Improved skill documentation (if approved)

---

## Step 3: Organize Structure (Skill Management)

```
/skill-management
```

**What to expect:**
- Audits skill folder structure
- Checks for issues (missing workflows, docs, routing problems)
- Suggests reorganization
- Asks "Reorganize?" before making changes

**Output:** Properly structured skills (if approved)

---

## Step 4: Document & Backup (Handoff)

```
/handoff
```

**What to expect:**
- Generates `.agents/handoff/YYYY-MM-DD-topic.md` with accomplishments, pause point, blockers
- Creates git commit
- Pushes to GitHub
- Returns copyable summary

**Output:** Handoff document + GitHub backup

---

## Step 5: Google Drive Sync (Automatic)

If Google Drive MCP is installed, the handoff document is automatically synced.

**Output:** Backup copy in Google Drive (if configured)

---

## Execution Notes

- Each step is **independent** — user can skip or rerun any step
- Confirmation checkpoints give user **full control** — no changes without approval
- All steps are **reversible** — changes are committed to git
- Takes ~5-10 minutes for full run

---

## Success Criteria

✓ Learnings extracted and skills updated (if approved)  
✓ Skills reviewed and improved (if needed)  
✓ Folder structure verified and organized (if needed)  
✓ Handoff document created and committed  
✓ GitHub backup complete  
✓ Google Drive sync (if available)  

Session is now closed and ready for next session.
