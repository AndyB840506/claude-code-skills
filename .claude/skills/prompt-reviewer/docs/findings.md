# What the Prompt Reviewer Finds

The Prompt Reviewer scans for these categories of issues:

## Clarity Issues
- **Ambiguous language** — Vague verbs, unclear references, words with multiple meanings
- **Confusing structure** — Poor ordering, illogical grouping, missing transitions
- **Unexplained jargon** — Technical terms without definition, domain-specific acronyms

## Gaps
- **Missing steps** — Procedures that skip critical actions without explanation
- **Undefined terms** — References to concepts introduced nowhere in the text
- **No examples** — Instructions without concrete illustration or sample output

## Ineffectiveness
- **Vague instructions** — "Do X well" without criteria for success
- **Missing context** — Rules stated without the reasoning behind them
- **Incomplete workflows** — Procedures that don't specify decision points or error handling

## Pattern Violations
- **Inconsistent style** — Mixing passive and active voice, varying terminology
- **Poor naming** — Function/variable names that don't reflect their purpose
- **Formatting inconsistency** — Varying bullet styles, heading levels, code fence types

## How the Reviewer Works

For each issue found, the review includes:
1. **The exact problem** — Quote the problematic text
2. **Why it matters** — How it affects understanding or execution
3. **The solution** — Specific before/after fix with reasoning

All changes require explicit user confirmation before applying.
