---
name: prompt-reviewer
description: "Audit and improve prompts, skills, and instructions. Finds clarity issues, completeness gaps, and ineffectiveness. Proposes specific fixes with reasoning. Asks for confirmation before applying changes. Better and faster than generic tools. Triggers: review prompt, evaluate skill, improve instructions, prompt audit, skill review, instruction check, this is unclear, fix my prompt."
---

# Prompt Reviewer — Audit and Improve

Analyzes prompts, skills, and instructions to find clarity issues, gaps, and ineffectiveness. Proposes specific, executable fixes.

**Core rule:** Return concrete improvements — not vague criticism. Every finding includes the exact problem, why it matters, and the solution.

**Always asks for confirmation before applying changes.**

---

## Quick Start

```
/prompt-reviewer
```

Or specify analysis depth:

```
/prompt-reviewer quick
/prompt-reviewer thorough
```

---

## How It Works

**4-Step Workflow:**

1. **Choose Mode** — Quick (5 min) or Thorough (15 min)
2. **Audit** — Find clarity issues, gaps, ineffective patterns
3. **Propose** — Suggest specific improvements with reasoning
4. **Confirm** — Apply only if you approve

---

## What It Finds

- **Clarity issues** — Ambiguous language, confusing structure
- **Gaps** — Missing steps, undefined terms, no examples
- **Ineffectiveness** — Vague instructions, missing context
- **Pattern violations** — Inconsistent style, poor naming

---

## Output

Problem identification + before/after examples + ready to apply or skip

---

## EXECUTION

You have invoked `/prompt-reviewer`. Now audit the skills and documentation.

### Step 1: Choose Mode

**Default: QUICK MODE** (5 minutes)
- Review recently modified skills only
- Check for critical clarity issues
- Identify major gaps

**If user specified "thorough": THOROUGH MODE** (15 minutes)
- Review ALL skills in `.claude/skills/` comprehensively
- Check for syntax, consistency, and completeness
- Deep analysis of structure, patterns, and alignment
- Full effectiveness audit across entire skill library

### Step 2: Audit for Issues

Scan the skill files for:

**Clarity Issues:**
- Ambiguous language ("might", "sometimes", "could")
- Confusing structure (poor organization)
- Undefined terms or acronyms
- Contradictory statements
- Vague instructions

**Gaps:**
- Missing steps in workflows
- Undefined terms without examples
- No explanation of why something matters
- Missing edge case handling
- Incomplete decision trees

**Ineffectiveness:**
- Overly wordy explanations (should be concise)
- Missing context about when to use something
- Weak command/instruction clarity
- Poor examples or no examples at all
- Inconsistent formatting/style

**Pattern Violations:**
- Inconsistent naming (camelCase vs snake_case)
- Different documentation structure than other skills
- Breaking established conventions
- Tone mismatch with rest of project

### Step 3: Propose Improvements

For each issue found, provide:

**Problem:**
```
File: workflows/execute.md
Line: 15
Issue: "Run the steps" is vague
Why it matters: User doesn't know if steps run in parallel or sequence
```

**Solution:**
```
- OLD: "Run the steps"
+ NEW: "Execute steps in this order (each waits for confirmation before next starts)"
```

### Step 4: Ask Confirmation

Present all findings and ask:

> **Apply these improvements?**
>
> Found X issues across Y skills:
> - Z clarity issues
> - Z gaps
> - Z ineffectiveness
>
> [Show summary of improvements]
>
> Continue? [yes/no]

Wait for user response.

### Step 5: Apply Changes (If Approved)

If user said YES:
- Update each skill file with improvements
- Show confirmation for each change
- Summarize improvements made

If user said NO:
- Discard all changes
- Return to main workflow

---

**Prompt review complete!** Skills audited and improved (if approved).
