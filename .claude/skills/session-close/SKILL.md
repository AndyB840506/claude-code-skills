---
name: session-close
description: "Complete session closing workflow: analyze learnings, review skills, organize structure, backup to GitHub + auto-sync to Google Drive. Triggers: session close, end session, closing session, cierre de sesión, cerrar sesión, session wrap-up, wrap up, end-of-session."
---

# Session Close — Automated Complete Workflow

Automated 5-step workflow that executes automatically when invoked. No manual steps required.

**Execution sequence:** Retrospective → Prompt Reviewer → Skill Management → Handoff → Google Drive Backup

---

## What It Does

Closes your session completely in one command. Executes all 5 steps automatically:

1. **Retrospective** — Extract learnings, propose skill updates
2. **Prompt Reviewer** — Review and improve updated skills  
3. **Skill Management** — Verify folder structure, suggest fixes
4. **Handoff** — Generate handoff document, create git commit + push
5. **Google Drive Backup** — Copy handoff to `G:\My Drive\claude projects`

All steps run sequentially. Each step completes before the next begins.

---

## Output

✓ Skill improvements applied (approved by you mid-flow)  
✓ Handoff document created and backed up  
✓ Git commit made and pushed to GitHub  
✓ Handoff copied to Google Drive backup folder  
✓ Summary displayed with all changes

---

## When to Use

See [When to Use](docs/when-to-use.md) for detailed guidelines, but quick version:
- **End of major sessions** — after creating/modifying skills or fixing bugs
- **End of day** — batch daily changes into one session close
- **Before handing off** — ensure everything is documented and backed up

---

## EXECUTION

**You invoke:** `/session-close`

**Automation executes all 5 steps in sequence (you only confirm approval prompts):**

1. **Step 1: Retrospective** — Scans conversation for learnings, proposes skill updates
   - Shows: Learnings found
   - **You confirm:** "Apply these changes?" → YES/NO
   - Updates approved skills

2. **Step 2: Prompt Reviewer** — Reviews updated skills, finds clarity issues
   - Shows: Improvements found
   - **You confirm:** "Apply improvements?" → YES/NO
   - Updates approved skills

3. **Step 3: Skill Management** — Audits folder structure, identifies issues
   - Shows: Structure issues found
   - **You confirm:** "Reorganize?" → YES/NO
   - Applies approved reorganization

4. **Step 4: Handoff** — Generates document, creates commit, pushes to GitHub
   - Runs automatically (no confirmation needed)
   - Creates `.agents/handoff/YYYY-MM-DD-topic.md`
   - Commits and pushes to GitHub
   - Copies summary to clipboard

5. **Step 5: Google Drive Backup** — Copies handoff to Google Drive backup folder
   - Runs automatically (no confirmation needed)
   - Copies to `G:\My Drive\claude projects\`
   - Google Drive Desktop auto-syncs to cloud

**Result:** All 5 steps complete automatically. Session fully closed, documented, backed up.

---

**Implementation details:** See [INSTRUCTIONS.md](INSTRUCTIONS.md) for auto-execution rules and error handling.

