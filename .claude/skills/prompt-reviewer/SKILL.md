---
name: prompt-reviewer
description: "Audita y mejora prompts, skills e instrucciones. Encuentra problemas de claridad, gaps de completitud e inefectividad. Propone fixes específicos con razonamiento. Para inglés, usar /prompt-reviewer-en. Triggers ES: revisar prompt, evaluar skill, mejorar instrucciones, auditar prompt, revisar skill, revisar instrucciones, esto no está claro, corregir mi prompt, mejorar mi prompt, auditar instrucciones, prompt no funciona."
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

## Output

Problem identification + before/after examples + ready to apply or skip

---

## See Also

- [What It Finds](docs/findings.md) — Patterns and examples
- [Execution Workflow](workflows/execute.md) — Step-by-step audit process

---

## EXECUTION

You have invoked `/prompt-reviewer`. Now execute the 4-step audit workflow:

1. **Choose Mode** — Quick (5 min) or Thorough (15 min) analysis depth
2. **Audit** — Scan for clarity issues, gaps, ineffectiveness, pattern violations
3. **Propose** — Generate specific improvements with before/after examples
4. **Confirm & Apply** — Present findings and apply only if user approves

See [Full Workflow](workflows/execute.md) for detailed step-by-step instructions.

**Result:** Skills reviewed and improved (if approved).
