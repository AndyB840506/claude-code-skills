---
name: prompt-reviewer
description: "Review and improve a prompt — system prompt, user prompt, or LLM instruction. Analyze clarity, specificity, potential failure modes, and output a scored assessment plus an improved version. English triggers: review this prompt, improve this prompt, audit this prompt, evaluate these instructions, this prompt is bad, review my system prompt, prompt not working, score this prompt, fix my prompt. Spanish triggers: revisar prompt, mejorar prompt, evaluar prompt, este prompt no funciona, auditar instrucciones, revisar instrucciones, mejorar instrucciones, puntuar prompt, corregir prompt."
---

# Prompt Reviewer

Analyze a prompt and produce: a scored assessment, identified issues, and an improved version.

## Process

### 1. Identify the prompt to review
- If the user pasted it directly, use that.
- If it's in a file, read the file first.
- If it's a system prompt in the codebase, locate and read it.

### 2. Classify the prompt type
- **System prompt** — sets AI behavior/persona/rules
- **User prompt** — single instruction or question
- **Chain prompt** — multi-step reasoning instruction
- **Few-shot prompt** — includes examples
- **Structured output prompt** — asks for JSON/XML/specific format

### 3. Score across 6 dimensions (1–10 each)

| Dimension | What to assess |
|---|---|
| **Clarity** | Is the instruction unambiguous? Would two people interpret it the same way? |
| **Specificity** | Are constraints, output format, scope, and limits clearly defined? |
| **Context** | Does the prompt give the model enough background to respond well? |
| **Failure resistance** | Does it guard against common failure modes (hallucination, scope creep, refusals)? |
| **Efficiency** | Is it as short as it can be without losing precision? No padding, no redundancy. |
| **Output control** | Is the expected output format, length, and style clearly specified? |

### 4. Output the review

---

## Prompt Review

**Type:** [System / User / Chain / Few-shot / Structured output]
**Length:** [X words / X tokens approx]

### Scores
| Dimension | Score | Note |
|---|---|---|
| Clarity | X/10 | ... |
| Specificity | X/10 | ... |
| Context | X/10 | ... |
| Failure resistance | X/10 | ... |
| Efficiency | X/10 | ... |
| Output control | X/10 | ... |
| **Overall** | **X/10** | |

### Critical Issues
List 2–4 specific problems that would cause the prompt to underperform. Quote the exact phrase or section causing the issue.

### Minor Issues
List 1–3 smaller improvements (style, redundancy, phrasing).

### Improved Version
Provide the full rewritten prompt. Mark changes with `[CHANGED: reason]` inline comments on first pass, then show the clean version.

### What Was Preserved
Note 2–3 things from the original that were kept intentionally and why.

---

## Scoring Guide

| Score | Meaning |
|---|---|
| 9–10 | Production-ready, no significant issues |
| 7–8 | Good, minor improvements recommended |
| 5–6 | Functional but will cause frequent edge-case failures |
| 3–4 | Significant structural problems, needs rewrite |
| 1–2 | Fundamentally broken — will not produce reliable output |

## Rules
- Always quote the specific text causing an issue — don't be vague.
- The improved version must be complete and immediately usable, not a skeleton.
- If the prompt is in Spanish, write the review in Spanish. If in English, in English.
- Don't add features the user didn't ask for. Improve what's there, don't redesign.
- Be direct. "This is ambiguous" is better than "This could potentially be interpreted as..."
