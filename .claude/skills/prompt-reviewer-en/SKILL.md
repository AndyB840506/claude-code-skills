---
name: prompt-reviewer-en
description: "Evaluate and improve prompts, skills, and instructions. Find clarity issues, missing edge cases, and effectiveness gaps. Propose specific, executable fixes with reasoning. Asks for confirmation before applying changes. Better than generic tools. Triggers: review prompt, evaluate skill, improve instructions, prompt audit, skill review, instruction check, is this clear, this is unclear, fix my prompt."
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
