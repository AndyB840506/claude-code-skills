---
name: prompt-reviewer-en
description: "Evaluate and improve prompts, skills, and instructions. Find clarity issues, missing edge cases, and effectiveness gaps. Propose specific, executable fixes with reasoning. For Spanish, use /prompt-reviewer. Triggers EN: review prompt, evaluate skill, improve instructions, prompt audit, skill review, instruction check, is this clear, this is unclear, fix my prompt, review my system prompt, audit instructions, prompt not working."
---

# Prompt Reviewer EN — Evaluate and Improve

Analyzes prompts, skills, and instructions to find clarity issues, gaps, and ineffectiveness. Proposes specific, executable fixes.

**Core rule:** Return concrete improvements — not vague criticism. Every finding includes the exact problem, why it matters, and the solution.

**Always asks for confirmation before applying changes.**

---

## Quick Start

```
/prompt-reviewer-en
```

Or specify analysis depth:

```
/prompt-reviewer-en quick
/prompt-reviewer-en thorough
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

## See Also

- [Execution Workflow](workflows/execute.md) — Step-by-step audit process

---

## EXECUTION

You have invoked `/prompt-reviewer-en`. Now execute the 4-step audit workflow:

1. **Choose Mode** — Quick (5 min) or Thorough (15 min) analysis depth
2. **Audit** — Scan for clarity issues, gaps, ineffectiveness, pattern violations
3. **Propose** — Generate specific improvements with before/after examples
4. **Confirm & Apply** — Present findings and apply only if user approves

See [Full Workflow](workflows/execute.md) for detailed step-by-step instructions.

**Result:** Skills reviewed and improved (if approved).
