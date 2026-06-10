---
name: prompt-reviewer-en
description: "Evaluate and improve prompts, skills, and instructions. Find clarity issues, missing edge cases, and effectiveness gaps. Propose specific, executable fixes with reasoning. For Spanish, use /prompt-reviewer. Triggers EN: review prompt, evaluate skill, improve instructions, prompt audit, skill review, instruction check, is this clear, this is unclear, fix my prompt, review my system prompt, audit instructions, prompt not working."
---

# Prompt Reviewer EN — Evaluate and Improve

Analyzes prompts, skills, and instructions to find clarity issues, gaps, and
ineffectiveness. Proposes specific, executable fixes.

**Core rule:** Return concrete improvements — not vague criticism. Every finding
includes the exact problem, why it matters, and the solution. **Always asks for
confirmation before applying changes.**

## Quick Start

```
/prompt-reviewer-en           # default depth
/prompt-reviewer-en quick      # 5 min
/prompt-reviewer-en thorough   # 15 min
```

## What It Finds

- **Clarity issues** — Ambiguous language, confusing structure
- **Gaps** — Missing steps, undefined terms, no examples
- **Ineffectiveness** — Vague instructions, missing context
- **Pattern violations** — Inconsistent style, poor naming

## Workflow

Follow `workflows/execute.md` — choose mode, audit, propose fixes with before/after
examples, then apply only after user confirms.
